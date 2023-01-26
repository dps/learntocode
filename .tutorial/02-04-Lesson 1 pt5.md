# Lesson 1 - part 5

```python
>>> "Emily " + "likes python"
'Emily likes python'
>>> "Daddy" * 2
'DaddyDaddy'
>>> "Emily" * 10
'EmilyEmilyEmilyEmilyEmilyEmilyEmilyEmilyEmilyEmily'
>>> 
```

## Variables

Take a look at these lines of code

```python
emily = 9
daddy = 41
```

Try typing them both into the python shell. Did it do what you expected?

Now trying typing this line of code in the same python shell:
```python
emily
```
What do you think happened? Explain it to Daddy.

----
```python
>>> emily = 9
>>> daddy = 41
>>> emily
9
>>> daddy
41
```

Those lines of code create two _variables_, called "emily" and "daddy". A variable is like a container that holds a value. In this case, the variable "emily" holds the value of 9, and the variable "daddy" holds the value of 41. The computer remembers what is stored in each container and when you use its name again in future, it looks up the value stored there and uses that in the rest of its calculations. So we can write things like:
```python
>>> emily + 1
10
>>> emily + daddy
50
```

> Try making some other variables yourself and try putting `int`s `float`s and `str`s in them.

## Introducing _functions_ and printing to the screen

Next, let's look at this line of code:

```python
print("Emily's age plus daddy's age makes", emily + daddy)
```

This line of code uses the "print" `function` to print out a sentence on the screen. The "print" function takes whatever is inside the parentheses and displays it on the screen. In this case, it's displaying the sentence "Emily's age plus daddy's age makes 50". The "emily + daddy" part is adding the two variables together to get the sum of 50.

## Congratulations - you've completed lesson 1

Now have some fun - try printing lots of stuff to the screen.