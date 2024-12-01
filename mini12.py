def coroutine(func):
    def midlleFun(*args, **kwargs):
        obj = func(*args, **kwargs)
        next(obj)
        return obj
    return midlleFun


@coroutine
def storage():
    values = set()
    was_there = False

    while True:
        val = yield was_there
        was_there = val in values
        if not was_there:
            values.add(val)


if __name__ == "__main__":
    st = storage()
    print(st.send(42))
    print(st.send(42))