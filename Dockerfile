# Stage 1: Build environment
FROM python:3.10-slim AS builder

WORKDIR /app

# Install system dependencies, compilers, and build tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . .

# Run your build script or setup process if needed
RUN python3 -m src.main


# Stage 2: Runtime environment
FROM python:3.10-slim

WORKDIR /app

# Copy only necessary build artifacts and dependencies
COPY --from=builder /app /app

# Set default command to run your application
CMD ["python3", "-m", "src.main"]
