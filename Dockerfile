FROM python:3-slim-buster

LABEL maintainer="nedenis.ste@gmail.com"

WORKDIR /wallet_app

ENV PYTHONPATH=/wallet_app

RUN python3 -m venv venv

RUN /wallet_app/venv/bin/pip install --no-cache-dir pyarrow==13.0.0

COPY requirements.txt /wallet_app/requirements.txt

RUN /wallet_app/venv/bin/pip install --no-cache-dir -r /wallet_app/requirements.txt

COPY wallet /wallet_app/wallet

CMD python /wallet_app/wallet/manage.py runserver