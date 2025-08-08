test_list = ['apple', 'banana' , 'kiwi' , 'orange' , 'rugby']
print (test_list)
print (test_list[0])
print (test_list[-1])
print (test_list[-3])
print (test_list[1:3])
print (test_list[:2])
print (test_list[2:4])
if "apple" in test_list:
    print (" the item can be found")

test_list.append ('cookie')
test_list.insert (3,'pads')
print (test_list)


#change item
test_list [3] = "chocolate"
print (test_list)
test_list [0:5]= '1','2','3','4','5'
print (test_list)

# remove item
test_list.remove ('cookie')
print (test_list)
test_list.pop (2)

#copy a list
list_copy = test_list.copy()
print (list_copy)
test_list = "apple","banana","juice"
print (test_list)
print (list_copy)

#concatenate and extend
first_list = "maria","rudolf","max"
second_list = "waqar","umi","ben"
print (first_list)
print (second_list)
print (first_list + second_list)
#extend method

extended_1 = ['today','is','a','good']
extended_2 = ['day','to','be','alive']
#extended_1.extend(second_list)....not working...i figured out my mistake it works
extended_1.extend(extended_2)
print (extended_1)


#sort and reverse
sort_list = ["5","4","2","1","3"]
sort_list.sort ()#parenthesis can be left empty and order will be sorted to normal
print (sort_list)
#reverse
sort_list.reverse()
print (sort_list)


#Count and index
count_test = ['cocnut','banana','coconut','banana','kiwi']
count_test.count ('banana')
print (count_test.count ('banana'))
#index
count_test.index ('kiwi')
print (count_test.index('kiwi'))

#n.12 list comprrehension (Bonus) --i'll skip this part i dont really understand it yet
































