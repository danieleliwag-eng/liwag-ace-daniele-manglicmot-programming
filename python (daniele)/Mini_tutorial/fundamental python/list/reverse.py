# sort descending
a=['a','b,','c']
a.sort(reverse='true')
print(a)
#Sort List Alphanumerically
a=['a','b,','c']
a.sort()
print(a)
#reverse order
a =['liwag','ace','daniele','Manglicmot']
a.reverse()
print(a)

# delcare function and 
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]

thislist.sort(key = myfunc)

print(thislist)
