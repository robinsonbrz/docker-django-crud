FROM ubuntu:20.04

# Lang config

ENV LANG en_US.UTF-8

ENV LANGUAGE en_US:en

ENV LC_ALL en_US.UTF-8

ENV DEBIAN_FRONTEND noninteractive

# Add a non root user

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID



RUN groupadd --gid ${USER_GID} ${USERNAME} && \
	useradd --uid ${USER_UID} --gid ${USER_GID} -m ${USERNAME}

# Configure OS

RUN apt-get update && apt-get install -y \
	software-properties-common \
	git \
	python3-pip \
	python3.8-dev \
	python3-venv

# Change default python adn pip

RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1 \
	&& update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1

RUN mkdir -p /workspace
RUN chown -R $USERNAME:$USERNAME /workspace

COPY requirements.txt /workspace

WORKDIR /workspace

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

USER $USERNAME