#### Lesson 1

emily = 9
daddy = 41
print("Emily's age plus daddy's age makes", emily + daddy)

if emily > daddy:
  print("Emily is older")
elif daddy > emily:
  print("Daddy is older")
else:
  print("Emily and daddy are the same age")

greeting = "Hello "

sentence = greeting + "Emily"
print(sentence)

name = input('What is your name? ')
age = int(input("How old are you? "))
length = len(name)
print(f"Hello {name}, your name has {length} letters.")

if age > emily:
  print("You are older than Emily")
elif age < emily:
  print("You are younger than Emily")
else:
  print("You are the same age as Emily")

total = 0
total = total + emily
total = total + daddy
print(total)

#### Lesson 2

list_of_fruits = ["pear", "banana", "apple"]
print(list_of_fruits)
print("The first fruit is", list_of_fruits[0])
print("The last fruit is", list_of_fruits[-1])

for fruit in list_of_fruits:
  print(fruit, len(fruit))

print(list(range(100)))
total = 0
fact = 1
for number in range(1, 100):
  total = total + number
  fact = fact * number

print(total, fact)

list_of_fruits = sorted(list_of_fruits)
print("We sorted them, now the first fruit is", list_of_fruits[0])

list_of_fruits_with_lengths = [(len(f), f) for f in list_of_fruits]
print(list_of_fruits_with_lengths)
ll = sorted(list_of_fruits_with_lengths)
print(ll)

lines = open("test.txt", "r").readlines()
print(lines)
for line in lines:
  print(line.strip())


def add(a, b):
  return a + b

def strip_non_alpha(word):
  return list(filter(lambda x: x.isalpha(), word.lower()))


print(strip_non_alpha("Emily is 9!"))


def is_palindrome(word):
  word = strip_non_alpha(word)
  for (i, ch) in enumerate(word):
    if i > len(word) // 2:
      return True
    if ch != word[-(i + 1)]:
      return False


def is_palindrome(word):
  word = list(filter(lambda x: x.isalpha(), word.lower()))
  for (a, b) in zip(word, reversed(word)):
    if a != b:
      return False
  return True


def is_p(word):
  word = list(filter(lambda x: x.isalpha(), word.lower()))
  return all(a == b for (a, b) in zip(word, reversed(word)))


print(is_palindrome("A man, a plan, a canal, Panama!"),
      is_palindrome("banana"))

print(is_p("A man, a plan, a canal, Panama!"))

print(is_pal("A man, a plan, a canal, Panama!"))
print(is_pal("Emily is 9!"))
print(is_pal("Anana"))
print(is_pal("Rotator"))
