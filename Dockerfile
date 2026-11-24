FROM python:3.14-slim

WORKDIR /app

COPY Day37.py .

CMD ["python", "Day37.py"]