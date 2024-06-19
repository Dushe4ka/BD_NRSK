pip install -r requirements.txt   
django-admin startproject config .
python manage.py startapp main  
python manage.py inspectdb   
python manage.py makemigrations 
python manage.py migrate 
python manage.py createsuperuser 
python manage.py dumpdata main > BD.json 
