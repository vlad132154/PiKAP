def field(items, *args):
    assert len(args) > 0

    if len(args) == 1:
        key = args[0]
        for item in items:
            value = item.get(key)
            if value is not None:
                yield value
    else:
        for item in items:
            row = {}
            for key in args:
                value = item.get(key)
                if value is not None:
                    row[key] = value
            if row:
                yield row


if __name__ == '__main__':
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]

    print(list(field(goods, 'title')))
    print(list(field(goods, 'title', 'price')))