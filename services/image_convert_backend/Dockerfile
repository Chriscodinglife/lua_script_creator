# syntax=docker/dockerfile:1

FROM python:3.10.1

WORKDIR /app

COPY requirements.txt requirements.txt
COPY imageconvert.py imageconvert.py
COPY image_converter.py image_converter.py

RUN pip3 install -r requirements.txt

CMD ["uvicorn", "imageconvert:app", "--host", "0.0.0.0", "--port", "8080"]