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

[Description](#description) | [Installation](#installation) | [Roadmap](#roadmap) | [Bonuses](#bonuses) | [Upcoming Features](#upcoming-features) | [License](#license)

<!-- DESCRIPTION -->
## Description

The **PetCare API** is a comprehensive platform designed to help users manage their pets, products, and orders. It provides a set of RESTful endpoints to facilitate user registration, authentication, and the management of pets, products, and orders. The API is structured into three main categories based on authorization levels: **Public**, **Authenticated Users**, and **Admin**.

### Key Features:
- **User Management**: Register, login, and change passwords.
- **Pet Management**: Add, view, edit, and delete pets.
- **Product Management**: View products (public) and manage product details (admin).
- **Order Management**: Place and manage product orders.
- **Vet Appointment Booking**: Schedule vet appointments for pets.

## API Structure

The PetCare API is structured into different endpoints based on user authentication levels:

### Public Endpoints
Accessible to all users (no authentication required):
- `POST /register` - Register a new user.
- `POST /login` - Log in to the API to obtain an authentication token.
- `GET /documentation` - Retrieve API documentation about the project.
- `GET /products` - View a list of all products.
- `GET /products/{product_id}` - View details of a specific product.

### Authenticated User Endpoints
Accessible only to authenticated users (via JWT token):
- `POST /pets/add_pet` - Add a new pet to the user’s account.
- `GET /pets` - Retrieve a list of the user’s pets.
- `POST /orders/place_order` - Place an order for products.
- `POST /users/change_password` - Change the user's password.
- `POST /appointments/book_appointment` - Book a vet appointment for a user's pet.

### Admin Endpoints
Restricted to users with admin roles:
- `POST /products/add_product` - Add a new product to the system.
- `POST /products/edit_product/{product_id}` - Edit an existing product.
- `POST /products/delete_product/{product_id}` - Remove a product from the system.
- `GET /pets` - Admins can view all pets in the system (not just their own).


All of the endpoints with example data and description that includes what kind of authorizations are needed, can be seen when you run the server.
This endpoint renders the template - (GetDocumentationPage, "/"),  # everyone can see the documentation page (public).


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


<!-- UPCOMING FUNCTIONALITIES -->
## Upcoming Features

- **Add an option to look for closest vet clinics**: In a future update, users will be able to look for the closest vet clinic near them by providing an address. Then they can use the already existing functionality to schedule appointments for their pets with veterinarians. This feature will allow pet owners to manage their pets’ health and wellness directly through the platform.


<!-- License -->
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
