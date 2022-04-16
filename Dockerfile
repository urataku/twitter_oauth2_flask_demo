FROM python:3.10.4

WORKDIR /build
COPY . ./
RUN apt update && apt install -y zip
RUN pip install --upgrade pip
RUN pip install requests Flask