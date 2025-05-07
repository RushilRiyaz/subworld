# SubWorld

SubWorld is a community driven SubWay sandwich discovery platform. It provides the following features:
- User authentication and profiles with image uploads
- Creating, viewing and deletion of sandwich posts with attributes (vegan, temperature, size, bread, meat, cheese, veggies, sauces, price)
- Bookmarking and commenting on posts
- Advanced filtering and searching of sandwich posts
- Shopping cart functionality with checkout
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
   pip freeze > requirements.txt
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
  


