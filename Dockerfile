FROM python:3

WORKDIR /usr/src/app

RUN apt update && apt install -y default-libmysqlclient-dev postgresql-server-dev-all

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY logger.py ./

CMD [ "python", "./logger.py" ]
