FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y libgl1-mesa-glx

COPY requirements.txt /app

# Install Django
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Expose a port (e.g., 8000) that your application will run on
EXPOSE 8000
CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate --noinput && python manage.py runserver 0.0.0.0:8000"]
