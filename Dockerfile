# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script and other required files into the container
COPY iiif_server.py /app/iiif_server.py
COPY index.html /app/index.html
COPY info.json /app/info.json
COPY styles.css /app/styles.css

# Expose the port on which the server will run
EXPOSE 3000

# Command to run the Python script
CMD [ "python", "iiif_server.py" ]
