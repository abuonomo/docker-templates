FROM python:3.7 as base

LABEL org.label-schema.description="flask-docker template for easy pathing"
LABEL org.label-schema.url=""

USER root
RUN mkdir service
COPY requirements.txt /service/requirements.txt
RUN pip install -r /service/requirements.txt

COPY static /service/static
COPY templates /service/templates
COPY app.py /service/
RUN chown -R www-data:www-data /service/templates/
WORKDIR /service/
USER www-data
CMD gunicorn app:app -b :5000 --timeout 1200
