# Lesson 2 - program files

So far we've been typing single lines of python code into the _interpreter_ but the way we usually write code is to put lots of lines together in a _file_. Python _reads_ the file and runs each line of code in it in order just like following the steps of a recipe.

A file is like a sheet of paper stored in the computer's long term memory. Just like you can write or draw something on a piece of paper and keep it somewhere safe, you can also create a file on a computer and "save" it to the computer's long term memory. (Which is also often called a "disk".)

> _Fun fact_: When Daddy was a kid this kind of long term computer memory was literally a disk of spinning metal or plastic which the computer stored data on in little tiny magnetized regions. Nowadays we use a kind of memory chip for long term storage but we often still call them disks.)
You can name the file whatever you want, just like you write a title on a piece of paper. 

Just like we can use a piece of paper to store different types of information, like a story you wrote or a drawing you made, you can also use files to store different types of information on a computer, like a song, a movie, or a game. Python programs are written in text files.

When choose names for files we usually give them an _extension_ which helps us and the computer know what kind of data is stored inside. The extension goes after a period.

Here are some file names: `notes.txt`, `emily.png`, `Birthday present list.pdf`.

>For each of these, what is the name and what is the extension?

Some common file extensions:
`.txt` - text file,
`.png` - A PNG file is a type of image file. It stands for "Portable Network Graphics" and is a format that is used to store digital images. 

We write python programs in text files and give them the extension `.py` so we know that they contain python code.

A text file is a type of computer file that contains only plain text, without any formatting or special characters. It's like a regular notebook where you can write words, sentences, and numbers, but instead of being written by hand, it is created and stored on a computer. You can open a text file using a program called a text editor, and you can also use programming languages like Python to read, write, and make changes to the text file. They are commonly used to store information like notes, stories, and even code that can be read and modified by both humans and computers.

## Your first python program

Let's write our very first python program in a file. Create a new file called `emily.py` and write the following code in it:

```
print("Hello, world")
```

It's a kind of silly programmer tradition that the first program you write in a new language should write _Hello, world_ on the screen.

To run the python program `emily.py` we write `python emily.py` in the Shell. Go ahead and run your program now.
```
~/learntocode$ python emily.py
Hello, World.
```

Let's _edit_ the contents of `emily.py` so they now read:
```
emily = 9
daddy = 41
print("Emily's age plus Daddy's age is", emily+daddy)
```

Now run that same command `python emily.py` again... Now we see a different result printed to the screen because the program - the recipe - has changed.
```
~/learntocode$ python emily.py
Emily's age plus Daddy's age is 50
```

# if / else

Take a look at this python code:

```python
emily = 9
daddy = 41
if emily > daddy:
  print("Emily is older")
else:
  print("Daddy is older or we are the same age")
```

This is called an "if-else" statement. It is used to check if a certain condition is true, and if it is, it will run the code inside the if statement. If the condition is not true, it will run the code inside the else statement.

> What do you think the code above will do?

> Update `emily.py` to match the code above and run it -- did it do what you expected?