# WZCalc

## About

Простой калькулятор для предварительного расчета цены товара на маркетплейсах Ozon и Wildberries.

Стек:

fastapi
sqlalchemy
alembic
postgres

## Table of Contents

- [Project structure](#Project-structure)
- [Endpoints](#endpoints)
  - [Calculations](#Calculations)
    - [Ozon](#Ozon)
    - [Wildberries](#Wildberries)
  - [Users](#Users)
- [Constraints](#Constrains)

______________________________________________________________________

## Project structure

```
wzcalc 

```

______________________________________________________________________

## Endpoints

### Calculations

#### Ozon

| Метод | URL | Описание |
|-----------------------------------------|-------------------------------------------------|--------------------------------------------|
| POST | /api/v1/ozon/prices/fbs/calculate | Расчет цены для FBS-логистики |
| POST | /api/v1/ozon/prices/fbo/calculate | Расчет цены для FBO-логистики |
| POST | /api/v1/ozon/prices/fbs/bulk/calculate/ | Массовый расчет цен для FBS-логистики |
| POST | /api/v1/ozon/prices/fbo/bulk/calculate/ | Массовый расчет цен для FBO-логистики |
| POST | /api/v1/ozon/logistics/fbs/calculate | Расчет стоимости FBS-логистики |
| POST | /api/v1/ozon/logistics/fbo/calculate | Расчет стоимости FBO-логистики |
| POST | /api/v1/ozon/returns/fbs/calculate | Расчет стоимости возвратов для FBS-логистики |
| POST | /api/v1/ozon/returns/fbo/calculate | Расчет стоимости возвратов для FBO-логистики |

#### Wildberries

| Метод | URL | Описание |
|-----------------------------------------|---------------------------------------------|-----------------------------------|
| POST | /api/v1/wb/prices/calculate | Расчет цены |
| POST | /api/v1/wb/prices/bulk/calculate/ | Массовый расчет цен |
| POST | /api/v1/wb/logistics/calculate | Расчет стоимости логистики |
| POST | /wb/returns/calculate | Расчет стоимости возвратов |

### Users

______________________________________________________________________

## Constraints

Ограничения для валидации входящих данных.

**Общие**

1. Все процентные значения (decimal)\
   *e.g. comission_percent*\
   gt=0, le=100, max_digits=4, decimal_places=1\
   Больше 0, меньше или равно 100, не более 1 знака после запятой.\
   1-100.0

1. Всё, что касается стоимости логистики (decimal)\
   *e.g minimal_price_fbs*\
   gt=0, le=99999, max_digits=6, decimal_places=1\
   Больше 0, меньше или равно 99999, не более 1 знака после запятой\
   1-99999.9

1. Всё, что касается иных цен (decimal)\
   *cost_per_one*\
   ge=0, max_digits=8, decimal_places=1\
   Больше или равно 0, не длинее 7 знаков целой части, не более 1 знака после занятой\
   0-9999999.9

**Уникальные**

1. Тип поставки (string)\
   *fbs_fbo_option*\
   Допустимые значения строго "fbs" или "fbo".

1. Размеры упаковки (string)\
   *box_size*\
   Допустимые значения проверяются регулярным выражением

1. Индекс локализации (decimal)\
   *local_index*\
   gt=0, le=10, max_digits=4, decimal_places=1\
   Больше 0, меньше или равно 10, не более 1 знака после запятой\
   0-10.0

1. Количество товаров в упаковке (integer)\
   *count*\
   conint(ge=1, le=9999999)\
   Больше или равно 1, меньше или равно 9999999\
   1-9999999
