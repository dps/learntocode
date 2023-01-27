# Lesson 3 - part 2

Try it out in the python interpreter:
```python
>>> alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
```
> How do you get the letter `'e'` out of the `alphabet` list?
```python
>>> alphabet[4]
'e'
```
> Get the letter `'y'` out of the `alphabet` list using a negative index.
```python
>>> alphabet[-2]
'y'
```

## len
Remember the `len` function we learned for strings?
```python
>>> len("emily")
5
```
It works on lists too!
```python
>>> len(["a","b","c"])
3
>>> len(alphabet)
26
```

## append and pop
There are a few more functions we can use on lists. `append` is a way to add something new to the end of a list in Python. Imagine you have a list of your favorite ice cream flavors, and you try a new one that you like. You can use the `append` method to add the new flavor to the end of your list, so you don't forget it.

```python
flavors = ["vanilla"]
flavors.append("chocolate") # flavors is now: ["vanilla", "chocolate"]
```

`pop` does the opposite - the pop() method lets you take the last flavor off of the list, like scooping the last scoop of mint ice cream out of the container. Here's an example of using the pop() method:
```python
ice_cream_flavors = ["chocolate", "vanilla", "strawberry", "mint"]
last_flavor = ice_cream_flavors.pop()
print(last_flavor) # "mint"
print(ice_cream_flavors) # ["chocolate", "vanilla", "strawberry"]
```

### Challenge

## Loops

Uses the "print" function to print out the entire list.

The next line of code:

print("The first fruit is", list_of_fruits[0])

Uses the "print" function to print out the first fruit in the list. Lists in Python are zero-indexed, so the first item in the list is at index 0.

The next line of code:

print("The last fruit is", list_of_fruits[-1])

Uses the "print" function to print out the last fruit in the list. Lists in Python are also indexed in reverse, so the last item in the list is at index -1

Now let's move on to the following lines of code:

for fruit in list_of_fruits:
print(fruit, len(fruit))

This is called a "for loop". It is used to iterate over each item in a list and perform a certain action. In this case, it is printing out each fruit in the list, followed by the length of the fruit using the len() function.

The next line of code:

print(list(range(100)))

Uses the "range" function to create a list of numbers from 0 to 99, and the "list" function is used to create a list of integers from the range function.

The next lines of code:

total = 0
fact = 1
for number in range(1, 100):
total = total + number
fact = fact * number

This code uses a for loop to iterate through the numbers in the range of 1 to 100, and at each iteration adding the number to the total and multipying fact with the number.

Finally, the code sorts the list of fruits using the "sorted" function and prints the first element after sorting and then it creates a list of tuples where each tuple contains the length of the fruit and the name of the fruit and then it sorts this list and prints it.

The range() function in Python is used to generate a sequence of numbers. The general syntax for using the range() function is range(start, stop, step), where start is the first number in the sequence, stop is the last number in the sequence, and step is the increment between numbers in the sequence.

When you call range(100), it is equivalent to calling range(0, 100), which means it will generate a sequence of numbers starting from 0 and ending at 99. This is because in Python, ranges are half-open, meaning that the start value is included, but the stop value is not. So, in this case, the range() function is generating a sequence of numbers from 0 to 99, with a step of 1.

You can also use the range(start, stop) or range(stop) where it will start with the default value of 0 if start is not provided.