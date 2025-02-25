# Use an official Python base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the setup.py and other necessary files
COPY setup.py ./
COPY . .

# Install dependencies using setup.py
RUN pip install --upgrade pip && \
    pip install .

# Define the command to run your application (Modify this as needed)
CMD ["python","-u","scheduler.py"]
