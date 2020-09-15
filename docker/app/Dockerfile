FROM python:3.8.5

RUN apt -y update && apt -y install vim mariadb-client git && \
    git clone https://github.com/nemodija/customer-manager.git && \
    cd customer-manager && \
    pip install -r requirements.txt
