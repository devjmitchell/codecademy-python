# the 'in' operator
# this script will print each key and its value (each pair will be on a new line)

my_dict = {
    "Name": "Jason",
    "Age": 31,
    "Citizen": True
}

for key in my_dict:
    print key, my_dict[key]
