FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /case-repository
COPY requirements.txt /case-repository/
RUN pip install -r requirements.txt
COPY . /case-repository/