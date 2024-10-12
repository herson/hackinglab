FROM python:3.9-slim

# Ensure commands run as root
USER root

WORKDIR /app

COPY app.py .

RUN pip install flask

EXPOSE 5000

CMD ["python", "app.py"]
