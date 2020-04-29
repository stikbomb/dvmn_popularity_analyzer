# Анализ упоминания фразы ВКонтакте

Скрипт для получения частоты и построения графика упоминания ключевых слов за указанное количество интервалов времени в постах ВКонтакте.

## Запуск

- Скачайте код
- Установите зависимости командой `pip install -r requirements.txt`
- Создайте приложение ВКонтакте (в качестве типа приложения необходимо указать 'standalone')
- Добавьте переменные окружения (см. пункт "Переменные окружения")
- Запустите скрипт командой `python3 main.py`

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `main.py` и запишите туда данные в формате: `ПЕРЕМЕННАЯ=значение`.
 
- `VK_ACCESS_TOKEN` — личный ключ пользователя, [подробная информация](https://vk.com/dev/implicit_flow_user)
- `VK_API_VERSION` — версия API, [подробная информация](https://vk.com/dev/versions)

Информация по вызовам API ВКонтакте доступна по [ссылке](https://vk.com/dev/api_requests).

## Использование скрипта

При вызове скрипта без параметров поиск ведётся для списка фраз ['Шаурма', 'Шаверма', 'Купат'] за последние 7 дней.

Пример выхова скрипта с параметрами:
```
python3 main.py pepsi fanta sprite -i month -n 12 
```

Запросы для поиска вводятся без ключа.

Ключ `-i` - тип интервала для поиска. Доступные значения - `day, week, month`.

Ключ `-n` - количество интервалов для поиска. Доступны значения в диапазоне от 1 до 12.



## Проблемы и ошибки

Ошибки со стороны API ВКонтакте, которые могут возникнуть во время выполнения скриптов, оформлены в соответствующие исключения - следите за выводом консоли во время выполнения скрипта.

Следует учитывать, что API ВКонтакте имеет ограничения на количество запросов.

## ToDo

- форматирование графика
- расчёт календарных интервалов
- ограничение на количество ключевых слов  


## Цель проекта

Код написан на основе учебного задания на портале [dvmn.org](https://dvmn.org/).