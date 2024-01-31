FROM python:3.9

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
RUN python ./analytics/manage.py makemigrations
RUN python ./analytics/manage.py migrate

EXPOSE 8000
CMD ["python", "./analytics/manage.py", "runserver", "0.0.0.0:8000"]