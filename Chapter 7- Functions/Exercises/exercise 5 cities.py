def describe_city(city, country='Pakistan'):
    msg = city.title() + " is in " + country.title() 
    print(msg)

describe_city('Kashmir')
describe_city('Gilgit')
describe_city('Venice' , 'Italy')