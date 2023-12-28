FROM python:3.9.18-slim-bullseye
WORKDIR /app
COPY app/ .
EXPOSE 80
ENTRYPOINT ["python", "server.py"]