# Lesson 2 - part 3

```python
flip = 1
if flip > 0:
  print("Flip!")
  print("flap")
print("flop")
flip = 0
if flip > 0:
  print("Flip!")
print("flop")
```

```bash
~/learntocode$ python emily.py
Flip!
flap
flop
flop
```

## Booleans

It's time to learn about a new type of data - booleans, which python abbreviates to `bool`. A boolean value is a value that can be either true or false. Think of it like a light switch, it can be either on or off. In programming, we use boolean values to make decisions and control the flow of the program. For example, if a certain condition is true, we want to run some code, and if it's false, we don't want to run that code. Boolean values are often used in if/else statements.

```
>>> True
True
>>> False
False
>>> 1 > 0
True
>>> 0 > 1
False
```

We can store `bool`s in variables just like `int`s and `str`s and use them in `if` statements like this:
```python
emily = True
if emily:
  print("Yo!")
```

We already saw how to use the greater than symbol `>` to return a `bool`.
```python
>>> 5 > 3
True
```
Another important thing to know is how to check that two values are equal. In Python, the `==` symbol is called the "comparison operator." It is used to compare two values and see if they are equal to each other. When you use the `==` operator, Python will check if the value on the left side of the operator is the same as the value on the right side. If they are the same, it will return `True`. If they are different, it will return `False`.

For example, let's say you have a variable x with the value 5 and you want to check if it is equal to another number, 7. You would write `x == 7` and Python would return `False` because 5 is not the same as 7.

You can also use == to compare strings or other types of data as well. For example, `"hello" == "hello"` would return `True`, because the two strings are the same.

One last thing, sometimes we want to check if variables are *not* equal - in python you can write `not` before any `bool` to get its inverse.
```python
>>> not True
False
>>> not False
True
>>> if not 1 == 0:
  print("Yo!") 
Yo!
```
## One more thing about strings

Earlier, we learned about the `print` function which writes stuff to the screen. There are lots of functions in python and we'll soon learn how to write our own. Let's learn about one right now.
```python
>>> len("Emily")
5
```
What do you think the `len` function does? Try it with some other strings.

As you probably figured out, `len` takes a string and _returns_ an `int` which is the length of the string you passed in.

```python
>>> len("Emily")
5
>>> len("Hello, world!")
13
>>> len("Daddy is the best")
17
>>> len("")
0
```

## input

To make our programs a bit more useful, we can make them _interactive_. An interactive program is a program that allows you to enter input and get immediate output. It allows you to have a conversation with the computer and get immediate feedback on your actions. We've seen an example of an interactive program already - the Python shell where you can type in commands and see the results right away.

To do this in our own programs we use the `input` function. Try this in the python shell:
```
>>> name = input("What is your name?")
What is your name? Emily
>>> name
'Emily'
```

Let's try this whole program (you can save it as `emily.py` again or give it a new name if you like):

```python
name = input('What is your name? ')
age = int(input("How old are you? "))
length = len(name)
print(f"Hello {name}, your name has {length} letters.")
```

There's something else new in here. "F strings" is a way to add variables into a string in Python. Instead of using the plus sign (`+`) to combine a string and a variable, you can use curly braces `{}` inside a string that starts with the letter "`f`". This way, you can insert a variable's value directly into the string. For example, instead of writing `"My name is " + name`, you can write `f"My name is {name}"`. This is more readable and easier to use when you have lots of variables in the string.

## Challenge

To complete lesson 2 modify the code you just saved to also print out the age of the person using the program and whether or not they are older than Emily!

