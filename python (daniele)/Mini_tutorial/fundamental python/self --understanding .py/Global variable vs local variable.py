#local vs global variable
# local:variable declared inside a function or a specific block of code
# Global : is a variable declared outside of any function, class, or block of code, giving it a scope that is accessible from anywhere within the program

#example
def subject():
   # Local variable
   chinese_language= "Cantonese"
   print(chinese_language)

# example
def subject():
   # local variable
      
   English_language="english literature"
   print(English_language)
   # global variable
subject()

# tutorial by youtuber
x = 0
def number():
   x = 4
print(x)
number()
print(x)

x = 0
def foo():
   # global keywords
   global x 
   x =2
   def bar():
      x = 7
      print(x)
   bar()
   print(x)
foo()
print()

# self test of global variable by using your own knowledge
personal_name=["liwag","ace","daniele","manglicmot"]
def perosnalityname(personal_name):
   personal_name = "liwag"
print(personal_name)
perosnalityname()
 
