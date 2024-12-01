def cycle(iterable):
    while True:
        for item in iterable:
            yield item


def chain(lstIter: list | tuple):
    for elem in lstIter:
        yield from elem


if __name__ == "__main__":

    my_iterable = [1, 2, 3]
    cycled = cycle(my_iterable)

    for i in range(110):
        print(next(cycled))

    asd = chain([iter([1, 2, 3]), iter([1,12,2,3, None, "sfafrgee", True]), iter(range(0, 22))])
    for a in asd:
        print(a)
