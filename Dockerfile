FROM python:3.7-buster

ARG pip_username
ARG pip_password

WORKDIR /usr/src/app

ENV TZ=America/Toronto
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/timezone && \
    apt-get update && \
    apt-get install -y vim-tiny less && \
    ln -s /usr/bin/vim.tiny /usr/bin/vim && \
    rm -rf /var/lib/apt/lists/*
COPY requirements.txt ./
COPY internal_requirements.txt ./
pip install --no-cache-dir -r requirements.txt -r internal_requirements.txt
COPY . .
RUN chmod +x gunicorn_starter.sh

CMD ["./gunicorn_starter.sh"]