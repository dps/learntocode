# Lesson 1 - part 4

## floats

The other kind of numbers are fractions, which computer programmers usually call "floating point numbers" in python these are called `float`s
```
>>> 1.5
1.5
>>> 3/2
1.5
>>> 3.14
3.14
>>> 100.0
100.0
```

Python can express other kinds of data as well as numbers, here's how you write words, punctuation and sentences in python:

## Strings
```
>>> "Hello, Emily!"
'Hello, Emily!'
```
The name for the type of letters and sentences in programming languages is `string` -- python abbreviates this to `str` in most places. You tell python you are writing a string by starting with `"` or `'` (a double quote or a single quote). You can use either, but if you start your string with a `"` you need to finish it with a `"` and if you start with a `'` you need to finish with a `'`.

> Try writing some more strings in python.

> Strings can contain letters and symbols in languages other than English. They can even contain emoji.
```
>>> "j'étais très excité"
"j'étais très excité"
>>> "苹果 🍎"
'苹果 🍎'
```

> What happens if you forget to use the " at the start? What happens if you finish the string with a different quote than you started it with?

```
>>> hello emily
  File "<stdin>", line 1
    hello emily
          ^^^^^
SyntaxError: invalid syntax

>>> "Oops'
  File "<stdin>", line 1
    "Oops'
    ^
SyntaxError: unterminated string literal (detected at line 1)
```

A SyntaxError occurs when the code you wrote doesn't follow the correct rules of the programming language. It's like if you're writing a letter in English, but you forget to use the right punctuation, capitalization, or spelling, the person reading your letter might not understand what you mean. Similarly, if the computer doesn't understand your code, it will tell you by raising a SyntaxError.

Just like our math statement earlier, we can do operations like `+` on strings. What do you think python will do with this expression?

> `"Emily " + "likes python"`

Try typing that in to python in the Shell.

> What do you think `"Daddy" * 2` will do? Try it for yourself.

> Can you make a string that says "Emily" 10 times?
