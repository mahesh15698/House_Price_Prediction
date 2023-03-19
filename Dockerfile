FROM python:3.9.0
COPY . /application
WORKDIR /application
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT application:app
