# django.dockerfile

FROM python:3.12

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y gettext

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN adduser --disabled-password --gecos '' nonrootuser

USER nonrootuser

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
