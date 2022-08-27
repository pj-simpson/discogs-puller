# https://luis-sena.medium.com/creating-the-perfect-python-dockerfile-51bdec41f1c8
FROM ubuntu:20.04 AS builder-image

# avoid stuck build due to user prompt
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install --no-install-recommends -y python3.9 python3.9-dev python3.9-venv python3-pip python3-wheel build-essential && \
	apt-get clean && rm -rf /var/lib/apt/lists/*

RUN python3.9 -m venv /home/myuser/venv
ENV PATH="/home/myuser/venv/bin:$PATH"

COPY ../../requirements.txt .
#need to upgrade to the latest pip for RUST stuff (pydantic uses it)
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir wheel
RUN pip3 install --no-cache-dir -r requirements.txt

FROM ubuntu:20.04 AS runner-image
RUN apt-get update && apt-get install --no-install-recommends -y sqlite3 python3.9 python3-venv && \
	apt-get clean && rm -rf /var/lib/apt/lists/* && \
	apt-get install procps


RUN useradd --create-home myuser
COPY --from=builder-image /home/myuser/venv /home/myuser/venv

RUN mkdir /home/myuser/code
WORKDIR /home/myuser/code
COPY ../.. .

COPY ./docker/local/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

ENV PYTHONUNBUFFERED=1

ENV VIRTUAL_ENV=/home/myuser/venv
ENV PATH="/home/myuser/venv/bin:$PATH"