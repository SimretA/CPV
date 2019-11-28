import random


def rann(min, max):
    list1 = list()
    rands = list()
    for i in range(min, max + 1):
        list1.append(i)
    for x in range(0, len(list1)):
        rand = random.randrange(0, len(list1))
        temp = list1[x]
        list1[x] = list1[rand]
        list1[rand] = temp
    return list1


if __name__ == '__main__':
    print(rann(0, 10))
