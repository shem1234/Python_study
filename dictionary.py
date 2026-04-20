my_dictionary={
    "Name":"Shem Gichimu",
    "Gender":"Male",
    "Age": 25,
    "City":"Nairobi",
    "Location":{"Postal code": "00100","Town": "Kiambu"}
}

# access values in a dictionary
print(my_dictionary)
print(type(my_dictionary))
print(my_dictionary["Age"])

# to update and add
my_dictionary["Age"]=40
my_dictionary["City"]="Mombasa"
my_dictionary["Occupation"]="Programmer"
print(my_dictionary)

# dictionary methods
my_dictionary["Hobbies"]=["Swimming","Dancing","Reading"]
print(my_dictionary)
print(my_dictionary["Hobbies"][1])