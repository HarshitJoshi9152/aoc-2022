import string

# a , A are different types of items and input is a list of types

"""
To help prioritize item rearrangement, every item type can be converted to a priority:

    Lowercase item types a through z have priorities 1 through 26.
    Uppercase item types A through Z have priorities 27 through 52.

I think we will need to sort the items on the basis of their priorities in the second half !
"""


demo_input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""


raw_input = None
with open("input") as fd:
    raw_input = fd.read()


def find_priority(fst, snd):  # bad naming
    # what would be a better way to do this ???? idk !!!
    for c in fst:
        for s in snd:
            if c == s:
                # print(c)
                return string.ascii_letters.find(c) + 1


# items = demo_input.splitlines()
items = raw_input.splitlines()

priorities = [] * len(items)  # pre-allocation

for item in items:
    # split in 2 parts and find the common part then find adn store priorites
    l = len(item)
    first_item = item[0 : l // 2]
    second_item = item[l // 2 :]
    priority = find_priority(first_item, second_item)
    priorities.append(priority)

# print(sum(priorities))


l = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
]

# should have used sets instead lol !
# But i wanted to try and do it this way !

a_bl = {}  # a bit list
b_bl = {}
c_bl = {}
# Maybe theres a better way to do this
for c in string.ascii_letters:
    a_bl[c] = 0
    b_bl[c] = 0
    c_bl[c] = 0

# what would happen if i zip them together since they are not of the same size !
def find_common(x, y, z):

    # print(x)
    # print(y)
    # print(z)
    common = []

    for c in x:
        a_bl[c] = 1

    for c in y:
        b_bl[c] = 1

    for c in z:
        c_bl[c] = 1

    for c in string.ascii_letters:
        # print(c, a_bl[c])
        # print(c, b_bl[c])
        # print(c, c_bl[c])
        # print()
        if a_bl[c] == 1 and b_bl[c] == 1 and c_bl[c] == 1:
            common.append(c)
        # clear cache
        a_bl[c] = 0
        b_bl[c] = 0
        c_bl[c] = 0

    return common


# print(find_common(*l))

# items = [
#     "vJrwpWtwJgWrhcsFMMfFFhFp",
#     "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
#     "PmmdzqPrVvPwwTWBwg",
#     "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
#     "ttgJtRGJQctTZtZT",
#     "CrZsJsPPZsGzwwsLwLmpwMDw",
# ]

prioties_2 = []

for i in range(0, len(items), 3):
    a = items[i]
    b = items[i + 1]
    c = items[i + 2]
    c, *args = find_common(a, b, c)
    prio = string.ascii_letters.find(c) + 1
    prioties_2.append(prio)

print(sum(prioties_2))
