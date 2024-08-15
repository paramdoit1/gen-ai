# Dictionaries are used to store data values in key:value pairs
# A dictionary is a collection which is ordered, changeable and do not allow duplicates

car_dict = {
    "brand" : "ford",
    "model": "accord",
    "year": 2000
}

print(car_dict["brand"])
#ford

#Get method also used to get the value from dict
print(car_dict.get('model'))
#accord

#Getting all the keys for the dict
car_dict_keys = car_dict.keys()
print("car_dict_keys : ", car_dict_keys)
#car_dict_keys :  dict_keys(['brand', 'model', 'year'])

#Adding item to a dictionary
car_dict['color'] = "green"
print(car_dict)
#{'brand': 'ford', 'model': 'accord', 'year': 2000, 'color': 'green'}

car_dict['year']  = 2010
print(car_dict)
#{'brand': 'ford', 'model': 'accord', 'year': 2010, 'color': 'green'}

#using update() to update the car color
car_dict.update({'color': 'white'})
print(car_dict)
#{'brand': 'ford', 'model': 'accord', 'year': 2010, 'color': 'white'}

# pop() method used to remove item with speicific key
car_dict.pop("color")
print(car_dict)
#{'brand': 'ford', 'model': 'accord', 'year': 2010}

#clear() method empties the dictionary

#Looping the dictionary and getting keys
for x in car_dict:
    print('Looping', x)

'''
Looping brand
Looping model
Looping year
'''
#Looping the dictionary and getting values
for x in car_dict:
    print('Values: ', car_dict[x])

'''
Values:  ford
Values:  accord
Values:  2010
'''

#Looping the dictionary and getting values directly
for x in car_dict.values():
    print('Values:: ', x)

'''
Values::  ford
Values::  accord
Values::  2010
'''
# we can use keys() method to return the keys of a dictionary
#we can use items() method to get the key value pairs

for x,y in car_dict.items():
    print(x, y)


'''
brand ford
model accord
year 2010
'''

#Making copy of a dictionary with copy() method
car_dict_1 = car_dict.copy()
print(car_dict_1)

'''
{'brand': 'ford', 'model': 'accord', 'year': 2010}
'''

#Making copy of a dictionary with dict() method
car_dict_2 = dict(car_dict)
print(car_dict_2)

'''
{'brand': 'ford', 'model': 'accord', 'year': 2010}
'''

car_dict1 = {
    "brand" : "honda",
    "model": "accord",
    "year": 2020
}

car_dict2 = {
    "brand" : "Toyota",
    "model": "Corolla",
    "year": 2021
}

car_dict3 = {
    "brand" : "Ford",
    "model": "F150",
    "year": 2022
}

car_dict = {
    "car1" : car_dict1,
    "car2" : car_dict2,
    "car3" : car_dict3
}

print(car_dict)

'''
{'car1': {'brand': 'honda', 'model': 'accord', 'year': 2020}, 'car2': {'brand': 'Toyota', 'model': 'Corolla', 'year': 2021}, 'car3': {'brand': 'Ford', 'model': 'F150', 'year': 2022}}
'''

#Creating dictionary as single item

car_dict_nested = {
    "car1" : {
        "brand" : "honda",
        "model": "accord",
        "year": 2020
    },
    "car2" : {
        "brand" : "Toyota",
        "model": "Corolla",
        "year": 2021
    },
    "car3" : {
        "brand" : "Ford",
        "model": "F150",
        "year": 2022
    }
}

#Accessing elements of nested dictionary
print(car_dict_nested["car1"]["model"])
#accord

#Looping through nested dictionary is done using items() method

#Getting key value from nested dictionary
for key, obj in car_dict_nested.items():
    for item_key, item_value in obj.items():
        print(item_key, " : ", item_value)

'''
brand  :  honda
model  :  accord
year  :  2020
brand  :  Toyota
model  :  Corolla
year  :  2021
brand  :  Ford
model  :  F150
year  :  2022
'''