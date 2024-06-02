# О проекте:

Пэт-проект.
Этот проект представляет собой интернет-магазин на  `Django`, в панели управления Вы сможете создавать,
удалять и редактировать товары или категории. В проекте реализованна оплата с помощью `Stripe`.
В проекте используется концепция REST API `DRF`, поэтому для отдачи информации клиенту существует отдельный API. База
данных изменена на `postgresql`. Добавлен `Celery` для автоматизации отправки писем.

## Функционал покупателя:

- Возможность выбирать категории, переход по одиночным страницам конкретного товара.
- Покупатель может совершать покупки через корзину, оплата осуществляется через сервис Stripe.
- Для создания заказа требуется подтвердить почту.
- Покупатель может посмотреть свои заказы в отдельной странице, и узнать их статус.

## Функционал администратора:

- Для входа в админ-панель необходимо дописать в адресной строке /admin, так же после авторизации админом появляется
  удобная кнопка в меню.
- Можно посмотреть подробные данные о заказе покупателя: номер заказа, дата покупки, сумма, содержимое корзины, и
  изменить статус заказа.
- Возможность добавлять, удалять или редактировать товары на странице "Продукты", так же можно посмотреть и информацию о
  товаре.
- Поиск товаров через поле поиска (нужно знать частичное или полное название товара).
- Добавление, удаление и редактирование категорий через страницу "Категории".
- Возможность изменять данные администратора: почта, пароль, имя.

# API DRF:

Здесь описаны основные запросы на сервер для получения данных:

#### Для просмотра всех товаров которые существуют в магазине отправляется запрос:

``` 
http://127.0.0.1:8000/api/product/
```

Ответ:

```json
{
  "count": 11,
  "next": "http://127.0.0.1:8000/api/product/?limit=3&offset=3",
  "previous": null,
  "results": [
    {
      "id": 2,
      "name": "Горшок",
      "description": "Пластик, 10см диаметр, с дополнительным сливом, цвет серый графит",
      "image": "http://127.0.0.1:8000/media/products_image/product2.jpg",
      "quantity": 2,
      "price": "123.00",
      "category": "Горшки"
    },
    {
      "id": 11,
      "name": "Морские ракушки",
      "description": "Растение продается вместе с золотым горшом и не требует пересадки",
      "image": "http://127.0.0.1:8000/media/products_image/product10.jpg",
      "quantity": 4,
      "price": "4456.00",
      "category": "Растения"
    }
  ]
}
```

#### Для просмотра определенного товара отправляется запрос:

``` 
http://127.0.0.1:8000/api/product/id_producta
```

### Для добавления, удаления, редактирования товаров нужно авторизоваться через админа и получить свой api-token:

```
http://127.0.0.1:8000/api-token-auth/
```

#### Так же можно посмотреть и изменить корзину пользователя с api-token владельца корзины:

```
http://127.0.0.1:8000/api/basket/
```

Ответ:

```
[
    {
        "id": 56,
        "product": {
            "id": 10,
            "name": "Различные суккуленты",
            "description": "Большой выбор различных видов",
            "image": "http://127.0.0.1:8000/media/products_image/product11.jpg",
            "quantity": 1245,
            "price": "125.00",
            "category": "Растения"
        },
        "quantity": 1,
        "sum": 125.0,
        "total_sum": 17949.0,
        "total_quantity": 5,
        "created_timestamp": "2024-05-27T14:45:07.169656Z"
    },
    {
        "id": 53,
        "product": {
            "id": 11,
            "name": "Морские ракушки",
            "description": "Растение продается вместе с золотым горшом и не требует пересадки",
            "image": "http://127.0.0.1:8000/media/products_image/product10.jpg",
            "quantity": 4,
            "price": "4456.00",
            "category": "Растения"
        },
        "quantity": 4,
        "sum": 17824.0,
        "total_sum": 17949.0,
        "total_quantity": 5,
        "created_timestamp": "2024-05-27T14:27:09.071632Z"
    }
]
```

