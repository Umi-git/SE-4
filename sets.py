#create a set called fruits
fruits = {"apple", "banana","grape", "melon","lemon"}
#check if banana is in fruits
if "banana" in fruits:
    print ("true")
#Add and Update Items
fruits.add ("pineapple")
print (fruits)
# list will not be updated when a duplicate is added as duplicates are not permitted in sets

#Create another set  with at least 3 unique items.
more_fruits= {"cherry" ,"maracuja" , "mango"}
#update fruits with more fruits with update function
fruits.update( more_fruits)
print (fruits)
fruits.remove("apple")
print (fruits)
#Attempt to remove an element not in the set using discard()
fruits.discard("apple")
print (fruits)
## no errors were outputed after using discard##
fruits.pop()
print (fruits)
fruits.clear()
print (fruits)
#Set Operations
set_a = {"chocolate", "lime", "raspberry", "banana"}
set_b = {"coconut" , "corn" , "tomato", "banana"}
#Union: Use union() to combine set_a and set_b
united_set = set_a.union(set_b)
print (united_set)
#Use intersection() to find common elements between set_a and set_b
common_elements_intersection = set_a.intersection(set_b)
print (common_elements_intersection)
#Use difference() to find elements in set_a not in set_b
difference = set_a.difference(set_b)
print (difference)
#Use symmetric_difference() to find items in either set_a or set_b
symethric_difference = set_b.symmetric_difference(set_b)
print (symethric_difference)

#In-place Set Operations
difference_update = set_a.difference_update(set_b) #remove item that can be found in both sets
print (difference_update)
#intersection update
intersection_update = set_a.intersection_update(set_b)
print (intersection_update)
#update--add items from another set
updated_set= fruits.update(set_b)
print (updated_set)
#Relational Methods
Large_set = {"a" , "b2", "c", "d"}
small_set = {"e" ,"f", "g"}
small_set.issubset(Large_set)
Large_set.issuperset(small_set)

print (Large_set)
#Check if two sets are disjoint using isdisjoint() and print the result.
disjoint_check = Large_set.isdisjoint(small_set)
print(disjoint_check)

