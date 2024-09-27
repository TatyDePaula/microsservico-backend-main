# Use uma imagem base do Python
FROM python:3.9-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt ./

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o conteúdo da pasta atual para o diretório de trabalho
COPY . .

# Define a variável de ambiente FLASK_APP
ENV FLASK_APP=main.py

# Expõe a porta que o Flask usa (padrão 5000)
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["flask", "run", "--host=0.0.0.0"]

