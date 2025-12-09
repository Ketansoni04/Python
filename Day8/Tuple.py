# tea_types = ("Black","Green","Oalang")
# >>> tea_types
# ('Black', 'Green', 'Oalang')
# >>> tea_types[0] = "Hebal"
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment
# >>> tea_types[-1]
# 'Oalang'
# >>> tea_types[1:]
# ('Green', 'Oalang')
# >>> tea_types[0]  
# 'Black'
# >>> len(tea_types)
# 3
# >>> more_tea =("Herbal","Earl Grey")
# >>> all_tea = more_tea + tea_types
# >>> all_tea = more_tea + tea_types
# >>> all_tea                          
# ('Herbal', 'Earl Grey', 'Black', 'Green', 'Oalang')
# >>> if "Green" in all_tea:
# ...     print("I have green Tea")
# ... 
# I have green Tea
# more_tea = ("Herbal","earl Grey ", "Herbal") 
# >>> more_tea                                    
# ('Herbal', 'earl Grey ', 'Herbal')
# >>> more_tea.count("Herbal")
# 2   
# >>> more_tea.count("Her")    
# 0
# >>> tea_types = ('black','green','OOlang') 
# >>> tea_types = ('Black','Green','Oolang') 
# >>> (black,green,Oolang) = tea_types       
# >>> Black
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'Black' is not defined. Did you mean: 'black'?
# >>> black
# 'Black'
# >>> type(tea_type)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'tea_type' is not defined. Did you mean: 'tea_types'?
# >>> type(tea_types)
# <class 'tuple'>
# >>> ("",(1,2,4),"")
('', (1, 2, 4), '')