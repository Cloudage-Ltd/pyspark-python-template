ARG IMAGE_VARIANT=slim-buster
ARG OPENJDK_VERSION=8


# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8.12
# FROM openjdk:${OPENJDK_VERSION}-${IMAGE_VARIANT}


RUN apt-get update
RUN apt-get install default-jdk -y


# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser


# # Allow for a consistant java home location for settings - image is changing over time
# RUN if [ ! -d "/docker-java-home" ]; then ln -s "${JAVA_HOME}" /docker-java-home; fi

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python", "src/main.py"]