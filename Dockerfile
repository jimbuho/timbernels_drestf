FROM python:3

WORKDIR /code

COPY requirements/requirements.txt /code/

RUN pip3 install virtualenv

RUN virtualenv -p python ve_env

RUN source ve_env/bin/activate

RUN pip3 install -r requirements.txt

COPY . /code/