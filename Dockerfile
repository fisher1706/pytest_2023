# Указываем с какого имеджа нужно собрать контейнер, наш гарнир
FROM python:3.10-alpine

# Переменные окружения. Помните, что ARG доступен только когда мы собираем наш контейнер
# когда мы будем его запускать, то доступ к этой переменной получить уже не сможем.
ARG run_env=production
ENV env $run_env

# С помощью этих штук, вы можете оставить какую-то информацию о себе
LABEL "channel"="SolveMe"
LABEL "creator"="SolveMe community"

# Этой командой обновляем наш базовый образ и устанвавливаем chromedriver
RUN apk update && apk upgrade && apk add bash
RUN apk add --no-cache chromium chromium-chromedriver tzdata

# Устанавливаем "окружение"
RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub
RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.30-r0/glibc-2.30-r0.apk
RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.30-r0/glibc-bin-2.30-r0.apk

RUN apk update && \
    apk add openjdk11-jre curl tar && \
    curl -o allure-2.13.8.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.8/allure-commandline-2.13.8.tgz && \
    tar -zxvf allure-2.13.8.tgz -C /opt/ && \
    ln -s /opt/allure-2.13.8/bin/allure /usr/bin/allure && \
    rm allure-2.13.8.tgz

# Указываем директорию в которой мы будем работать внутри докера
WORKDIR ./usr/lessons

# Создаём вольюм, для того чтобы иметь возможность получить данные после того, как контейнер закончит свою работу
VOLUME /allure-results

# Копируем отдельно наш файл с зависимостями
COPY requirements.txt .

# Инстайлим наши зависимости внутри контейнера
RUN pip install --no-cache-dir --verbose -r requirements.txt

# Копируем наши файлики внутрь контейнера
COPY . .

# Ну и наконец-то запускаем наши тесты
#CMD pytest -m "$env" -s -v tests_lifecoding/* --alluredir=allureResults
#CMD pytest -s -v tests/* --alluredir=allure-results

