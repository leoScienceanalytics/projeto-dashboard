FROM python:3.11.9-slim
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
WORKDIR /app
CMD ["Python", "codigo_fonte.py"]