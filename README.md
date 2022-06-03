LGFM BackEnd Challenge - Build a DRF REST API
=========================


Overview of the Backend
------------------------

- The aim is to create some Django Rest Framework API endpoints that would eventually be used by a front end.
- The initial project of an example ecommerce shop is given (using the Oscar Commerce framework on Django), 
as well as the database containing some example data (already migrated).


Install Steps
------------------------

0. Running well on Python 3.9. Another version might be used.
1. Create virtual environment and install all dependencies in requirements.txt
2. Run "python manage.py runserver" to initialize the dev server.

You can see the example shop navigating to /catalogue
And you can enter the example Oscar Dashboard at /dashboard:
user: admin
pass: admin


Requirements
------------

Create 3 new endpoints inside api project. The endpoints should be reached under /api:
1. /product-types: Endpoint that returns a list of all the product types available at the store.
2. /books: Endpoint that returns a list of books in the store. If possible, make it able to filter by book genre passing 
a query param like e.g. /books?genre=fiction
3. /orders: Endpoint that returns a list of all orders placed. If possible, with nested serialization of basket,
user and user.


Tasks
-----

- [ ] Fork this repository and create a new branch with your name, e.g. dani-garcia
- [ ] Create the endpoints described in Requirements the best you can.
- [ ] OPTIONAL: If you want to impress, implement authentication for the 3 endpoints (e.g. session or token)
- [ ] Make a pull request when you are done.


Resolucion
------------
Comentarios
    /api/product-types//?detailed=PARAMETRO
        PARAMETRO=> True o False
        Por defecto trae los tipos "Books" y "Clothing". En el caso de especificar el parametro como True, se añade los subgeneros de libros.

    /api/books/?genre=PARAMETRO
        Parametros disponibles:
            *Books
            *Fiction
            *Computers in Literature
            *Non-Fiction
            *Essential programming
            *Hacking
        No influyen las mayusculas/minusculas. Ni los espacios en los extremos del parametros. Estan contemplados.

    Mejoras:
        En el endpoint de "product-types", que los subjeneros queden anidados correctamente dentro de "Books". Sin importar la cantidad de "padres" e "hijos".
        En el endpoint de "books", poder utilizar una relacion entre los modelos de los productos y las categorias.
        Reutilizar mejor los serializers heredando ciertos atributos en comun.