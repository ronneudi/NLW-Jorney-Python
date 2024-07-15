FROM python:3.12-alpine
LABEL authors="ronne_souza"
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80
ENTRYPOINT ["sh","-c","python run.py"]