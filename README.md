# Hello World in Docker

## Prerequisites

- docker
- docker-compose

### STEP 1. Clone this repo

```shell
git clone https://github.com/obsessionsys/demo-app.git
```

### STEP 2. Change permissions

```shell
cd demo_app
bash ./make_demo_app.sh
```

### STEP 3. Start docker containers

```shell
cd /demo_app
docker-compose up -d
```

* The Prometheus and Grafana stack will unfold
* This will start the Docker node-exporter on the same network (optional)
* Automatically build all necessary Docker containers

### STEP 4. Connect Grafana to datasource Prometheus

Connect web browser on Grafana


URL Grafana: **http://HOST_IP:3000**

Grafana Login: **admin**</br>

Grafana Pass: **pass**



URL Prometheus: **http://HOST_IP:9090**

URL Application: **http://HOST_IP:8080**

URL App Exporter: **http://HOST_IP:8000**

![Connect](image/connect.png)

## Шаг 5. Import dashboard

Upload `python_web_app-grafana.json`

![Import](image/import.png)

* No Prometheus security
* No SSL security for all URLS
* FQDN + SSL requests not implemented


---
Предварительные замечания:

На хост системе должны быть уже установлены:
 - docker
 - docker-compose
  
## Шаг 1. Выкачиваем сырцы

```shell
git clone https://github.com/obsessionsys/demo-app.git
```

## Шаг 2. Выставляем права на директорию

```shell
cd demo_app
bash ./make_demo_app.sh
```

## Шаг 3. Поднимаем докер контейнеры 
* Будет поднят стек Prometheus + Grafana
* Будет поднят в той же сети контейнер node-exporter (опционально поднимается для демо)
* В автоматическом режиме будет произведен сборка Docker контейнера приложения


Для разворачивания необходимо произвести:

```shell
cd /demo_app
docker-compose up -d
```

## Шаг 4. Подключаем Grafana к datasource Prometheus
URL Grafana: **http://HOST_IP:3000**

Grafana Login: **admin**</br>
Grafana Pass: **pass**



URL Prometheus: **http://HOST_IP:9090**

URL Application: **http://HOST_IP:8080**

URL App Exporter: **http://HOST_IP:8000**

![Connect](image/connect.png)

## Шаг 5. Импортируем дашбоард

![Import](image/import.png)

## ВАЖНО !!!
* Нет безопасности Prometheus
* Нет защищенности на уровне SSL всех URL-ов
* Не реализовано запросы по FQDN + SSL