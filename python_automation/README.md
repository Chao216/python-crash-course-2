# this is the second (application part of another book)
***AUTOMATE THE BORING STUFF WITH PYTHON***

## 1. join list of strings use following syntax
```python
str1 = ", " # could be anything for seperation purpose

longString = str1.join(list1) # you can also use join with tuple, set, dictionary

# you don't have to pre-define a spe string

longString1 = ' # '.join(tuple1) # you can write the sep string right before .join()
```

## 2. pyperclip copy, paste

pyperclip allow python to access to clipboard

```python
import pyperclip as pc

text1 = "Hello, how are you doing? "

pc.copy(text1) # copy content from text1

text2 = pc.paste() paste content to text2

print(text2) # same as text1
```
