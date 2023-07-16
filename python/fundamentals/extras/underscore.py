class Underscore:
    def map(self, iterable, callback):
        return [callback(x) for x in iterable]

    def find(self, iterable, callback):
        for x in iterable:
            if callback(x):
                return x
        return None

    def filter(self, iterable, callback):
        return [x for x in iterable if callback(x)]

    def reject(self, iterable, callback):
        return [x for x in iterable if not callback(x)]
