# Use an Alpine-based Python image as the base image
FROM python:alpine

# Install dependencies required to build psycopg2
RUN apk update && apk add --no-cache \
    postgresql-dev \
    gcc \
    python3-dev \
    musl-dev \
    libffi-dev

# Set the working directory inside the container
WORKDIR /home/app/src

# Copy the requirements file to the container
COPY requirements/requirements.txt /home/app/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r /home/app/requirements.txt

# Copy the entire application code to the container
COPY src /home/app/src
COPY alembic.ini /home/app/alembic.ini
COPY migration /home/app/migration

# Set the default command to run when the container starts
CMD ["sh", "-c", "alembic upgrade head && uvicorn main:app --host 0.0.0.0 --reload"]

