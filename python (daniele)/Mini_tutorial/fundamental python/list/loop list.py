# syntax
# list = [store the variable in the data type of the ]
# loop list
# meanning : iterating over each element within a list

a =['apple','banana','cherry','blueberry']
for i in a :
    print(a)

#Loop Through the Index Numbers
# range() and len()
# meanning : generates index numbers. data[i] fetches the character at each index.
# *unseen : enumerate()*
# enumerate(data) yields (index, value) pairs automatically. No need to manually calculate the index.
# list comprehension
# meanning :is a way to create lists using a concise syntax.  
# method 1
a = [
    'apple','banana','cherry','strawberry'
]
for i in range(len(a)):
    print(a)


# example of enumerate
NBA=['curry','lebron james','james harden']
for i in enumerate(NBA):
    print(NBA)

# using list comprehension
# list
programminglanguage=['HTML','css','python']
# for loops
for i in programminglanguage:
    print(programminglanguage)
 
# combine
[print(programminglanguage) for i in programminglanguage]

# example tutorial by youtuber
Fruit=['apple' ,'cherry','strawberry']
for i in Fruit:
    Fruit.lower()
print(Fruit)

# tricky one
fruits=['banana','apple','watermelon']
new_fruits=[]
for fruit in fruits:
    fruit = fruit.upper()
    new_fruits.append(fruit)

fruits = new_fruits
print(fruit)

# example 2
personal_name=['liwag','ace','daniele',"manglicmot"]
[personal_name.upper() for personal_name in personal_name]
print(personal_name)

#conditional statement of list comprehension
bits = [False , True , False , True]
# create the empty list to stores the result to get the new variable of the list
new_bits=[]

for i in bits:
        if i == True:
            new_bits.append(1)
        else:
            new_bits.append(0)
            super_bits=[1 if b == True else 0 for b in bits]
print(bits)
print(new_bits)
print(super_bits)

#string manipulation of list comprehension
my_string = "my name is liwag ace daniele manglicmot"
my_string = [ i for i in my_string]
print(my_string)

#example 2
my_string="Liwag ace daniele manglicmot"
my_string="".join([i for i in my_string])
print(my_string)

my_string="liwag ace daniele manglicmot"
my_string="".join([ i if i.islower() else "" +  i for i in my string])[:1]
#slice end index



# tutorial by the (portfolio youtube)
#loop through list from while loop
# step
        
     # [0,1,2,3,4] <- #indexes
data=[5,6,7,8,9]
#for item in data:
    #print(item)
i = 0
while #conditon  :
    data[i]
    i=+1

#method 2
data=[5,6,7,8,9]
i=0
while i < len(data):
    print(data[i])




 














    






