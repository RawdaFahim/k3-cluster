# Use the official Python image as a base
FROM python:3.8-slim


ENV DD_AGENT_HOST=datadog
ENV DD_TRACE_AGENT_PORT=8126
ENV DD_ENV=production
ENV DD_SERVICE=python-sample-app
ENV DD_VERSION=1.0.0
# Set the working directory
WORKDIR /app

# Install necessary packages
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask app to the container
COPY app.py .

# Expose the port on which the Flask app will run
EXPOSE 80


# Run the app
CMD ["ddtrace-run", "python", "-m", "notes_app.app"]