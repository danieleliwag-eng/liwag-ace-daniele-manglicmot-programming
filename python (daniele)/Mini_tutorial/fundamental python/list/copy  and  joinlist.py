#copy list
# it can return the new list and wont chenge the variable of the original list
superhero=["captain america", "blackwidow", "iron man","daniele"]
superhero.copy()
print(superhero)


# list : To represent the return of the original variable of the array 
NBA=["stephen curry", "lebron james","james harden ","seth curry"]
mylist=list(NBA)
print(NBA)

#slice operator
NBA=["stephen curry", "lebron james","james harden ","seth curry"]
mylist =NBA[:]
print(mylist)

# join list
NBA=["stephen curry", "lebron james","james harden ","seth curry"]
WNBA=["kelsey plum", "candance parker","sabrina lonescu","diana taurasi"]
Genderbasketballplayer = WNBA+NBA
print(Genderbasketballplayer)

# extend() by using the join list of built in method
marvel=["ironman","Hulk","widow","captain america"]
DCcomics=["superman","wonderwoman","shazam","Black adam"]
marvel.extend(DCcomics)
print(marvel)









#deep copy(* a copy whose properties do not share the same references (point to the same underlying values) as those of the source object from which the copy was made*) vs shallow copy(*a copy whose properties share the same references (point to the same underlying values) as those of the source object from which the copy was made*)
#shallow (copy.copy()) and deep (copy. deepcopy ()) 
#syntax: 
import copy

a = [[1, 2, 3], [4, 5, 6]]

# Creating a deep copy of the nested list 'a'
b = copy.deepcopy(a)

# Modifying an element in the deep-copied list
b[0][0] = 99 
print(b) 



