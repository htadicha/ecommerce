#  Tadicha Hussey E-commerce Platform

![Project Banner](./static/readmeimg/banner.png)

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/htadicha/ecommerce)
[![Django Version](https://img.shields.io/badge/Django-3.2.25-blueviolet)](https://www.djangoproject.com/)
[![Python Version](https://img.shields.io/badge/Python-3.12-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Tadicha Hussey** is a full-stack e-commerce web application built with Python and the Django framework. It provides a complete online shopping experience, featuring robust product management, secure user authentication, and a seamless checkout process for both registered users and guests.

**[➡️ View the Live Project Here](https://tadichaecommercestore-6c140a2ed1bd.herokuapp.com/)**

---

## Table of Contents

- [Key Features](#key-features)
- [Technology Stack](#technology-stack)
- [Database Schema](#database-schema)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Local Development Setup](#local-development-setup)
- [Testing](#testing)
- [Deployment](#deployment)
- [Future Roadmap](#future-roadmap)
- [Credits](#credits)
- [License](#license)

---

## Key Features
![Project Banner](./static/readmeimg/navigation.png)
Tadicha Hussey provides a feature-rich experience tailored to different user roles, ensuring a smooth and intuitive journey from browsing to purchase. The functionality is broken down by page and component below.

### Home Page
![Project Banner](./static/readmeimg/navigation.png)
- **All Users (Visitor, Registered, Admin):**
    - View featured products and promotional banners.
    - Navigate to all main sections of the site via the navigation bar.
    - Access the search bar to find products.

### Store Page
![Project Banner](./static/readmeimg/store.png)
- **All Users (Visitor, Registered, Admin):**
    - Browse a comprehensive grid of all available products.
    - View key product details like name, image, and price.
    - Click on any product to navigate to its detailed view.
- **Sorting Functionality:**
![Project Banner](./static/readmeimg/navigation.png)
    - Sort products by name, price, or category to easily find desired items.
- **Responsive Design:**
    - The product grid adapts seamlessly to any screen size, from mobile to desktop. ([View Responsiveness Details](RESPONSIVE.md))

### Product Detail Page
![Project Banner](./static/readmeimg/navigation.png)
- **All Users (Visitor, Registered, Admin):**
    - View detailed product information, including multiple images, description, color, and product code.
    - See stock availability and status (e.g., New, Deal, Clearance).

### Search Bar & Results
![Project Banner](./static/readmeimg/navigation.png)
- **All Users (Visitor, Registered, Admin):**
    - Search for products sitewide using keywords.
    - Receive clear feedback if a search yields no results.
    - View results on a dedicated page that displays all matching products.

### Cart Page
![Project Banner](./static/readmeimg/cart.png)
- **Visitor (Guest User):**
    - Add items to a temporary cart that is stored using browser cookies.
    - View all items, quantities, and totals in the cart.
    - Remove items from the cart.
- **Registered User & Admin:**
    - All guest functionalities.
    - The cart is persistently saved to the user's account, accessible across different devices.
    - **Full CRUD Functionality:** Can add, view, update item quantities, and remove items.

### Checkout Page
- **Visitor (Guest User):**
    - Proceed to checkout and provide shipping and payment information to complete the purchase without creating an account.
- **Registered User & Admin:**
    - Enjoy a streamlined checkout process where saved information can be used to pre-fill forms.
    - Can review the order summary before finalizing the purchase.
    - Ability to easily navigate back to the cart to make changes.

### ⚙️ For Site Administrators (Superuser)
- **Full Product Management (CRUD):** From the Django admin panel, the superuser can create, read, update, and delete products, including all their details and images.
- **Order Fulfillment:** View and manage all customer orders, update their status (e.g., "Shipped"), and track fulfillment.
- **User Management:** Oversee all registered users, manage their permissions, and ensure data integrity.

---

## Technology Stack

This project leverages a modern and robust stack to deliver a high-performance, scalable e-commerce solution.

| Category      | Technology / Library                                                                                                                              |
| :------------ | :------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Backend** | [**Python**](https://www.python.org/), [**Django**](https://www.djangoproject.com/), [**Gunicorn**](https://gunicorn.org/)                           |
| **Frontend** | [**HTML5**](https://en.wikipedia.org/wiki/HTML/), [**CSS3**](https://en.wikipedia.org/wiki/CSS), [**JavaScript**](https://www.javascript.com/), [**Bootstrap**](https://getbootstrap.com/) |
| **Database** | [**PostgreSQL**](https://www.postgresql.org/) (Production), [**SQLite3**](https://www.sqlite.org/index.html) (Development)                           |
| **Deployment**| [**Heroku**](https://www.heroku.com/), [**Cloudinary**](https://cloudinary.com/) (Media Hosting), [**WhiteNoise**](http://whitenoise.evans.io/) (Static Files) |
| **Key Packages**| [**Django Allauth**](https://django-allauth.readthedocs.io/) (Auth), [**Crispy Forms**](https://django-crispy-forms.readthedocs.io/) (Forms), [**Psycopg2**](https://pypi.org/project/psycopg2/) |

---

## Database Schema

The database is designed with a normalized structure to ensure data integrity and efficiency. The core models include `Account`, `Product`, `Category`, `Cart`, `Order`, and `Payment`, with clear relationships defined between them.

![Database Diagram](./static/images/database_wireframe.png)

*This diagram was created using Lucidchart.*

---

## Getting Started

To run a local copy of this project, follow the steps below.

### Prerequisites

- Python 3.10+
- PIP (Python Package Installer)
- Git

### Local Development Setup

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/htadicha/ecommerce.git](https://github.com/htadicha/ecommerce.git)
    cd ecommerce
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set Up Environment Variables:**
    - Create a new file named `env.py` in the root directory.
    - Add your local configuration variables to this file. **Note:** This file should be added to `.gitignore` and never committed.
    ```python
    # env.py
    import os

    os.environ['SECRET_KEY'] = 'your-super-secret-key-for-local-dev'
    # Use a local SQLite database for simplicity
    # os.environ['DATABASE_URL'] = 'postgres://user:password@localhost/dbname' 
    os.environ['CLOUDINARY_URL'] = 'cloudinary://api_key:api_secret@cloud_name'
    ```

4.  **Apply Migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Create a Superuser:**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the Development Server:**
    ```bash
    python manage.py runserver
    ```
    The project will be available at `http://127.0.0.1:8000/`.

---

## Testing

Comprehensive testing has been performed to ensure application stability and functionality. For detailed information on the testing process, including manual and automated testing results, please see the [TESTING.MD](TESTING.MD) file.

---

## Deployment

This application is deployed on **Heroku** using a **PostgreSQL** database.

- **Static files** are managed by **WhiteNoise**.
- **Media files** (user-uploaded images) are hosted on **Cloudinary**.

The deployment process involves:
1.  Creating a Heroku app and linking it to the GitHub repository.
2.  Adding the Heroku Postgres add-on.
3.  Configuring environment variables (`DATABASE_URL`, `SECRET_KEY`, `CLOUDINARY_URL`) in the Heroku dashboard.
4.  Pushing the code to the main branch, which triggers an automatic deployment.

---

## Future Roadmap

The following features are planned for future releases to further enhance the platform:
-   **Advanced Product Filtering:** Implement category-specific filters for brand, price range, and other attributes.
-   **Payment Gateway Integration:** Integrate Stripe and PayPal to enable real-time credit card processing.
-   **Customer Reviews & Ratings:** Allow authenticated users to submit reviews and ratings for products.
-   **Order Tracking:** Provide users with a dashboard to view their order history and track the status of current shipments.
-   **Promotional Tools:** Add functionality for creating discount codes and promotional banners on the home page.

---

## Credits

-   **Content & Imagery:** Product images and initial content were sourced from [Freepik](https://www.freepik.com/free-photos-vectors/floral-shirt) and [Unsplash](https://unsplash.com/).
-   **Inspiration & Resources:** Guidance and solutions were adapted from documentation and community discussions on [W3Schools](https://www.w3schools.com/python/), [Stack Overflow](https://stackoverflow.com/), and various tutorials.
-   **Special Thanks:** A special thank you to the Code Institute community and my mentor for their invaluable support and guidance throughout this project.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
