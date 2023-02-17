Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
tao = turtle.Pen()
#draw a pattern
while True:
    pensize(4)
    pencolor('red')
    circle(50)
    forward(5)
    right(25)
    turtle.done()

    
Traceback (most recent call last):
  File "<pyshell#10>", line 2, in <module>
    pensize(4)
NameError: name 'pensize' is not defined
tao.clear()
#draw a pattern
while True:
    pencolor('red')
    circle(50)
    forward(5)
    right(25)

    
Traceback (most recent call last):
  File "<pyshell#18>", line 2, in <module>
    pencolor('red')
NameError: name 'pencolor' is not defined
>>> NameError: name 'pencolor' is not defined
SyntaxError: invalid syntax
>>> tao.clear()
>>> penup()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    penup()
NameError: name 'penup' is not defined
>>> tao.clear()
>>> from turtle import*
>>> penup()
>>> for a in range (40, -1, -1) :
...     stamp()
...     left(a)
...     forward(20)
... 
...     
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
