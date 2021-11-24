FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /usuarios

WORKDIR /usuarios

ADD . /usuarios/

RUN pip install -r requirements.txt

ENV PORT 8080
EXPOSE 8080

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:$PORT