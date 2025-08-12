#Create and Print a Dictionary
myself ={"name":"Umi",
         "age":"31",
         "city":
         "karlsruhe",
         "skill":"runner"}

print (myself)

#Access Dictionary Elements

my_name = myself["name"]
print (my_name)
my_mail = myself.get("email")
print (my_mail)
keys= myself.keys() #parenthesis can be empty if not for a specified value
print (keys)
values = myself.values()
print (values)
items = myself.items()
print (items)


#Check for Key Existence

if "age" in myself:
    print ("age can be found in my library")

#Change and Update Dictionary Elements

myself["city"]= "pretoria"
print (myself)
myself.update({"profession":"student", "hobby": "sports"})
print (myself)
myself.update( {"city": " cape_town" , "profession":"software_engineer"})
print (myself)


# Remove Items from the Dictionary

myself.pop("age")
print (myself)
myself.popitem()
print (myself)
del myself["city"]
print (myself)

#Copy a Dictionary

Dictionary_copy = myself.copy()
Dictionary_copy.update({"favourite_dish": "meat", "quote":"best dad ever"})
print (myself)
print (Dictionary_copy)

#Using setdefault()

new_library = {"age":"71",
               "name":"mario",
               "height":"1.60cm"}
print (new_library)
25 = new_library.setdefault("age":"33")
print (new_library["age"])
