FROM python:3.8.10-alpine as base
LABEL maintainer="fredrik@scaleoutsystems.com"
WORKDIR /app
COPY requirements.txt .
RUN apk add --update --no-cache \
    build-base \
    python3-dev \
    py3-setuptools \
    && pip install --no-cache-dir -r requirements.txt \
    && pip install -e git+https://github.com/scaleoutsystems/fedn.git@develop#egg=fedn\&subdirectory=fedn


FROM python:3.8.10-alpine as build
COPY --from=base /usr/local/lib/python3.8/site-packages/ /usr/local/lib/python3.8/site-packages/
