<div align="center">
<p align=center>
<a href="https://softuni.bg">
<img src="https://codeweek-s3.s3.amazonaws.com/event_picture/SoftUni-Logo-Flat.png" alt="Logo" width="600">
</a>
<p>
<br><br>
<h1 align=center>PetCare</h1>
<h3 align=center>
</div>

[Description](#description) | [Installation](#installation) | [Endpoints](#endpoints) | [Roadmap](#roadmap) | [Bonuses](#bonuses) | [Future Functionalities](#future-functionalities)

<!-- DESCRIPTION -->
## Description

The PetCare API is a comprehensive platform designed to help users manage their pets, products, and orders. It provides a set of RESTful endpoints to facilitate user registration, authentication, and the management of pets, products, and orders. The API is structured into three main categories based on authorization levels: Public, Authenticated Users, and Admin.

Key Features:
User Management:

Users can register and log in to access personalized features.
Authenticated users can update their passwords.
Pet Management:

Authenticated users can add, view, edit, and delete their pets.
Admin users have additional privileges to view and manage all pets in the system.
Product Management:

Users can view all available products, as well as details about specific products.
Admin users can add, edit, and delete products.
Order Management:

Authenticated users can place orders for products. These orders are linked to the user’s account.
Vet Appointment Booking (Coming Soon):

Soon, users will be able to schedule appointments for their pets with veterinarians, making it easier for pet owners to ensure the health and well-being of their pets.
API Structure:
Public Endpoints: Available to everyone (no authentication required).

POST /register - Register a new user.
POST /login - Log in a user to obtain an authentication token.
GET /about - Retrieve information about the API.
GET /products - View a list of all products.
GET /products/{product_id} - View details of a specific product.
Authenticated User Endpoints: Available only to users who are logged in (authentication required via JWT token).

POST /pets/add_pet - Add a new pet to the user’s account.
GET /pets - Retrieve a list of the user’s pets.
POST /orders/place_order - Place an order for products.
POST /users/change_password - Change the user's password.
Admin Endpoints: Restricted to users with admin roles.

POST /products/add_product - Add a new product to the system.
POST /products/edit_product/{product_id} - Edit the details of an existing product.
POST /products/delete_product/{product_id} - Remove a product from the system.
GET /pets - Admins can view all pets in the system, not just those belonging to them.
Future Enhancements:
In the upcoming update, the PetCare API will introduce an endpoint for booking vet appointments. This feature will allow users to schedule appointments for their pets with certified veterinarians, ensuring that their pets receive necessary care and health check-ups.

This feature will further enrich the API by integrating pet care management into one centralized platform, providing pet owners with seamless access to essential services like appointments, product orders, and health tracking.

Conclusion:
The PetCare API is a powerful tool for managing pets, products, and orders, with easy access for both regular users and administrators. With the upcoming addition of the vet appointment booking feature, it will become an even more indispensable service for pet owners, ensuring that their pets live long, healthy lives.


<!-- INSTALLATION -->
## Installation

<h4>To install the project, you should first clone the repository and install the requirements:</h4>

```bash
git clone https://github.com/elly2chan/flask-pet-files-project.git
```
	
```bash
pip install -r requirements.txt
```
<br>

<h4>Next step is to create a .env file and configure the following:</h4>

```python
DB_USER = ""
DB_PASSWORD = ""
DB_HOST = ""
DB_PORT = ""

# Production/Development Database (if it's going to be the same)
DB_NAME = ""

# Test Database
TEST_DB_NAME = ""

# Used for jwt.encode and jwt.decode
SECRET_KEY = ""

# You can change the configuration environment from here (prod, dev, testing)
CONFIG_ENV=""

-----------------------------------------------------------------------------

# Other third party 'secrets'

WISE_API_KEY = ""
WISE_URL = ""
WISE_PROFILE_ID = ""

```	

<!-- ENDPOINTS -->
## Endpoints

<h4>The project has the following endpoints:</h4>
	
```python
routes = (
    (RegisterUser, "/register"),  # everyone can register
    (LoginUser, "/login"),  # everyone can log in
    (ChangePassword, "/users/change_password"),
    (GetDocumentationPage, "/"),  # everyone can see the documentation page (public)
    (AddPet, "/pets/add_pet"),  # only authenticated users can add pets
    (GetPets, "/pets"),  # only authenticated users can see their pets, admins can see all pets
    (EditPet, "/pets/edit_pet/<int:pet_id>"),  # only authenticated users can edit pets, admins can edit all
    (DeletePet, "/pets/delete_pet/<int:pet_id>"),  # only authenticated users can delete pets, admins can delete all
    (AddProduct, "/products/add_product"),  # only authenticated admins can add products
    (GetProducts, "/products"),  # everyone can see products (public part)
    (GetProduct, "/products/<int:product_id>"),  # everyone can see products (public part)
    (EditProduct, "/products/edit_product/<int:product_id>"),  # only admins can edit products
    (DeleteProduct, "/products/delete_product/<int:product_id>"),  # only admins can remove products
    (PlaceOrder, "/orders/place_order"),  # only authenticated users can place orders
)
```

<h4>Authentication/Authorization</h4>
	
```python
    (RegisterUser, "/register")
    (LoginUser, "/login")
    (ChangePassword, "/users/change_password")
```

<h4>Pets</h4>
	
```python
    (AddPet, "/pets/add_pet")
    (GetPets, "/pets")
    (EditPet, "/pets/edit_pet/<int:pet_id>")
    (DeletePet, "/pets/delete_pet/<int:pet_id>")
```

<h4>Products</h4>
	
```python
    (AddProduct, "/products/add_product")
    (GetProducts, "/products")
    (GetProduct, "/products/<int:product_id>")
    (EditProduct, "/products/edit_product/<int:product_id>")
    (DeleteProduct, "/products/delete_product/<int:product_id>")
```

<h4>Orders</h4>
	
```python
    (PlaceOrder, "/orders/place_order")
```

All of the endpoints with example data and description that includes what kind of authorizations are needed, can be seen when you run the server.
This endpoint renders the template - (GetDocumentationPage, "/"),  # everyone can see the documentation page (public).


<!-- ROADMAP -->
## Roadmap

- [X] The application must be implemented using FlaskRESTful Framework
- [X] The application must have at least 8 endpoints (up to 8 points)
- [X] The application must have authentication and authorization functionality (15 points)
- [X] The application must have public part (A part of the website, which is accessible by everyone – un/authenticated users and admins)
- [X] The application must have private part (accessible only by authenticated user or authenticated admins)
- [X] The application should have CRUD at least to a one resource a.k.a GET, POST, PUT and DELETE endpoint (not restricted to be for the same role) (10 points)
- [X] The application should be structured, using MVC pattern or similar (different directories/packages for managers, services, routes/resources) (20 points)
- [X] The input and output data should be validated and parsed against schemas (could be Marshmallow or similar) (15 points)
- [X] The application should have in general at least 2 custom and unlimited pre-built validators used in the schemas
- [X] The application should follow the principle of class-based views and good OOP practices (10 points)
- [X] Usage of ORM (flask_sqlalchemy/sqlalchemy or similar) (15 points)
- [X] The code should be formatted against pep8 standard (you can use black) (5 points)
- [X] All imports should be in the correct order (you can use ctr+alt+o in PyCharm for automatic reordering) (2 points)
- [X] Use a source control system by choice – GitHub is preferred. (10 points)
- [X] The application should use relational database for persistent storage (20 points)
- [X] All third-party libraries/packages should be listed in requirements.txt file in the root folder of the project with their versions
- [X] For database credentials or other secret keys and data you should use environment variables which are not committed in the repo (or hardcoded in the code) (10 points)
- [X] Gitignore file is mandatory to exclude all sensitive data, caches and etc. (5 points)
- [X] At least one page of good described ReadMe file (should include how to install the dependencies, what are the endpoints, which are protected, what they return and what are the conditions to access them, the description of the project itself, future functionality) (5 points)
- [X] At least one migration (up to 10 points – each migration is 2 points)
- [X] Tests (30 points)
- [X] At least 5 meaningful commits
- [X] At least 5 tests of the most crucial feature of the app including mocking if needed
- [X] 5 integration tests (api tests – from the request to this endpoint to the response)
- [X] Factories
- [X] The application should be integrated with some 3th service of your choice (could be AWS S3 or AWS Simple email service, or could be a payment provider of your choice) (25 points)


<!-- BONUSES -->
## Bonuses

- [X] Write tests for at least 60% coverage on your business logic
- [ ] Deployment
- [ ] CI or CD (with GitHub actions or Jenkins)
- [ ] Documentation / Swagger
- [X] Front end application (with framework like Angular, React VueJS or only vanilla JS) - partially, only one page is currently available
- [ ] Different patterns with meaningful usage
- [X] If the application is a creative app (something that helps you automate daily tasks, or we will be used by real users – your friends or family), something that solves an actual problem and has a potential to grow and be used
- [ ] Any other popular library like pandas, GraphQL and etc. with meaningful usage in the code


<!-- FUTUREFUNCTIONALITIES -->
## Future Functionalities

- [ ] Full front end application with React
- [ ] Add more 3th service integrations
- [ ] Add endpoints to book an appointment for your pet/s
