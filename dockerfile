FROM python:latest



ADD new.py .



RUN pip install elasticsearch sendgrid



RUN apt update




CMD ["python", "new.py"]