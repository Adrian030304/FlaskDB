FROM python:3.13

WORKDIR /FLASKWITHDB

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN flask db init
RUN flask db migrate
RUN flask db upgrade

CMD [ "python3" , "run.py" ]
