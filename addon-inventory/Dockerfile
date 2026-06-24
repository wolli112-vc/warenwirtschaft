ARG BUILD_FROM
FROM $BUILD_FROM

ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache py3-pip py3-flask py3-jinja2 py3-werkzeug py3-click py3-itsdangerous

COPY app /app
WORKDIR /app

EXPOSE 8099

CMD ["python3", "-u", "app.py"]
