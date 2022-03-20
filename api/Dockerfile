# pull official base image
FROM python:3.10.3

# set work directory
WORKDIR /var/www/osf-etl-api

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV HOST 0.0.0.0
ENV PORT 8000

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r ./requirements.txt

# copy project
COPY . .

# run development server
CMD uvicorn src.server:app --host $HOST --port $PORT --reload