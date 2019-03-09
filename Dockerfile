FROM python:2.7-slim

WORKDIR /gangaproj

COPY . /gangaproj

RUN pip install --upgrade pip

RUN apt-get update
RUN apt-get install -y python python-dev python-pip build-essential swig git libpulse-dev
RUN apt-get install -y build-essential libpoppler-cpp-dev pkg-config python-dev

RUN pip install --trusted-host pypi.python.org -r requirements.txt

ENV NAME gangavenv

CMD ["ganga", "T3.py"]


