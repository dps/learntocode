# Lesson 3 - lists and loops

In this lesson, we're going to learn about lists and loops in Python.

First, let's look at this line of code:

```python
list_of_fruits = ["pear", "banana", "apple"]
print(list_of_fruits)
print("The first fruit is", list_of_fruits[0])
print("The last fruit is", list_of_fruits[-1])
```

This code creates a list, which is a type of variable that can hold multiple values. In this case, the list is called `list_of_fruits` and it holds the values `"pear"`, `"banana"`, and `"apple"`.

We write lists in python by putting elements inside square brackets `[ ]` and separating them with commas `,`

Lists can contain python data of any type - we can write a list of `int`s, `str`s... we can even mix the type of elements inside a list (though this is not done often by programmers as it's rarely the clearest or easiest thing to understand)
```python
>>> [1, 2, 3, 4]
[1, 2, 3, 4]
>>> ['Labrador Retriever', 'German Shepherd', 'Golden Retriever', 'Bulldog', 'Poodle']
['Labrador Retriever', 'German Shepherd', 'Golden Retriever', 'Bulldog', 'Poodle']
>>> [1, 'poodle', 2, 'pug']
[1, 'poodle', 2, 'pug']
>>> 
```

The next line of code:

print(list_of_fruits)

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
