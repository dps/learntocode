# Lesson 2 - part 2 - if/else

```python
emily = 9
daddy = 41
if emily > daddy:
  print("Emily is older")
else:
  print("Daddy is older or we are the same age")
```
```
~/learntocode$ python emily.py
Daddy is older or we are the same age
```

Something important to notice is that the code that runs inside the `if` and `else` statement has two spaces before it. Those spaces `indent` the code. Python understands that blocks of code with the same `indentation` go together. This is different from most other programming languages which put special brackets `{ }` around blocks of code. This makes python code a bit faster to write and forces you to lay it out neatly which makes it easy to read too. It's something a lot of python programmers really love about the language, but it's important to remember.

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

Read this code carefully. What do you think will be printed to the screen when you run it?