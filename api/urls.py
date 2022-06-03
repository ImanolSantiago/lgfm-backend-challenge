from django.urls import path
from api.views import productTypeView, booksView, ordersView

urlpatterns = [
    path('product-types/', productTypeView.as_view()),
    path('books/', booksView.as_view()),
    path('orders/', ordersView.as_view()),
]
