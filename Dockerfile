FROM python:3.11

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /app
WORKDIR /app
COPY requirements.txt requirements.txt
COPY requirements.dev.txt requirements.dev.txt

ARG DEV=false
RUN apt-get update && \
    apt-get install -y git && \
    git init && \
    apt-get install -y vim && \
    apt-get install -y gcc python3-dev && \
    apt-get install -y libpq-dev gcc && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt &&\
    if [ !$DEV ]; \
        then pip install -r requirements.dev.txt ; \
    fi && rm -rf /temp



COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0:8000"]
