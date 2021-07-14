FROM ubuntu:20.04
LABEL maintainer="Karlos Helton Braga <Konkah>"

RUN apt update
RUN apt upgrade -y
RUN apt autoremove -y
RUN apt autoclean -y

RUN apt install -y curl
RUN apt install -y nano
RUN apt install -y unzip
RUN apt install -y net-tools
RUN apt install -y telnet

RUN apt install -y python3.8 
RUN apt install python3-pip -y
RUN apt install python3-dev -y 
RUN apt install libmysqlclient-dev -y

COPY . /var/www

RUN python3 -m pip install -U pip
RUN python3 -m pip install -U setuptools
RUN python3 -m pip install -U wheel

WORKDIR /var/www/api_clientes
RUN python3 -m pip install -r requirements.txt

#CMD bash
CMD python3 manage.py runserver