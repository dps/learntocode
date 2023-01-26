# Lesson 2 - wrap up

There are many different ways to solve the challenge - here's one!
```python
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
```

```bash
~/learntocode$ python emily.py 
What is your name? Jacob
How old are you? 6
Hello Jacob, your name has 5 letters.
You are 6 years old which means you are younger than Emily
~/learntocode$ python emily.py 
What is your name? Mummy
How old are you? 41
Hello Mummy, your name has 5 letters.
You are 41 years old which means you are older than Emily
~/learntocode$ python emily.py 
What is your name? Emily
How old are you? 9
Hello Emily, your name has 5 letters.
You are 9 years old which means you are the same age as Emily
```