#Excercise 8: Get the key of a minimum value from the following dictionary

the_dict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}
print(min(the_dict, key=the_dict.get))