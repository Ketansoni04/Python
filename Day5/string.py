#  setone = {1,2,3,4}
# >>> setone & {1,3}
# {1, 3}
# >>> setone | {1,3}
# {1, 2, 3, 4}
# >>> setone | {1,3,5,7} 
# {1, 2, 3, 4, 5, 7}                                                          
# > > setone | {1,3,5,7}                                                                                                                      
# {1, 2, 3, 4, 5, 7}
# >>> setone - {1,2,3,4}
# set()
# >>> type({})
# <class 'dict'>
# >>> type(True)
# <class 'bool'>
# >>> True == 1                                                       
# True
# >>> False == 0
# True
# >>> True is 1 
# <stdin>:1: SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
# False
# >>> True + 4
# 5
# >>>
#  *  History restored 

# PS C:\Users\DC\Desktop\python> 
#  *  History restored 

# PS C:\Users\DC\Desktop\python> 
#  *  History restored 

# PS C:\Users\DC\Desktop\python> python
# Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# Ctrl click to launch VS Code Native REPL
# >>> demo = "hello world"                              
# >>> first_char = demo[0]
# >>> first_char          
# 'h' 
# >>> char_slice = [:6] 
#   File "<stdin>", line 1   
#     char_slice = [:6]      
#                   ^        
# SyntaxError: invalid syntax
# >>> char_slice =demo [:6] 
# >>> char_slice           
# 'hello '
# >>> char_slice =demo [:5] 
# >>> char_slice
# 'hello'
# >>> print(char_slice)
# hello
# >>> print(first_char)
# h
# >>>  num_list = "0123456789"
#   File "<stdin>", line 1
#     num_list = "0123456789"
# IndentationError: unexpected indent
# >>> num_list = "0123456789"  
# >>> print(num_list[0:7:2]) 
# 0246
# >>> print(num_list[0:7:3]) 
# 036
# >>>demo = "Hello World"  
# >>> print(demo.lower())
# hello world
# >>> print(demo.upper()) 
# HELLO WORLD
# >>>        
# >>> demo = "    hello world    "
# >>> print(dem)                   
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'dem' is not defined. Did you mean: 'demo'?
# >>> print(demo)
#     hello world    
# >>> print(demo.strip())
# hello world
# >>> print(demo.raplace) 
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'str' object has no attribute 'raplace'. Did you mean: 'replace'?
# >>> print(demo.replace("hello,"Namaste"))
#   File "<stdin>", line 1
#     print(demo.replace("hello,"Namaste"))
#                                       ^
# SyntaxError: unterminated string literal (detected at line 1)
# >>> print(demo.replace("hello","Namaste"))
#     Namaste world    
# >>>
#  *  History restored 

# PS C:\Users\DC\Desktop\python> python 
# Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# Ctrl click to launch VS Code Native REPL
# >>> demo = "hello world
#   File "<stdin>", line 1
#     demo = "hello world
#            ^
# SyntaxError: unterminated string literal (detected at line 1)
# >>> demo = "hello world"
# >>> demo.lower
# <built-in method lower of str object at 0x000001C99AAF78F0>
# >>> demo.lower()
# 'hello world'
# >>> demo.upper()
# 'HELLO WORLD'
# >>> demo = "     hello World     "
# >>> demo.strip()                  
# 'hello World'
# >>> demo.replace("hello","Namste")  
# '     Namste World     '
# >>> demo = "Namaste, Hello, sastriyakal"  
# >>> demo.split(", ")
# ['Namaste', 'Hello', 'sastriyakal']
# >>> demo.split(",")  
# ['Namaste', ' Hello', ' sastriyakal']
# >>> demo
# 'Namaste, Hello, sastriyakal'
# >>> demo.find("Namaste") 
# 0
# >>> demo.find("Hello, ") 
# 9
# >>> demo = "hello hello hello world"
# >>> demo.count(""hello world) 
#   File "<stdin>", line 1
#     demo.count(""hello world)
#                ^^^^^^^
# SyntaxError: invalid syntax. Perhaps you forgot a comma?
# >>> demo.count("hello")       
# 3
# >>> demo_name = "ketan""      
#   File "<stdin>", line 1
#     demo_name = "ketan""
#                        ^
# SyntaxError: unterminated string literal (detected at line 1)
# >>> demo_name = "ketan" 
# >>> demo_age = 23       
# >>> meassage = "I am {} I am {}"
# >>> print(message.format(demo_name,demo_age)
# ... print(message.format(demo_name,demo_age)^X
#   File "<stdin>", line 2
#     print(message.format(demo_name,demo_age)↑
#                                             ^
# SyntaxError: invalid non-printable character U+0018
# >>> print(message.format(demo_name,demo_age)) 
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'message' is not defined. Did you mean: 'meassage'?
# >>> print(meassage.format(demo_name,demo_age)) 
# I am ketan I am 23
# >>> demo_list = ["Namaste","Hello","SastriyaKal"]
# >>> print(" ".join(demo_list)
# ... print(" ".join(demo_list)
# KeyboardInterrupt
# >>> print(" ".join(demo_list))
# Namaste Hello SastriyaKal
# >>> print("-".join(demo_list)) 
# Namaste-Hello-SastriyaKal
# >>> demo                      
# 'hello hello hello world'
# >>> print(len(demo))
# 23
# >>> demo = "hello world"
# >>> demo =              
#   File "<stdin>", line 1
#     demo =
#           ^
# SyntaxError: invalid syntax
# >>> demo  
# 'hello world'
# >>> for letter in demo:
# ...     print(letter)
# ... 
# h
# e
# l
# l
# o

# w
# o
# r
# l
# d
# >>> demo = "He said \"Masala chai is awesom\" "
# >>> demo
# 'He said "Masala chai is awesom" '
# >>> demo = "Masala\nChai"
# >>> print(demo) 
# Masala
# Chai
# >>> dmo = r"Masala\nChai"
# >>> print(dmo)
# Masala\nChai
# >>> demo = r"drive\:photo\images"  
# >>> print(demo)
# drive\:photo\images
# >>> demo =" drive\\:photo\\images" 
# >>> demo                            
# ' drive\\:photo\\images'
# >>> print(demo)
#  drive\:photo\images
# >>> demo = drive\:photo\imageses   
#   File "<stdin>", line 1
#     demo = drive\:photo\imageses
#                  ^
# SyntaxError: unexpected character after line continuation character
# >>> demo ="hello word"
# >>> demo ="hello world"
# >>> demo ="hello world"

# SyntaxError: invalid syntax
# >>> print("hello" in demo))
#   File "<stdin>", line 1
#     print("hello" in demo))
#                           ^
# SyntaxError: unmatched ')'
# >>> print("hello" in demo) 
# True
# >>> print("hello4" in demo) 
# False