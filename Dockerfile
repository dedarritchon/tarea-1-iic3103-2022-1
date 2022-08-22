FROM python:3.10.2-slim-buster

WORKDIR /home/app
COPY requirements.txt ./
COPY . ./

RUN apt update
RUN apt install -y gcc
RUN pip install --no-cache-dir -r requirements.txt
RUN apt remove --purge -y gcc

EXPOSE 8000

CMD ["/bin/sh", "./docker/entrypoint.sh"]