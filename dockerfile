#Usando uma imagem base oficial
FROM python:3.11.9-slim

#Definindo diretório padrão de trabalho
WORKDIR C:\Users\leona\Documents\novoprojetopythondashboards\dockerfile

#Copiando conteúdo de Requerimentos
COPY requirements.txt .

#Instalando as dependências do python
RUN pip install --novoprojetopythondashboards -r requeriments.txt

#Copiando todo o conteúdo do diretório atual para o diretório de trabalho
COPY . .

#Definindo a variável do ambiente para evitar que o python crie arquivos .pyc
ENV ambienteprojeto 1

# Define a variável de ambiente para garantir que a saída do Python seja exibida na saída do console (log)
ENV PYTHONUNBUFFERED 1

#Definindo a porta que o dash usa
EXPOSE 8050

#Comando para rodar a aplicação
CMD ["python", "codigo_fonte.py"]