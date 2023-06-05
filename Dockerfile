FROM python:3.10.6-slim as base
LABEL maintainer="salman@scaleoutsystems.com"
WORKDIR /app
COPY requirements.txt .
RUN apt-get update \ 
    && apt-get install --no-install-recommends -y git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \ 
    && pip install git+https://github.com/scaleoutsystems/fedn.git@master#egg=fedn\&subdirectory=fedn \
    && pip install --no-cache-dir -r requirements.txt


FROM python:3.10.6-slim as build
COPY --from=base /usr/local/lib/python3.10/site-packages/ /usr/local/lib/python3.10/site-packages/
COPY --from=base /usr/local/bin/fedn /usr/local/bin/
WORKDIR /app
