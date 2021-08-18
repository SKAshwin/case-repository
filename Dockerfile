FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /app/
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get -y install graphviz graphviz-dev
RUN mkdir /app/static
RUN pip install -r requirements.txt
COPY . /app/