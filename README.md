![wzcalc-header](/images/wzcalc.jpg)

# WZCalc

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)

Простой калькулятор для предварительного расчета цены товаров для маркетплейсов Ozon и Wildberries.

<br>
<br>

## Table of Contents

- [Summary](#Summary)
- [How is this calculated?](#How-is-this-calculated?)
  - [Ozon](#Ozon-calculations)
    - [Logistics fee FBS Ozon](#logistics-fee-fbs-ozon)
    - [Logistics fee FBO Ozon](#logistics-fee-fbo-ozon)
    - [Reverse logistics fee Ozon](#reverse-logistics-fee-ozon)
    - [Returns fee Ozon](#returns-fee-ozon)
    - [Profit fee Ozon](#profit-fee-ozon)
    - [Price fee Ozon](#price-fee-ozon)
  - [Wildberries](#Wildberries-calculations)
    - [Logistics fee FBS wildberries](#logistics-fee-fbs-wildberries)
    - [Logistics fee FBO wildberries](#logistics-fee-fbo-wildberries)
    - [Returns fee Wildberries](<>)
    - [Profit fee Wildberries](<>)
    - [Price fee Wildberries](<>)
- [Project structure](#Project-structure)
- [Calculator core package](#Calculator-core-package)
  - [Core package structure](#Core-package-structure)
  - [Description](#Description)
    - [Interfaces](#intefaces)
    - [Services](#services)
    - [Calculators](#calculators)
    - [Domain](#domain)
- [Endpoints](#endpoints)
  - [Calculations](#Calculations)
    - [Ozon endpoints](#Ozon-endpoints)
    - [Wildberries endpoints](#Wildberries-endpoints)
- [Constraints](#Constrains)
- [Variables](#Variables)
  - [Ozon variables](#Ozon-variables)
  - [Wildberries variables](#Wildberries-variables)
- [References](#References)

<br>
<br>

## Summary

Краткое содержание документации


1. How is this caclulated?  
    В этом разделе подробно описано как именно происходит расчет составляющих цены и итоговой цены

2. Project structure  
    В этом разделе подробно описана структура проекта

3. Calculator core package  
    В этом разделе подробно описаны структура и особенности ядра калькулятора

4. Endpoints  
    В этом разделе описано какие существуют endpoints и как именно к ним обращаться

5. Constraints  
    В этом разделе описаны существующие pydantic-правила для входящих данных

6. Variables  
    В этом разделе приведен список используемых переменных с описанием

7. References  
    Ссылки на источники, использованные для написания приложения и создания документации


<br>
<br>

______________________________________________________________________

## How is this calculated?

![wzcalc-ozon-calculations](/images/ozon-calculations.jpg)

### Ozon

#### Logistics fee FBS Ozon

Как расчитывается стомость для логистики FBS.

- Переменные и обозначения:

| Обозначение | Параметр | Описание |
|-------------|----------------------|--------------------------------------------------------------------------|
| $V$ | `box_volume` | Объём упаковки в литрах |
| $I$ | `local_index` | Индекс локализации |
| $C\_{\\text{lg}}$ | `fix_large_fbs` | Стоимость логистики за объём $> 190$ литров |
| $C\_{\\text{min}}$ | `minimal_price_fbs` | Стоимость логистики за объём $\\leq 0.4$ литров |
| $C\_{\\text{base}}$ | `base_price_fbs` | Базовая стоимость логистики за объём $0.4 < V \\leq 190$ литров |
| $C\_{\\text{vol}}$ | `volume_factor_fbs` | Стоимость логистики за каждый дополнительный литр |
| $L$ | `logistics_fee` | Итоговая стоимость логистики |

- Идея расчета:

  Если объем упаковки не превышает 0.4 литра, то стоимость логистики рассчитывается как произведение minimal_price_fbs и local_index:\
  $L = C\_{\\text{min}} \\cdot I$

  Если объем упаковки от 0.4 литров до 1 литра включительно, то стоимость логистики рассчитывается как произведение base_price_fbs и local_index:\
  $L = C\_{\\text{base}} \\cdot I$

  Если объем упаковки от 1 литра до 190 литров включительно, стоимость логистики расчитвается как произведение local_index и base_price_fbo + volume_factor за каждый дополнительный литр:\
  $\\bigl(C\_{\\text{base}} + C\_{\\text{vol}} \\cdot \\lceil V - 1 \\rceil \\bigr) \\cdot I$

  Если объем превышает 190 литров, то:\
  $L = C\_{lg} \\cdot I$

- Формула:

$V\_{\\text{max}}$ = 190\
$V\_{\\text{min}}$ = 0.4\
$V\_{\\text{avg}}$ = 1

$$
L(V) =
\\begin{cases}
C\_{\\text{lg}} \\cdot I & V \\gt V\_{\\max} \\\\[6pt]
C\_{\\min} \\cdot I & 0 \\lt V \\leq V\_{\\min} \\\\[6pt]
C\_{\\text{base}} \\cdot I & V\_{\\min} < V \\leq V\_{\\text{avg}} \\\\[6pt]
\\bigl(C\_{\\text{base}} + C\_{\\text{vol}} \\cdot \\lceil V - 1 \\rceil \\bigr) \\cdot I & V\_{\\text{avg}} < V \\leq V\_{\\max}
\\end{cases}
$$

#### Logistics fee FBO Ozon

Как расчитывается стомость для логистики FBO.

- Переменные и обозначения:

| Обозначение | Параметр | Описание |
|-------------|----------------------|--------------------------------------------------------------------------|
| $V$ | `box_volume` | Объём упаковки в литрах |
| $I$ | `local_index` | Индекс локализации |
| $C\_{\\text{lg}}$ | `fix_large_fbo` | Стоимость логистики за объём $> 190$ литров |
| $C\_{\\text{base}}$ | `base_price_fbo` | Базовая стоимость логистики за объём $0 < V \\leq 190$ литров |
| $C\_{\\text{vol}}$ | `volume_factor_fbo` | Стоимость логистики за каждый дополнительный литр |
| $L$ | `logistics_fee` | Итоговая стоимость логистики |

- Идея расчета:

  Если объем упаковки до 1 литра включительно, то стоимость логистики рассчитывается как произведение base_price_fbs и local_index:\
  $L = C\_{\\text{base}} \\cdot I$

  Если объем упаковки от 1 литра до 190 литров включительно, стоимость логистики расчитвается как произведение local_index и base_price_fbo + volume_factor за каждый дополнительный литр:\
  $\\bigl(C\_{\\text{base}} + C\_{\\text{vol}} \\cdot \\lceil V - 1 \\rceil \\bigr) \\cdot I$

  Если объем превышает 190 литров, то:\
  $L = C\_{lg} \\cdot I$

- Формула:

$V\_{\\text{max}}$ = 190\
$V\_{\\text{avg}}$ = 1

$$
L(V) =
\\begin{cases}
C\_{\\text{lg}} \\cdot I & V \\gt V\_{\\max} \\\\[6pt]
C\_{\\text{base}} \\cdot I & V \\leq V\_{\\text{avg}} \\\\[6pt]
\\bigl(C\_{\\text{base}} + C\_{\\text{vol}} \\cdot \\lceil V - 1 \\rceil \\bigr) \\cdot I & V\_{\\text{avg}} < V \\leq V\_{\\max}
\\end{cases}
$$

#### Reverse logistics fee Ozon

Как расчитывается стоимость обратной логистики.

Стоимость обратной логистики расчитывается так же, как и логистика FBS, только local_index (индекс локализации) всегда равен 1.

#### Returns fee Ozon

Как расчитывается стоимость невыкупов.

- Переменные и обозначения:


| Обозначение | Параметр | Описание |
|-----------|--------|--------|
| $r$ | `redemption_percentage` | Процент выкупа |
| $L$ | `logistics_fee` | Стоимость логистики для одного товара |
| $R$ | `reverse_logistics_fee` | Стоимость обратной логистики для одного невыкупленного товара |
| $P$ | `nonredemption_processing_cost` | Стоимость обработки одного возврата |
| $F$ | `returns_fee` | Стоимость возвратов при текущем $r$ (redemption_percentage) |


- Идея расчета:

  Берем базовую выборку в 100 отправленных заказов.\
  Все 100 заказов будут доставлены до ПВЗ покупателя, поэтому логистика оплачивается за все 100 отправлений: $100L$.\
  Часть заказов будет возвращена отправителю - за них должна быть оплачена стоимость обратной логистики: $R(100 - r)$.\
  Так же должна быть оплачена стоимость обработки возвратов: $P(100 - r)$.\
  Суммарные затраты распределяются только на выкупленные заказы ($r$).\
  После чего из получившегося значения вычитается $L$, иначе она будет учитана 2 раза.

- Формула:

  $F = \\frac{100L + (100-r)(R+P)}{r} - L$

- Формула (упрощенная):\
  *Расчет происходит по этой формуле*

  $F = \\frac{100-r}{r}(L + R + P)$

#### Profit fee Ozon

#### Price fee Ozon

<br>
<br>

![wzcalc-wildberries-calculations](/images/wildberries-calculations.jpg)

### Wildberries

#### Logistics fee FBS wildberries

Как расчитывается стомость для логистики FBS.

Стоимость логистики для FBS расчитывается так же как и стоимость логистики для FBO, но индекс локализации всегда равен 1.

#### Logistics fee FBO wildberries

Как расчитывается стомость для логистики FBO.

- Переменные и обозначения

| Обозначение | Параметр | Описание |
|-------------|----------------------|--------------------------------------------------------------------------|
| $V$ | `box_volume` | Объём упаковки в литрах |
| $I$ | `local_index` | Индекс локализации |
| $C\_{\\text{base}}$ | `base_price` | Базовая стоимость логистики за объем $V \\gt 1$ |
| $C\_{\\text{min1}}$ | `min_lim_1_price` | Стоимость логистики за малый объём $0 \\lt V \\leq 0.2$ литров |
| $C\_{\\text{min2}}$ | `min_lim_2_price` | Стоимость логистики за малый объём $0.2 \\lt V \\leq 0.4$ литров |
| $C\_{\\text{min3}}$ | `min_lim_3_price` | Стоимость логистики за малый объём $0.4 \\lt V \\leq 0.6$ литров |
| $C\_{\\text{min4}}$ | `min_lim_4_price` | Стоимость логистики за малый объём $0.6 \\lt V \\leq 0.8$ литров |
| $C\_{\\text{min5}}$ | `min_lim_5_price` | Стоимость логистики за малый объём $0.8 \\lt V \\leq 1$ литра |
| $C\_{\\text{vol}}$ | `volume_factor` | Стоимость логистики за каждый дополнительный литр |

- Идея расчета

  Если объем упаковки от 0.001 до 0.2 литров включительно, то стоимость логистики расчитывается как произведение min_lim_1_price * local_index:\
  $L = C\_{\\text{min1}} \\cdot I$

  Если объем упаковки от 0.2 до 0.4 литров включительно, то стоимость логистики расчитывается как произведение min_lim_2_price * local_index:\
  $L = C\_{\\text{min2}} \\cdot I$

  Если объем упаковки от 0.4 до 0.6 литров включительно, то стоимость логистики расчитывается как произведение min_lim_3_price * local_index:\
  $L = C\_{\\text{min3}} \\cdot I$

  Если объем упаковки от 0.6 до 0.8 литров включительно, то стоимость логистики расчитывается как произведение min_lim_4_price * local_index:\
  $L = C\_{\\text{min4}} \\cdot I$

  Если объем упаковки от 0.8 до 1 литра включительно, то стоимость логистики расчитывается как произведение min_lim_4_price * local_index:\
  $L = C\_{\\text{min5}} \\cdot I$

  Если объем упаковки 1 литро более, то стоимость логистики расчитывается как:\
  (base_price + (box_volume - 1) * volume_factor) * local_index:\
  $L = (C\_{\\text{base}} + (V - 1) \\cdot C\_{\\text{vol}}) \\cdot I$

- Формула

$$
L(V) =
\\begin{cases}
C\_{\\text{min1}} \\cdot I & 0 \\lt V \\leq 0.2 \\\\[6pt]
C\_{\\text{min2}} \\cdot I & 0.2 \\lt V \\leq 0.4 \\\\[6pt]
C\_{\\text{min3}} \\cdot I & 0.4 \\lt V \\leq 0.6 \\\\[6pt]
C\_{\\text{min4}} \\cdot I & 0.6 \\lt V \\leq 0.8 \\\\[6pt]
C\_{\\text{min5}} \\cdot I & 0.8 \\lt V \\leq 1 \\\\[6pt]
(C\_{\\text{base}} + (V - 1) \\cdot C\_{\\text{vol}}) \\cdot I & V \\gt 1 \\\\[6pt]
\\end{cases}
$$

#### Returns fee Wildberries

#### Profit fee Wildberries
 
#### Price fee Wildberries

<br>
<br>
<br>

______________________________________________________________________

## Project structure

**feature based organisation**

```
wzcalc 

```

______________________________________________________________________

## Calculator core package

### Core package structure

```
Core
.
│ 
├──   __init__.py 
│ 
├──   interfaces
│    ├──   __init__.py
│    ├──   oz_interfaces.py
│    └──   wb_interfaces.py
│  
├──   services
│    ├──   __init__.py
│    ├──   oz_services.py
│    └──   wb_services.py
│ 
├──   calculators
│    ├──   __init__.py
│    ├──   common.py
│    ├──   ozon.py
│    └──   wildberries.py
│ 
└──   domain
     ├──   __init__.py
     ├──   enums.py
     ├──   oz_calcdata.py
     └──   wb_calcdata.py

```

### Description

Пакет Core предоставляет сервисы для соответствующих расчетов.
Core стремится быть независимым от фреймворка поэтому оперирует dataclass и имеет интерфейсы.

#### interfaces

Интерфейсы для fastapi

**oz_interfaces**

**wb_interfaces**

#### services

Сервисы расчетов

**oz_services**

*oz_calculate_returns_fbs*  
Функция-cервис расчета стоимости возвратов для Ozon с учетом логистики FBS  

*oz_calculate_returns_fbo*  
Функция-cервис расчета стоимости возвратов для Ozon с учетом логистики FBO  

*oz_calculate_reverse_logistics_fee*  
Функция-cервис расчета стоимости обратной логистики для Ozon   

*oz_calculate_profit*  
Функция-cервис расчета стоимости профита для Ozon  

**wb_services**

*wb_calculate_returns*  
Функция-cервис расчета стоимости возвратов для Wildberries  


#### calculators

Калькуляторы

**common**

*box_volume_clc*  
Функция-калькулятор объема упаковки исходя из размеров в сантиметрах переданных одной строкой вида "12\*10\*10"

*comissions_fee_clc*  
Функция-калькулятор фактической стоимости комиссии исходя из процента комиссии

*round_decimal*  
Округляет значение типа данных Decimal в большую сторону до одного знака после запятой

**ozon**

*oz_last_mile_clc*  
Функция-калькулятор стоимости последней мили для Ozon

*oz_log_fbs_clc*  
Функция-калькулятор стоимости логистики FBS для Ozon

*oz_log_fbo_clc*  
Функция-калькулятор стоимости логистики FBO для Ozon

*oz_returns_clc*  
Функция-калькулятор стоимости возвратов для Ozon

*oz_profit_ts_simple_clc*  
Функция-калькулятор профита исходя из цены для налооблажения % от стоимости товара для Ozon

*oz_profit_ts_diff_clc*  
Функция-калькулятор профита исходя из цены для налооблажения % от чистой прибыли (доход - расход) для Ozon

**wildberries**

*wb_log_clc*  
Функция-калькулятор стоимости логистики для Wildberries

*wb_returns_clc*  
Функция-калькулятор стоимости возвратов для Wildberries

#### domain

Dataclasses

**oz_calcdata**

**wb_calcdata**

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

## References

[fast api best practices](https://github.com/zhanymkanov/fastapi-best-practices?tab=readme-ov-file#async-routes)
