FROM python:3.7-alpine

# Install system dependencies
RUN apk update && \
    apk add --no-cache \
    bash gcc python3-dev musl-dev postgresql-dev

# Create work directory
WORKDIR /app

# Copy requirements and install
ADD ./requirements-dev.txt ./requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements-dev.txt

# Add source
ADD . /app/

EXPOSE 8000

CMD ["/app/entrypoint.sh"]
