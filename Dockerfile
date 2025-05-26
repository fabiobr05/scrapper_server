FROM python:3.11-slim

ARG TARGETARCH

RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    wget \
    libglib2.0-0 \
    libnss3 \
    libx11-6 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxi6 \
    libxtst6 \
    libxrandr2 \
    libasound2 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    libdrm2 \
    libgbm1 \
    libxshmfence1 \
    --no-install-recommends

# Instala o Chromium + Chromedriver para ARM e x86
RUN if [ "$TARGETARCH" = "arm64" ] || [ "$TARGETARCH" = "arm/v7" ]; then \
    apt-get update && apt-get install -y chromium chromium-driver; \
else \
    apt-get update && apt-get install -y chromium chromium-driver; \
fi

# Dá permissão no chromedriver
RUN chmod +x $(which chromedriver)

# Verifica versões para debug
RUN chromium --version
RUN chromedriver --version

ENV BROWSER_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
