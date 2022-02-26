FROM python:latest
LABEL maintainer="Danwand NS | DanBrown47"

# Workdir
WORKDIR /app

# Install Dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy files
COPY . .

# Execute script
CMD ["python", "scrapper.py"]
