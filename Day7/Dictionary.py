#  chai_type =  {"Masala": "Spicy", "Ginger_tea" : "Zesty" , "Green" : "Mild"}
# >>> chai_type["Masala"]
# 'Spicy'
# >>> chai.type.get("Ginger")
# Traceback (most recent call last):   
#   File "<stdin>", line 1, in <module>
# NameError: name 'chai' is not defined
# >>> chai_type.get("Ginger") 
# >>> chai_type.get("Ginger_tea")
# 'Zesty'
# >>> chai_type["Masal"]          
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'Masal'
# >>> chai_type["Green"] = "fresh"
# >>> chai_type                   
# {'Masala': 'Spicy', 'Ginger_tea': 'Zesty', 'Green': 'fresh'}
# >>> for chai in chai_type: 
# ...     print(chai)
# ... 
# Masala
# Ginger_tea
# Green
# >>> for chai in chai_type:
# ...     print(chai,chai_type()
# ...  
# ... ^Z

#   File "<stdin>", line 2
#     print(chai,chai_type()
#          ^
# SyntaxError: '(' was never closed
# >>> for chai in chai_type: e()
# ...     print(chai, chai_type[chai])
# ... 
# Masala Spicy
# Ginger_tea Zesty
# Green fresh
# >>> for key,value in chai_type.item():
# ...     print(key, value)        i])   
# ... 
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'dict' object has no attribute 'item'. Did you mean: 'items'?
# >>> for key,value in chai_type.items():
# ...     print(key, value)
# ... 
# Masala Spicy
# Ginger_tea Zesty
# Green fresh
# >>> if "Masala" in chai_type:
# ...     print(True)      
# ... 
# True
# >>> print(len(chai_type)) 
# 3
# >>> chai_type["Herbal"] = "Mild" i])   
# >>> chai_type                     
# {'Masala': 'Spicy', 'Ginger_tea': 'Zesty', 'Green': 'fresh', 'Herbal': 'Mild'}
# >>> chai_type.pop("Ginger"]
#   File "<stdin>", line 1
#     chai_type.pop("Ginger"]
#                           ^
# SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
# >>> chai_type.pop("Ginger")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'Ginger'
# >>> chai_type.pop("Ginger_tea")
# 'Zesty'
# >>> chai_type.popitem          
# <built-in method popitem of dict object at 0x00000261AC937C40>
# >>> chai_type.popitem()
# ('Herbal', 'Mild')
# >>> chai_type          
# {'Masala': 'Spicy', 'Green': 'fresh'}
# >>> del chai_type["Green"]  delete the reference from memory     
# >>> chai_type
# {'Masala': 'Spicy'}
# >>> chai_type_copy = chai_type.copy()                                                                              
# >>> [[],[],[]]                                                                     
# [[], [], []]
# >>> tea_shop = {
# ... "chai" : {Masala: "Spicy", " Ginger": "Zesty"},     
# ... "Tea" : {"Green": "Mild","Black" : "Strong"}
# ... }
# Traceback (most recent call last):
#   File "<stdin>", line 2, in <module>
# NameError: name 'Masala' is not defined
# >>> tea_shop = {
# ... "chai" : {"Masala": "Spicy", " Ginger": "Zesty"}, 
# ... "Tea" : {"Green": "Mild","Black" : "Strong"}
# ... }
# >>> tea_shop
# {'chai': {'Masala': 'Spicy', ' Ginger': 'Zesty'}, 'Tea': {'Green': 'Mild', 'Black': 'Strong'}}
# >>> tea_shop["chai"]
# {'Masala': 'Spicy', ' Ginger': 'Zesty'}
# >>> tea_shop["chai"]["Ginger"]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'Ginger'
# >>> tea_shop["chai"][" Ginger"]
# 'Zesty'
# >>> squared_num = {x:x**2 in range(10)} 
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'x' is not defined
#  squared_num = {x:x**2 for x in range(10)}  
# >>> squared_num
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
# >>> keys = ["Ginger", "Green"]       
# >>> default_value = "Mild"
# >>> tea = dic.fromkeys(keys,default_value)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'dic' is not defined. Did you mean: 'dir'?
# >>> tea = dict.fromkeys(keys,default_value) 
# >>> tea
# {'Ginger':

