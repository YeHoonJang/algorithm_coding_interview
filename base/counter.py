from collections import Counter

counter = Counter(["red", "blue", "red", "green", "blue", "blue"])
print(counter["blue"])
print(counter["red"])
print(dict(counter))