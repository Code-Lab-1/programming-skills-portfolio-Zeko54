rivers = {
    'amazon ' : 'brazil',
    'chenab ' : 'pakistan',
    'nile' : 'egypt',
    'Yangtze': 'china',
    'volga ': 'russia',
}

for river,countries in rivers.items():
  print('The ' + river.title() + " Flows through " + countries.title())

print("\nThe following rivers are included in this dictionary:")
for river in rivers.keys():
  print('*' + river.title())

print("\nThe following countries are include in this dictionary:")
for countries in rivers.values():
  print('*' + countries.title())