USCities =["Oakland", "Atlanta", "New York City", "Seattle", "Memphis", "Miami", "Boston", "Los Angeles", "Denver", "New Orleans"]
print (USCities)

best_fruit = ["apple","orange","grape","banana","kiwi","strawberry","mango","blueberry","watermelon","peach"]
print (best_fruit[0])

print (USCities[2])
print (USCities[4])
print (USCities[6])

print (best_fruit[1])
print (best_fruit[3])
print (best_fruit[5])

fav_cities = USCities[0:3]
fav_fruit = best_fruit[7:10]

print(fav_cities)
print(fav_fruit)

USCities [1] = "Orlando"
USCities [0] = "San Fransisco"
USCities [0] = "San Fransisco"
USCities [2] = "Brooklyn"
USCities [7] = "Hollywood"
USCities [5] = "Miami"

print(USCities)

USCities.append("New Jersey")
USCities.extend(["Santa Cruz","Selma","Chicago"])
USCities.insert(7,"Washington,D.C")

print(USCities)

USCities.append("Oakland")
USCities.extend(["New York City","Los Angeles"])
USCities.insert(0,"Miami")

print(USCities)

del USCities[3]
USCities.pop(6)
USCities.remove("New York City")

print(USCities)

del USCities[5]
USCities.pop(2)
USCities.remove("Los Angeles")

print (USCities)