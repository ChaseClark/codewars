def recover_secret(triplets):
    # triplets is a list of triplets from the secrent string. Return the string.
    order = []
    for t in triplets:
        for c in t:
            if c not in order:
                order.insert(0, c)

    # first sorting pass
    for t in triplets:
        move(order, t[0], t[1])
        move(order, t[1], t[2])

    # second pass
    for t in triplets:
        move(order, t[0], t[1])
        move(order, t[1], t[2])

    return "".join(order)


def move(list, a, b):
    if list.index(a) > list.index(b):
        list.remove(a)
        list.insert(list.index(b), a)


test = [
    ["t", "u", "p"],
    ["w", "h", "i"],
    ["t", "s", "u"],
    ["a", "t", "s"],
    ["h", "a", "p"],
    ["t", "i", "s"],
    ["w", "h", "s"],
]

print(
    f"input:{test} output:{recover_secret(test)} correct?:{recover_secret(test) == 'whatisup'}"
)
