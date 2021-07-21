FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /app/
RUN mkdir /app/static
RUN pip install -r requirements.txt
COPY . /app/