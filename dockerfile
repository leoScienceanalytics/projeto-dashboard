# Use uma imagem base com Python
FROM python:3.11.9-slim

# Defina o diretório de trabalho dentro do contêiner
WORKDIR C:\Users\leona\Documents\novoprojetopythondashboards\app

# Copie o arquivo de requisitos para o diretório de trabalho
COPY app/requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie todos os arquivos para o diretório de trabalho
COPY . .

# Defina o comando padrão para executar a aplicação
CMD ["python", "codigo_fonte.py"]