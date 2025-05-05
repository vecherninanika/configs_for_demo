pip install django
django-admin startproject demo .
python manage.py migrate
python manage.py startapp reader_app
# добавить в INSTALLED_APPS "reader_app.apps.ReaderAppConfig"
# создать модели
#python manage.py makemigrations reader_app
#python manage.py migrate
pip install djangorestframework
# ER
pip install pygraphviz
python manage.py graph_models -a -g -o my_project_visualized.png
# tests coverage
pip install coverage
#coverage run --source=reader_app manage.py test reader_app
#coverage report
# linter
pip install flake8 pylint black isort
#black .
#isort .