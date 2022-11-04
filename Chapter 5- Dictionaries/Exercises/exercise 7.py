#Exercise 7: Rename key of a dictionary

the_dict = {
    "name": "Zoraiz",
    "age": 19,
    "salary": 0,
    "city": "Sharjah"
}

the_dict['location'] = the_dict.pop('city')
print(the_dict)