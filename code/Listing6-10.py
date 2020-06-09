import dis


def list_comprehension():

    l = [x % 2 for x in range(5)]


print(dis.dis(list_comprehension))
