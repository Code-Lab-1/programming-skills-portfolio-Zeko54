pets=[]

pet={ 'animal': 'cat',
      'name' : 'tom',
      'owner' : 'zoraiz',
      'food' : 'tuna'
    }

pets.append(pet)

pet={ 'animal': 'dog',
      'name' : 'jake',
      'owner' : 'ahmed',
      'food' : 'meat'
    }

pets.append(pet)

for pet in pets:
    print("\nHere's what I know about " + pet['name'].title())
    for key, value in pet.items():
        print("\t" + key + " : " + value)
