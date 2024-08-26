import json

x = '{"name":"Raja", "age":"30"}'

#JSON to python dictionary

y= json.loads(x)
print(y)

'''
{'name': 'Raja', 'age': '30'}
'''
# Accessing an value of key

print(y['age'])
#30

#Converting from Python object to json 

car_dict = {
    "brand" : "ford",
    "model": "accord",
     "year": 2000,
}

z = json.dumps(car_dict)
print(z)

'''
{"brand": "ford", "model": "accord", "year": 2000}
'''

z = json.dumps(car_dict, indent=4)
print(z)

'''
{
    "brand": "ford",
    "model": "accord",
    "year": 2000
}
'''
#Use Sort_keys parameter to specify if the keys to be sorted or not

car_dict = {
    "year": 2000,
    "brand" : "ford",
    "model": "accord"
}

z = json.dumps(car_dict, sort_keys=True)
print(z)

#{"brand": "ford", "model": "accord", "year": 2000}
