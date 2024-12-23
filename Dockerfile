FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN apt-get update

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    && apt-get clean

RUN pip install -r requirements.txt

COPY . /app
CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--reload"]