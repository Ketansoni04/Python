# tea_varities = ['black', 'green', 'Masala', 'Herbal'] 
# >>> print(tea_varities)
# ['black', 'green', 'Masala', 'Herbal']
# >>> tea_varities[1]                                       
# 'green'
# >>> tea_varities[1:3]   
# ['green', 'Masala']
# >>> tea_varities[1:]  
# ['green', 'Masala', 'Herbal']
# >>> tea_varities[:3]  
# ['black', 'green', 'Masala']
# >>> tea_varities[2] = 'ginger'
# >>> print(tea_varities)
# ['black', 'green', 'ginger', 'Herbal']
# >>> tea_varities[1:2]  =  "Lemon"
# >>> print(tea_varities)
# ['black', 'L', 'e', 'm', 'o', 'n', 'ginger', 'Herbal']
# >>> tea_varities[2] = ['ginger'] 
# >>> print(tea_varities)
# ['black', 'L', ['ginger'], 'm', 'o', 'n', 'ginger', 'Herbal']
# >>> tea_varities[1:1]  =  ["Lemon"]
# >>> print(tea_varities)
# ['black', 'Lemon', 'L', ['ginger'], 'm', 'o', 'n', 'ginger', 'Herbal']
# >>> tea_varities[1:1]  =  ["Lemon",'Lemon']  
# >>> print(tea_varities)
# ['black', 'Lemon', 'Lemon', 'Lemon', 'L', ['ginger'], 'm', 'o', 'n', 'ginger', 'Herbal']
# >>> tea_varities[1:3]  =  []                
# >>> print(tea_varities)      
# ['black', 'Lemon', 'L', ['ginger'], 'm', 'o', 'n', 'ginger', 'Herbal']
# >>> tea_varities = ["black', 'green', 'Masala', 'Herbal'] 
#   File "<stdin>", line 1
#     tea_varities = ["black', 'green', 'Masala', 'Herbal']
#                     ^
# SyntaxError: unterminated string literal (detected at line 1)
# >>> tea_varities = ['black', 'green', 'Masala', 'Herbal'] 
# >>> for tea in tea_varities
#   File "<stdin>", line 1
#     for tea in tea_varities
#                            ^
# SyntaxError: expected ':'
# >>> for tea in tea_varities:
# ...     print(tea)
# ... 
# black
# green
# Masala
# Herbal
# >>> for tea in tea_varities:
# ...     print(tea,end="-")
# ... 
# black-green-Masala-Herbal->>> 
# >>> if "Ginger" in tea_varities:
# ...     print("I have Ginger Tea")
# ... 
# >>> tea_varities.append("Ginger")
# >>> print(tea_varities)
# ['black', 'green', 'Masala', 'Herbal', 'Ginger']
# >>> if "Ginger" in tea_varities:")
# ...     print("I have Ginger tea")
# ... 
# I have Ginger tea
# >>>
#  *  History restored 

# PS C:\Users\DC\Desktop\python> python
# Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# Ctrl click to launch VS Code Native REPL
# >>> tea_varities = ["black","green","Masala","herbal","green"
# ... 
# KeyboardInterrupt
# >>> tea_varities = ["black","green","Masala","herbal","green"]
# >>> tea_variities.pop()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'tea_variities' is not defined. Did you mean: 'tea_varities'?
# >>> tea_varities.pop()  
# 'green'
# >>> tea_varities      
# ['black', 'green', 'Masala', 'herbal']
# >>> tea_varities.remove("Masala") 
# >>> tea_varities
# ['black', 'green', 'herbal']
# >>> tea_varities.insert(1,"green")  
# >>> tea_varities
# ['black', 'green', 'green', 'herbal']
# >>> tea_varities_copy = tea_varities.copy()
# >>> tea_varities                           
# ['black', 'green', 'green', 'herbal']
# >>> tea_varities_copy.append("green")      
# >>> tea_varities
# ['black', 'green', 'green', 'herbal']
# >>> tea_varities_copy                      
# ['black', 'green', 'green', 'herbal', 'green']
# >>> squared_nums = [x**2 for x in range(10)]
# >>> squared_nums                            
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# >>> range(10)
# range(0, 10)
# >>> range(10)
