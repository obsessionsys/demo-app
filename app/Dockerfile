FROM python:2-stretch

RUN mkdir -p /app

ADD ./ /app

WORKDIR /app

RUN pip install prometheus-client \
    && apt install -y iputils-ping

HEALTHCHECK --interval=5s --timeout=3s CMD curl --fail http://localhost:8080 || exit 1

EXPOSE 8080 8000

CMD [ "python", "app.py" ]