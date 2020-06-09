import dis


def for_loop():

    l = []

    for x in range(5):

        l.append(x % 2)


print(dis.dis(for_loop))
