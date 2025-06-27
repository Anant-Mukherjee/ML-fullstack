data = ['cat', 'dog', 'cat', 'bird', 'dog', 'cat']
data_freq = dict()
for animal in data:
  if animal in data_freq:
    data_freq[animal] += 1
  else:
    data_freq.update({animal: 1})
print(data_freq)

seen = set()
ans = []
for animal in data:
  if animal in seen:
    continue
  else:
    ans.append(animal)
    seen.add(animal)
print(ans)
print("\n\n")


pairs = [(0, 'cat'), (1, 'dog'), (2, 'elephant')]
index, creature = [], []
for val, animal in enumerate(pairs):
  index.append(val)
  creature.append(animal[1])
print(index, creature, sep = "\n", end = "\n\n\n")

sort_animal = sorted(pairs, key = lambda x: x[0], reverse = True)
print(sort_animal)


