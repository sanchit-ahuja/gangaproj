FROM python:3.7-slim

WORKDIR /gangaproj

COPY . /gangaproj

RUN apt-get update
RUN apt-get install -y python python-dev python-pip build-essential swig git libpulse-dev

RUN pip install --trusted-host pypi.python.org -r requirements.txt

ENV NAME gangavenv

CMD ["ganga", "T3.py"]


