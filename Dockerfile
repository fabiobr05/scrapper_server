# Use uma imagem slim do Python
FROM python:3.11-slim

# Instalar as dependências necessárias
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    libglib2.0-0 libnss3 libx11-6 libxcomposite1 libxcursor1 \
    libxdamage1 libxi6 libxtst6 libxrandr2 libasound2 libatk1.0-0 \
    libatk-bridge2.0-0 libgtk-3-0 libdrm2 libgbm1 libxshmfence1 \
    curl unzip wget --no-install-recommends && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Defina o caminho do binário do Chromium (para ARM)
ENV CHROME_BIN=/usr/bin/chromium

# Defina o caminho do chromedriver (para ARM)
ENV CHROMEDRIVER_PATH=/usr/lib/chromium-driver/chromedriver

# Copie o código da aplicação para o container
WORKDIR /app
COPY . /app

# Instale as dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Comando para rodar a aplicação
CMD ["python", "app.py"]
