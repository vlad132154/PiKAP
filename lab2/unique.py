class Unique(object):
    def __init__(self, items, **kwargs):
        self.ignore_case = kwargs.get('ignore_case', False)
        self.iterator = iter(items)
        self.seen = set()

    def __next__(self):
        while True:
            item = next(self.iterator)
            key = item.lower() if self.ignore_case and isinstance(item, str) else item
            if key not in self.seen:
                self.seen.add(key)
                return item

    def __iter__(self):
        return self


if __name__ == '__main__':
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    print(list(Unique(data)))

    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    print(list(Unique(data)))
    print(list(Unique(data, ignore_case=True)))