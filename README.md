# slaves-bot-vk

[Бот для мини-игры ВКонтакте "Рабы"](https://vk.com/app7794757)
[Тема на Lolzteam](https://lolz.guru/threads/2389937/)

## Какие настройки присутствуют?
[image](https://i.imgur.com/HEpnGkf.png)
- Anticooldown. Рандомизация времени на выдачу цепей, покупку рабов и выдачу названвания работы
- Job_name. Имя работы
- Min/Max_price. Минимальная и максимальная цена за которую покупать рабов
- Buy_slave, True/False. Покупка рабов
- Buy_fetter, True/False. Покупка оков

## Флуд в консоль ошибками
- Error when buying slave, possibly a cooldown. Возможно флуд-контроль на покупку рабов
- Error when installing the job, possibly cooldown. Возможно флуд-контроль на установку названия работы
- Error when buying fetter, possibly a cooldown. Возможно флуд-контроль на покупку оков
[image](https://i.imgur.com/E0GDfzN.png)

## Запуск скрипта на Windows:
- Скачать архив с репозитория
- Установить Python последней версии http://python.org
- Поставить галочку ADD TO PATH
- Установить модули pip install -r requirements.txt
- Запустить скрипт
- Ввести ключ:
[image](https://i.imgur.com/mZODDE7.png)

## Как получить ключ?
- Заходим в приложение ["Рабы"](https://vk.com/app7794757)
- Открываем консоль CTRL + SHIFT + I
- Переходим по вкладку NETWORK
- В графе filter пишем start
- Обновляем страницу
- Копируем все из поля authorization
[image](https://i.imgur.com/0WT8GH1.png)

## Планы на будущее
- Добавить рандомизацию при установке работ
