# #base image
# # base image  
# FROM python:3
# # setup environment variable  
# ENV PYTHONUNBUFFERED 1
# ENV DockerHOME=/home/app/webapp  

# # set work directory  
# RUN mkdir /app

# # # where your code lives  
# WORKDIR /app

# #installRequirements
# COPY requirements.txt /app/
# RUN pip3 install -r requirements.txt

# # copy entire project folder to /app 
# COPY . /app/
# # # set environment variables  
# # ENV PYTHONDONTWRITEBYTECODE 1
# # ENV PYTHONUNBUFFERED 1  
# # # install dependencies  
# # RUN pip install --upgrade pip  
# # # copy whole project to your docker home directory. COPY . $DockerHOME  
# # # run this command to install all dependencies  
# # RUN pip install -r requirements.txt  
# # # port where the Django app runs  
# # EXPOSE 8000  
# # # # start server  
# # CMD python manage.py runserver 
FROM python:3


ENV PYTHONUNBUFFERED 1

WORKDIR /webapp

ADD . /webapp

COPY ./requirements.txt /webapp/

RUN pip install -r requirements.txt  

COPY  . /webapp

RUN python manage.py collectstatic --noinput --clear

CMD gunicorn BackendApi_Dev.wsgi:application

