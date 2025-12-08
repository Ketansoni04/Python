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