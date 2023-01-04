raw_input: str = None

with open("input") as fd:
    raw_input = fd.read()

# raw_input = """2-4,6-8
# 2-3,4-5
# 5-7,7-9
# 2-8,3-7
# 6-6,4-6
# 2-6,4-8"""

data = [a.split(",") for a in raw_input.splitlines()]


def convert(p):
    s, e = p.split("-")
    return (int(s), int(e))


overlap = 0
p1 = 0

for pair in data:
    a, b = pair
    a_s, a_e = convert(a)
    b_s, b_e = convert(b)

    # FOR COMPLETE OVERLAP
    # check if range a is contained in b
    if a_s >= b_s and a_e <= b_e:
        overlap += 1
        p1 += 1
        continue
    # check if range b is contained in a
    elif b_s >= a_s and b_e <= a_e:
        overlap += 1
        p1 += 1
        continue

    # FOR ANY OVERLAP LIKE (5-7, 7-9) & (2-6,4-8)
    # if b partially overlaps over a
    if a_s <= b_s and b_s <= a_e:
        overlap += 1
        continue

    # if a partially overlaps over b
    if b_s <= a_s and a_s <= b_e:
        overlap += 1
        continue

# print(p1)
print(overlap)
