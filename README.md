# E-commerce Platform

![Project Banner](./static/readmeimg/banner.png)


[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/htadicha/ecommerce)
[![Django Version](https://img.shields.io/badge/Django-3.2.25-blueviolet)](https://www.djangoproject.com/)
[![Python Version](https://img.shields.io/badge/Python-3.12-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**GreatCart** is a full-stack e-commerce web application built with Python and the Django framework. It provides a complete online shopping experience, featuring robust product management, secure user authentication, and a seamless checkout process for both registered users and guests.

**[➡️ View the Live Project Here](https://tadichaecommercestore-6c140a2ed1bd.herokuapp.com/)**

---

## Table of Contents

- [User Experience (UX) & Project Scope](#user-experience-ux--project-scope)
- [Key Features](#key-features)
- [Design](#design)
- [Technology Stack](#technology-stack)
- [Database Schema](#database-schema)
- [Getting Started](#getting-started)
- [Testing](#testing)
- [Deployment](#deployment)
- [Future Roadmap](#future-roadmap)
- [Credits](#credits)
- [License](#license)

---

## User Experience (UX) & Project Scope

This section details the project's planning phase, including user stories and the overall goals of the application.

### User Stories

User stories were created to define the required functionality from the perspective of different types of users.

#### As a Website Visitor, I can:
- Navigate around the site and easily view the desired content.
- View a list of available products to purchase and choose accordingly.
- Search for products.
- Add products to a temporary cart and remove them.
- View the cart and see the totals on the cart page.
- Sign up to create a new account.

#### As a Logged-in User, I can:
- Perform all actions available to a website visitor.
- Have a persistent shopping cart saved to my account.
- Control the number of items in my cart (perform CRUD functionality without accessing the admin panel).
- Check out and have my saved information pre-fill the address forms.
- Log in and out of my account securely.

#### As a Website Superuser (Admin), I can:
- Perform all actions available to a logged-in user.
- Create, update, and delete products, including their prices and images.
- Control user access and change website permissions for other users.
- View and manage all customer orders.
- Create new user accounts tied to customer instances.

### Agile Methodology

The project's development was managed using an agile approach, with user stories and tasks tracked as issues on GitHub. The project board can be found [here](https://github.com/htadicha/ecommerce/issues).

### Project Goals

- To provide an excellent and intuitive user experience.
- To create a visually pleasing website that is easy to navigate.
- To implement role-based permissions, giving registered users a streamlined checkout advantage.
- To provide effective tools, like the search bar, for users to find products easily.

---

## Key Features

GreatCart provides a feature-rich experience tailored to different user roles, ensuring a smooth and intuitive journey from browsing to purchase.

### Page-by-Page Functionality

#### Home Page
![Cart Items](./static/readmeimg/home.png)
- **All Users:** View an engaging hero slider, key service promises (Free Shipping, Money-Back Guarantee), and a grid of the latest products.
- **Functionality:** Browse featured items and navigate to all site sections.

#### Shope Page
![Cart Items](./static/readmeimg/store.png)
- **All Users:** Browse a comprehensive grid of all products.
- **Sorting:** Sort products by **Name**, **Price**, or **Best Rated**. The selected sort order persists.
![Cart Items](./static/readmeimg/sortby.png)

#### Cart & Checkout

###### Cart

![Cart Items](./static/readmeimg/cartt.png)

###### Checkout
![Cart Items](./static/readmeimg/checkout.png)

- **Guest Users:** Can add items to a temporary cart (using cookies) and complete a purchase.
- **Registered Users:** Enjoy a persistent cart saved to their account and a faster checkout experience.
- **CRUD:** Users can update item quantities and remove items directly from the cart page.

### User Account Management

###### Signin

![Cart Items](./static/readmeimg/sign_in.png)

###### Registration
![Cart Items](./static/readmeimg/register.png¸)

The application features a robust user account system, powered by `django-allauth`, to provide a personalized and secure experience for registered users.

* **Secure Registration & Login:** New users can create an account with a secure, hashed password. The login system establishes a persistent session, allowing users to stay logged in across visits. With good user feedback for bith successiful login and registration

* **Persistent Shopping Cart:** A key advantage for registered users is that their shopping cart is saved to their account. They can add items on one device and complete the purchase later on another without losing their selections.

* **Role-based Permissions:** The system differentiates between standard users and superusers, ensuring that regular users can manage their own shopping experience while administrators have access to site-wide management tools.


#### Search & Navigation
- **All Users:** A sitewide search bar allows users to find products by keyword. The main navigation is present on all pages for easy access.

#### ⚙️ Site Administration (Superuser)
![Cart Items](./static/readmeimg/admin.png)
- **Full Product Management:** From the Django admin panel, the superuser can perform all CRUD operations on products.
- **Order Fulfillment:** View and manage all customer orders and update their status.
- **User Management:** Oversee all registered users and manage their permissions.

---

### Typography & Colour Scheme
- **Font:** The primary font used across the site is **'Poppins'**, sans-serif. This choice provides a clean, modern, and highly readable text display that complements the minimalist aesthetic.
- **Colours:** The color palette is intentionally minimalist to create a professional and user-friendly interface that focuses on the products.
    -   **White (`#FFFFFF`):** Used as the primary background color to create a sense of space and cleanliness.
    -   **Black (`#000000`):** Used for all primary text, ensuring maximum readability and contrast.
    -   **Light Grey (`#F8F9FA`):** Employed for secondary elements, such as section backgrounds or borders, to add subtle depth and separation without distracting from the main content.

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

![Database Diagram](./static/readmeimg/data_base_design.png)

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
    # Use a local SQLite database for simplicity, or your own Postgres string
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

A continuous and multi-faceted testing strategy was employed throughout the project lifecycle to ensure quality, functionality, and performance.

### Code Validation

-   **Python PEP8:** All Python code across the project (`views.py`, `models.py`, `forms.py`, etc.) was validated using `PEP8 Online` to ensure adherence to style standards and to identify any syntax errors. No errors were found.
-   **HTML Validation:** All HTML templates were validated using the [W3C HTML Validator](https://validator.w3.org/). Minor warnings related to Django template tags were noted but do not affect performance.
-   **CSS Validation:** Custom CSS was validated using the [W3C Jigsaw Validator](https://jigsaw.w3.org/css-validator/).
-   **JavaScript Validation:** JavaScript files were checked for syntax and logical errors. The browser console was monitored during manual testing to ensure no errors were present.

### Performance and Accessibility
-   **Lighthouse:** Google Lighthouse was used to audit the deployed site for Performance, Accessibility, Best Practices, and SEO.
 

### Manual Testing
Rigorous manual testing was performed across all features and user roles.

-   **User Authentication Flow:**
    -   **Signup:** Verified that new users can register successfully and are redirected appropriately. Form validation for existing emails and password mismatches works as expected.
    -   **Login/Logout:** Confirmed that registered users can log in with correct credentials, are blocked with incorrect ones, and can log out successfully.
-   **Store and Product Functionality:**
    -   **Navigation & Display:** All pages load correctly, products display with correct images and prices, and all navigation links direct to the correct pages.
    -   **Search:** Verified that searching for an existing product yields correct results and searching for a non-existent product returns a "No results found" message.
    -   **Sorting:** Confirmed that products on the store page can be sorted by name, price, and rating, with the selection persisting after reload.
-   **Shopping Cart & Checkout:**
    -   **Guest Cart:** Verified that non-logged-in users can add/remove items and the cart persists using cookies.
    -   **Registered User Cart:** Confirmed that the cart is saved to the user's account and that item quantities can be updated (CRUD).
    -   **Checkout:** Tested the full checkout flow for both guest and registered users, ensuring the order summary is correct and forms function as expected.
-   **Cross-Browser & Responsiveness:**
    -   The site was tested on Chrome, Firefox, and Safari to ensure consistent functionality and styling.
    -   Mobile responsiveness was verified on various device sizes using browser developer tools, ensuring layouts, forms, and the navigation menu adapt correctly.

### Fixed Bugs

Several bugs were identified and resolved during development:

1.  **`NoReverseMatch` for 'sign_up':** Solved by adding the correct URL pattern in `urls.py`.
2.  **`NameError` for undefined forms/functions:** Resolved by ensuring proper imports for `LoginForm` and `redirect` in `views.py`.
3.  **CSRF Token Error on POST:** Fixed by adding the `{% csrf_token %}` tag to all forms.
4.  **Login Not Redirecting:** Ensured the redirect URL after a successful login was correctly named and referenced.
5.  **Search Query Not Showing "No Results":** Added conditional logic to the search results template to display the message when the product query set is empty.

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