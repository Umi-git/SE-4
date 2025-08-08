#create a Tuple
my_tuple = '1', '2','ananas','banana'
#print the tuple
print (my_tuple)
#print first item index 0
print (my_tuple[0])
#print last item index -1
print (my_tuple[-1])
#slice the tuple-print from start to certain index--print middle items--print certain index till end
print (my_tuple [0:3], [-3], [-2], [1-3])
#check if an item exist
if 'banana' in my_tuple:
    print ('banana can be found in tuple') 
    
 #count and index
print (my_tuple.count('banana')) #use count method to detrmine how many times a specific value is in the tuple
print (my_tuple.index ('1'))#use index method to determine position of first occourence in value

#packing and unpacking ( a tuple is already packed by assigning multiple values to the tuple my_tuple)
#unpacking means to separate tuples in separate variables so that each variable corresponds to an item in the tuple.
a,b,c,d=my_tuple
print (a)
print (b)
print (c)
print (d)
#asterisk unpacking scenario
asterisk_tuple_unpacking = 'quads','tights','1','2'
e, *g = asterisk_tuple_unpacking
print (e)
print (g)

#joining tuples
another_tuple = 'olo','06','08','august'
#join using operator
print (my_tuple + (another_tuple)) #works
#multiply one of your tuples by an integer and print the result.

tuple_multiplication = another_tuple* 10
print (tuple_multiplication)

#end






