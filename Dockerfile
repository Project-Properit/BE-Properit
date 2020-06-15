FROM python:3-alpine
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN apk add --no-cache --virtual .build-deps gcc musl-dev libffi-dev openssl-dev python3-dev
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
ENTRYPOINT [ "gunicorn", "-w", "2", "-b", ":5000", "api:app" ]
