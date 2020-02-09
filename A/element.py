records = [
    ('foo', 2, 3),
    ('kee', 'hello'),
    ('foo', 2, 3)
]


def do_foo(x, y):
    print('foo', x, y)


def do_kee(s):
    print('kee', s)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'kee':
        do_kee(*args)
