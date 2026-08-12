# Stage 1: Build environment
FROM python:3.10-slim AS builder

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . .

# (Optional) If you have a setup script or requirements.txt, install them here:
# RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Runtime environment
FROM python:3.10-slim

WORKDIR /app

# Copy necessary files from builder
COPY --from=builder /app /app

# Set default command with placeholder arguments (update path/format as needed)
CMD ["python3", "-m", "src.main", "path/to/source.file", "apk"]
