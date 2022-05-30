FROM python:3.10
RUN mkdir /pytest_container/
ADD . /pytest_container
WORKDIR /pytest_container/
RUN python -m pip install --upgrade pip
RUN pip install -r ./requirements.txt
