# SubWorld
<img width="1499" height="858" alt="homepage" src="https://github.com/user-attachments/assets/50797e58-a2f3-4013-852f-2175839247a5" />


SubWorld is a community driven SubWay sandwich discovery platform. It provides the following features:

- User authentication and profiles with image uploads
- Creating, viewing and deletion of sandwich posts with attributes (vegan, temperature, size, bread, meat, cheese, veggies, sauces, price, popularity)
- Bookmarking and commenting on posts
- Advanced filtering and searching of sandwich posts
- Shopping cart functionality with checkout
- Premium Subscription for 10% discount off of all purchases
- Media handling for sandwich and profile images

## Technology Stack

- Python 3.13.2
- Django 5.2
- SQLite 3 (default development database)
- Django Crispy Forms
- Django Filters
- Pillow (for image handling)
- HTML/CSS (Django templates and static files)
- Bootstrap4
- jQeury

## Installation

1. Clone the repository
   ```zsh
   git clone <repository-url>
   ```
2. Create and activate a virtual enviroment
   ```zsh
   python -m venv env
   source env/bin/activate
   ```
3. Install dependencies
   ```zsh
   pip install -r requirements.txt
   ```
4. Create superuser (optional)
   ```zsh
   cd backend
   python3 manage.py createsuperuser
   ```
5. Run the development server
   ```zsh
   cd backend
   python3 manage.py runserver
   ```
   The website will be accesible at http://127.0.0.1:8000/

## Previews
<img width="800" height="800" alt="homepage" src="https://github.com/user-attachments/assets/b0fe9a53-7c06-41e6-8755-9eaf3f58bc6f" />

<img width="1512" height="860" alt="post view" src="https://github.com/user-attachments/assets/140643af-715e-4bd3-bae7-b0f0642b10d1" />

<img width="1512" height="859" alt="filter" src="https://github.com/user-attachments/assets/07eedd09-d976-4f2e-b189-cc028a4d28f8" />

<img width="1512" height="859" alt="shopping cart" src="https://github.com/user-attachments/assets/99dbc773-2909-4dff-8ac1-da63a5d692e4" />

<img width="1512" height="859" alt="profile" src="https://github.com/user-attachments/assets/d3f74a67-b35d-4a01-b3fb-bd966765805c" />

<img width="1512" height="859" alt="checkout" src="https://github.com/user-attachments/assets/9e12b1c1-af46-46c0-b99b-95a4b19d5c70" />

<img width="1507" height="861" alt="register" src="https://github.com/user-attachments/assets/0dbfbe15-bd74-448d-b751-3df93f304eb3" />


