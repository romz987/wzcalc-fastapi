# WZCalc

## About

Простой калькулятор для предварительного расчета цены товаров для маркетплейсов Ozon и Wildberries.

Стек:

fastapi
sqlalchemy
alembic
postgres

## Table of Contents

- [Project structure](#Project-structure)
- [Calculator package](#Calculator)
  - [Service package structure](#Service-package-structure)
  - [Description](#Description)
- [How is this calculated?](#How-is-this-calculated?)
  - [Ozon](#Ozon-calculations)
    - [Logistics FBS](<>)
    - [Logistics FBO](<>)
    - [Returns](<>)
    - [Profit](<>)
    - [Price](<>)
  - [Wildberries](#Wildberries-calculations)
    - [Logistics FBS](<>)
    - [Logistics FBO](<>)
    - [Returns](<>)
    - [Profit](<>)
    - [Price](<>)
- [Endpoints](#endpoints)
  - [Calculations](#Calculations)
    - [Ozon endpoints](#Ozon-endpoints)
    - [Wildberries endpoints](#Wildberries-endpoints)
  - [Users](#Users)
- [Variables](#Variables)
  - [Ozon variables](#Ozon-variables)
  - [Wildberries variables](#Wildberries-variables)
- [Constraints](#Constrains)
- [References](#References)

______________________________________________________________________

## Project structure

**feature based organisation**

```
wzcalc 

```

______________________________________________________________________

## Calculator package

### Service package structure

```

```

### Description

______________________________________________________________________

## How is this calculated?

### Ozon

#### Logistics FBS

#### Logistics FBO

#### Returns

#### Profit

#### Price

### Wildberries

#### Logistics FBS

#### Logistics FBO

#### Returns

#### Profit

#### Price

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

## Variables

### Ozon

**input**

tax_system: Система налогооблажения str ['simple', 'difference']

profit_percent: Желаемый профит - в процентах от себестоимость\
comission_percent: Процент комиссии маркетплейса\
acquiring_percent: Процент эквайринга\
tax_percent: Процент налога\
risk_percent: Процент рисков\
redemption_percentage: Процент выкупа\
last_mile_percent: Процент последняя миля

shipment_processing: Стоимость обработки отправления\
count: Количество товаров в комплекте\
cost_per_one: Стоимость единицы товара\
wage_cost: Стоимость труда\
box_cost: Стоимость упаковки

box_size: Размеры упаковки\
local_index: Индекс локализации\
nonredemption_processing_cost: Стоимость обработки одного возврата

minimal_price_fbs: Стоимость логистики FBS для упаковки объемом менее 0.4 литра\
base_price_fbs: Базовая стоимость логистики FBS\
volume_factor_fbs: Стоимость логистики FBS за каждый дополнительный литр для упавки объемом более 1 литра\
fix_large_fbs: Стоимость логистики FBS для упаковки объемом более 190 литров

base_price_fbo: Базовая стоимость логистики FBO\
volume_factor_fbo: Стоимость логистики FBO за каждый дополнительный литр для упавки объемом более 1 литра\
fix_large_fbo: Стоимость логистики FBO для упаковки объемом более 190 литров

**output**

### Wildberries

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
   *e.g. minimal_price_fbs*\
   gt=0, le=99999, max_digits=6, decimal_places=1\
   Больше 0, меньше или равно 99999, не более 1 знака после запятой\
   1-99999.9

1. Всё, что касается иных цен (decimal)\
   *e.g. cost_per_one*\
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

______________________________________________________________________

## References

[fast api best practices](https://github.com/zhanymkanov/fastapi-best-practices?tab=readme-ov-file#async-routes)
