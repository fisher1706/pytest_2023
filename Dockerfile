# Указываем с какого имеджа нужно собрать контейнер, наш гарнир :)
FROM python:3.10-slim

# Переменные окружения. Помните, что ARG доступен только когда мы собираем наш контейнер
# когда мы будем его запускать, то доступ к этой переменной получить уже не сможем.
ARG run_env=development
ENV env $run_env

# С помощью этих штук, вы можете оставить какую-то информацию о себе
LABEL "channel"="SolveMe"
LABEL "creator"="SolveMe community"

# Указываем директорию в которой мы будем работать внутри докера
WORKDIR ./usr/lessons

# Создаём вольюм, для того чтобы иметь возможность получить данные после того, как контейнер закончит свою работу
VOLUME /allureResults

# Этой командой обновляем наш базовый образ
RUN apt update && apt install -y npm

# Копируем отдельно наш файл с зависимостями
COPY requirements.txt .

# Инстайлим наши зависимости внутри контейнера
RUN pip3 install --upgrade pip
RUN apt-get update && apt-get -y install libpq-dev gcc && pip install psycopg2
RUN pip3 install -r requirements.txt

# Копируем наши файлики внутрь контейнера
COPY . .

# Ну и наконец-то запускаем наши тесты
CMD pytest -m "$env" -s -v tests/* --alluredir=allureResults
