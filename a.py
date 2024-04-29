bicycles = ["trek","cannondale","specialized"]
print(bicycles[1])
print(bicycles[2])

print(bicycles[-1])


magicians = ["alan","cx330","frank"]
for magician in magicians:
    print(magician)

for magician in magicians:
    print(magicians)

for x in "banana":
    print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

  fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

from random import randint
randint(1,6)

for x in range(1,10,2):
   print(x)