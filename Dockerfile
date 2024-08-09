# Use uma imagem base do Python com suporte a build tools
FROM python:3.9-slim-buster

# Crie um diretório de trabalho
WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

# Expose a porta (ajuste conforme necessário)
EXPOSE 8521

# Defina o comando para executar a aplicação
ENTRYPOINT ["mesa", "runserver", "src/server.py"]
