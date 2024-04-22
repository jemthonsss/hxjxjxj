#pylint:disable=E0001

FROM youthon:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "youthon1", "youthoon.py"]
