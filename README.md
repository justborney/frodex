Тестовое задание

Идея: Асинхронный счётчик лайков.
Задача: Разработать веб-приложение с использованием указанных технологий

Тех стек бэка: python, falcon, nginx (в качестве reverse proxy), postgresql, redis + celery (celery в качестве обработчика очереди), docker, docker-compose
Тех стек фронта: react, остальное на выбор. Дизайн простой

Описание задачи: Пользователь с браузера заходит на веб-страницу, кликает на кнопку лайка. Счетчик лайков увеличивается на +1 локально. После посылается запрос на бэк на увеличение счетчика. Бэк принимает его, создает задачу в очередь на увеличение счетчика и сразу отвечает 200 OK (если ошибка, то на фронте счетчик -1). На бэке же обработчик очереди забирает задачу и увеличивает счетчик в бд. На фронте каждые 5 сек летят запросы на бэк, чтобы получить текущее значение лайков из бд (синхронизация)

Дистрибуция: через Docker образ. Можно просто Dockerfile, чтобы локально можно было собрать и запустить. В docker-compose.yml описать все сервисы (postgresql, redis, backend, nginx и тд)