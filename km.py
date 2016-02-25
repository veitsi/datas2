import random


def uniq_random(n, k):
    if k > n:
        return None
    a = []
    for i in range(n):
        a.append(i)

    rez = []
    for i in range(k):
        r = random.randint(0, n - 1 - i)
        rez.append(a[r])
        del a[r]
    return rez


def distance(x, c):
    return abs(c - x)


def center_coordinates(x, newclass, k):
    rez, class_capacity = [0] * k, [0] * k
    for i in range(len(x)):
        pclass = newclass[i]
        rez[pclass] += x[i]
        class_capacity[pclass] += 1
    for i in range(k):
        rez[i] /= class_capacity[i]
    return rez


def km(x, k):
    n = len(x)
    if k < 1 or n / k < 1:
        return None
    oldclass, newclass, center_coords = [-1] * n, [0] * n, []
    center_indexes = uniq_random(len(x), k)
    for i in center_indexes:
        center_coords.append(x[i])
    iterations = 0
    while iterations < 10 and newclass != oldclass:
        oldclass = newclass
        i = 0
        while i < len(x):
            closest = 0
            min_dist = distance(x[i], center_coords[0])
            j = 1
            while j < k:
                if distance(x[i], center_coords[j]) < min_dist:
                    closest = j
                    min_dist = distance(x[i], center_coords[j])
                j += 1
            newclass[i] = closest
            i += 1
        iterations += 1
        center_coords = center_coordinates(x, newclass, k)
    print(center_coords)
    return newclass, oldclass


# assert km([1, 2, 9, 10], 1) is not None
# assert km([1, 2, 9, 10], 1) == [1, 2, 9, 10]
#
# assert km([1, 2], 0) is None
# assert km([2], 2) is None
# assert km([2, 3, 7], 5) is None

# print(center_coordinates([2,4, 8,10],[0,0,1,1],2))
a1, a2 = km([2, 5, 122, 12, 25, 100, 140, 7, 0], 2)
print(a1, a2)

# print(uniq_random(12,3))
# print(uniq_random(3,3))
# print(uniq_random(1,1))
a = uniq_random(12, 3)
assert a[0] != a[1] != a[2]
