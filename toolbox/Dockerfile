FROM python:3.13

# กำหนดโฟลเดอร์หลักของโปรเจค
WORKDIR /app

COPY /app/

# ติดตั้ง dependencies ที่จำเป็น
RUN pip install django

RUN python manage.py makemigrations

RUN python manage.py migrate

RUN python manage.py runserver

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]