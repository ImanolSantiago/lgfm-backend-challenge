from rest_framework.views import APIView
from rest_framework.response import Response
from oscar.apps.basket.models import Basket
from oscar.apps.catalogue.models import Product, Category
from .serializers import productSerializer, bookSerializer, userSerializer, basketSerializer


class productTypeView(APIView):
    def get(self, request, format=None):
        try:
            detailed = True if self.request.query_params.get('detailed', "False").lower() == "true" else False
            response = []
            # Dependiendo de "detailed" (True o False), trae todas las categorias o solo las principales:
            categories_list = Category.objects.all() if detailed else Category.objects.filter(depth=1)

            for item in categories_list:
                response.append(productSerializer(item).data)

            return Response({"status": 200,
                            "message": response})

        except Exception as error:
            return Response({"status": 500,
                            "message": "Error: " + str(error)})


class booksView(APIView):

    def get(self, request, format=None):
        try:
            genre = self.request.query_params.get('genre', "Books").lower().strip().replace(" ", "-")
            response = []
            for item in Product.objects.all().filter(product_class_id=2):
                print(item)
                slug_name = item.categories.all()[0].full_slug  # Example books/non-fiction/hacking'
                if genre in slug_name:
                    # Para no mezclar los resultados de "fiction" con "non-fiction":
                    if not (genre == "fiction" and "non" in slug_name):
                        response.append(bookSerializer(item).data)

            return Response({
                            "status": 200,
                            "message": response,
                            "books_count": len(response)
                            })

        except Exception as error:
            return Response({"status": 500,
                            "message": "Error: " + str(error)})


class ordersView(APIView):
    def get(self, request, format=None):
        try:
            response = []
            for item in Basket.objects.all():
                basket_serialized = basketSerializer(item).data
                basket_serialized["user"] = userSerializer(item.owner).data
                response.append(basket_serialized)

            return Response({"status": 200,
                            "message": response})

        except Exception as error:
            return Response({"status": 500,
                            "message": "Error: " + str(error)})
