FROM python:3.12-slim
WORKDIR /app

ARG APP_ENV
ARG DB_PASSWORD

ENV APP_ENV=$APP_ENV
ENV DB_PASSWORD=$DB_PASSWORD

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV APP_ENV=production

CMD ["python", "app/app.py"]
