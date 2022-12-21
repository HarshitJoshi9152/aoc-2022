raw_input : str = None

with open("input") as fd:
  raw_input = fd.read()

# max_sum = 0

# 0 -> min value, -1 -> max value
top3 = [0, 0, 0]


for elf in raw_input.split("\n\n"):
  calories = map(int, elf.split("\n"))
  elf_sum = sum(calories)
  print(elf_sum)
  if (top3[0] < elf_sum):
    top3.append(elf_sum)
    top3.sort() # sorts in ascending order by default
    top3 = top3[1:]

print(top3)
print(sum(top3))