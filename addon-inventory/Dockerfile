ARG BUILD_FROM
FROM $BUILD_FROM

ENV PYTHONUNBUFFERED=1

RUN pip install --no-cache-dir flask jinja2 werkzeug click itsdangerous

COPY app /app
WORKDIR /app

EXPOSE 8099

CMD ["python3", "-u", "app.py"]
