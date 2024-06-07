# Let me take you through the workflow
### Frontend
1. Create ```index.html``` and add the cdn of ```tailwind css``` in the head
2. Create ```login.html``` and add the cdn of ```tailwind css``` in the head
3. Create other html files with tailwind css


### Backend
4. Create a ```backend``` directory
5. Create a django folder project using ```django-admin startproject name_of_project```
6. ```cd``` into project folder ```ai_blog_app``` and create django app using ```python3 manage.py startapp blog_generator```
    - Project: ```C:\Users\HP\Documents\KESHTECH\PYTHON\Python_Projects\AI-YT-Blog_Generator\backend\ai_blog_app\ai_blog_app```
    - App: ```C:\Users\HP\Documents\KESHTECH\PYTHON\Python_Projects\AI-YT-Blog_Generator\backend\ai_blog_app\blog_generator```
7. Add the app ```blog_generator``` to ```Project\settings.py``` under ```INSTALLED_APPS```
    ```
    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog_generator'
]
    ```

8. Create ```urls.py``` to contain all the urls used in the application
    - ```App\urls.py``` means it is created in the ```blog_generator``` App folder
9. Update ```App\views.py``` to contain ```def index(request):``` for home page path in ```App\urls.py```
10. Setup ```include``` in the ```Project\urls.py```
11. Setup HTML templates
    - Create ```templates``` folder as in ```C:\Users\HP\Documents\KESHTECH\PYTHON\Python_Projects\AI-YT-Blog_Generator\backend\ai_blog_app\templates```
    - Add the templates to ```Project\settings.py``` under ```TEMPLATES``` under ```'DIRS': [BASE_DIR, 'templates']```
    - Copy all the html files into the ```templates``` folder

    