def flatten(start: list, finish: None | list = None, depth: int = -1) -> list:
    if finish is None:
        finish = []
    if depth == 0:
        finish.extend(start)
        return finish

    for elem in start:
        if isinstance(elem, list):
            flatten(elem, finish, depth - 1)
        else:
            finish.append(elem)

    return finish

if __name__ == "__main__":
    a = flatten([1, 2, [4, 5], [6, [7]], 8], depth=1)
    print(a)
    f = 2;