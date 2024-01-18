FROM python:3.8  

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
RUN python manage.py makemigrations
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]