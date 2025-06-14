'''append,insert,pop,remove,indexing'''


cartoons=['Tom & Jerry','Tom & Jerry','Doremon','shinchan','Oggy & cockroach']
print(cartoons)
print("After Appending:")
cartoons.append('Heidi')
print(cartoons)
#add another 3 element
cartoons.append('Horrid Henry')
print (cartoons)
cartoons.append('Roll no.21')
print (cartoons)
cartoons.append('Chota bheem')
print (cartoons)
cartoons.insert(0,'motu pathulu')
print(cartoons)
cartoons.pop()
print (cartoons)
cartoons.pop(4)
print (cartoons)
cartoons.remove('Tom & Jerry')
print (cartoons)
print(cartoons.index('Doremon'))
