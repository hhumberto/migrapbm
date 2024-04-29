FROM python:3.10.9
LABEL maintainer="humberto@bitegra.mx"

WORKDIR /azpipeline

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8088

CMD ["python", "manage.py", "runserver", "0.0.0.0:8088"]