name = input('What is your name? ')
age = int(input("How old are you? "))
length = len(name)
print(f"Hello {name}, your name has {length} letters.")
emily_age = 9
if emily_age > age:
  compared = "younger than"
if emily_age < age:
  compared = "older than"
if emily_age == age:
  compared = "the same age as"
print(f"You are {age} years old which means you are {compared} Emily")