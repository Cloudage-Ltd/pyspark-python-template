FROM python:3.8.12

ARG PROFILE_NAME="dev"
ARG HOST_URL="UPDATE HOST_URL HERE"
ARG TOKEN="UPDATE TOKEN HERE"

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

RUN echo "[${PROFILE_NAME}]\nhost = ${HOST_URL}\ntoken = ${TOKEN}" >> ~/.databrickscfg

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python", "src/main.py"]