# Outer Space!
Write a function that will make every character in a given string one space apart

## Input
One argument (String)
  
## Output
The same string with a space between every character, except at the end

## Example
```python
space("Hello") == "H e l l o"
space("k") == "k"
space("Goodbye") == "G o o d b y e"
```



# math?
Write a function that parses a length 3 string into an equation to solve

## Input
One argument (String {length 3, first and third character = number, second = + or -})

## Output
An integer based on the 'equation'

## Example
```python
maths("3+2") == 5
maths("0-0") == 0
maths("2-9") == -7
```



# Inner Space?
Write a function that gets rid of all spaces in a given string

## Input
One argument (String)

## Output
A new string without spaces

## Example
```python
nospace("Hello World") == "HelloWorld"
nospace("Please no") == "Pleaseno"
nospace(space("literally anything")) == "literallyanything"
```



# CAPSLOCK
Write a function that converts a given string to upper case

## Input
One argument (String)

## Output
A new string converted to upper case

## Example
```python
caps("not capital") == "NOT CAPITAL"
caps("PleAsE nO") == "PLEASE NO"
caps(nospace(space("okeedokee"))) == "OKEEDOKEE"
```



# Splice and (don't) Dice
Write a function that will splice two strings together in an alternating pattern

## Input
Two arguments (String), (String) {of equal length}

## Output
One string made of alternating parts of the two passed arguments

## Example
```python
splice("Hello", "World") == "HWeolrllod"
splice("rUh", "RoH") == "rRUohH"
splice("HloWrd", "el ol!") == "Hello World!
```
