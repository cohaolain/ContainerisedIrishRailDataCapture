FROM python:3

WORKDIR /usr/src/app

RUN apt update && apt install -y \
    default-libmysqlclient-dev \
    postgresql-server-dev-all \
    # openssl and ca-certificates are to here to fix SSL
    # issues in newer Python versions (https://tiny.cc/4e0hfz)
    openssl \
    ca-certificates

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY logger.py ./

CMD [ "python", "./logger.py" ]
