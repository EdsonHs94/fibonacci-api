FROM amazonlinux:2017.09

RUN yum -y update && yum -y install \
    nginx \
    python35 \
    python35-devel \
    git \
    gcc \
    python35-pip

RUN python35 --version
ADD app /app

WORKDIR /app

RUN pip-3.5 install -r requeriments.txt
EXPOSE 8000
CMD gunicorn wsgi:api