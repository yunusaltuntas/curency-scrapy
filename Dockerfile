FROM python:3.7

WORKDIR /

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install fake-useragent==0.0.8
RUN pip install lxml
RUN apt-get update