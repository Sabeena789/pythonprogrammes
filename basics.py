#strings
#it can be single line,double line,multiline comments
"""
a='hannu'
print(type(a))
#string indexing support both poitive and negative indexing
##memnership operartor#not in
#the start index o and the end index with n-1
#space is also calculate
#negative index wnt have n-1

a="hannu fathima"
print(a[3:11])
print(a[:8])
b = "Hello,World!"
print(len(b))
print(b[-2:])
print(b[2:-5])
#print(b[-3:-9])
#to add or concadination used to join the strings
s="sabeena" + "johny"
print(s)
#modify string
s="hannu"
print(s.upper())
s="FATIMA"
print(s.lower())
x="johny"*5
print(x)
#for repetation of the string"need to discuss"

#we cannot delete the string
#To add a space between them, add a " ":
a="sabeena"
b="johny"
x=a +" "+b
print(x)

x="hai\n" \
  "hello\\n" \
  "h wr\t u"
print(x)
"""
###################LIST###########################
"""
x=[]
print(x)

#Lists are used to store multiple items in a single variable.
#allows duplicate values
#they follow order
x=["apple","ball",12,"cat","apple"]
print((x))
#acess items start with 0
y=["apple","ball",12,"cat","apple"]
print(y[3])
#negative indexing
z=["apple","ball",12,"cat","apple"]
print(z[-3])
#Range of Indexes 0 to n-1
b=["apple","ball",12,"cat","apple","don","hannu","johny","ammu"]
print(b[3:8])
x=["apple","ball","cat","box","cat","man"]
print(x[:-3])
print(x[3:])
#change the list & range of items with index values
x=["apple","ball","cat","box","cat","man"]
#x[2]="fox"
#print(x)
x[3:5]=["mat","cat"]
print(x)
#Insert Items without replacing any of the existing values, we can use the insert() method.
b=["apple","ball",12,"cat","apple","don","hannu","johny","ammu"]
b.insert(3,"dil")
print(b)
#add list items we use append method
b=["apple","ball",12,"cat","apple","don","hannu","johny","ammu"]
b.append("orange")
print(b)
#removelist items
b=["apple","ball",12,"cat","apple","don","hannu","johny","ammu"]
b.remove(12)
print(b)
#to remove specific index we use pop()
#The pop() method removes the specified index.
b=["apple","ball",12,"cat","apple","don","hannu","johny","ammu"]
b.pop(3)
print(b)

#list in list\
#a=[['cat',"bat"],[10,20,30,40],[30,20,50],["hai","hello"]]
#print(a[:-3])
#change a list
b=[10,20,30,"hai"]
b[1]="hello"
print(b)
x="apple" in ["hai","hello","apple","man"]
print(x)
x="banana" in ["hai","hello","apple","man"]
print(x)
for i in range (4):
    print(i)
x=[0,1,2,3]
for i in x:
    print(i)
#even
x=list(range(0,100,2))
print(x)

#If you do not specify the index, the pop() method removes the last item.
b=["apple","ball",12,"cat","apple","don","hannu","johny","ammu"]
b.pop()
print(b)
#The del keyword also removes the specified index:neeed to check
b=["apple","ball",12,"cat","apple","don","hannu","johny","ammu"]
b.del[4]
print(b)
#clear
b=["apple","ball",12,"cat","apple","don","hannu","johny","ammu"]
b.clear()
print(b)
#sort() method that will sort the list alphanumerically, ascending,
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
#reverse method will help to order in descending order
x=['orange','apple','hai','mango','ball','hello']
x.sort(reverse=True)
print(x)
x=[29,45,255,89,1,7,0]
x.sort(reverse=True)
print(x)

#Use the extend() method to add list2 at the end of list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

# iterating a list  
list = ["John", "David", "James", "Jonathan"]      
for i in list:     
    # The i variable will iterate over the elements of the List and contains each element in each iteration.       
    print(i)  

#in and not in operators
"apple" in ["hai","hello","apple","man"]
"""
################################################SETS#########################################
myset={"apple","man"}
print(type(myset))

#Sets are used to store multiple items in a single variable.
#Sets are unordered, so you cannot be sure in which order the items will appear.
#Duplicates Not Allowed
#length of set
s={"apple","banana","orange","hello"}
print(len(s))
set1 = {"abc", 34, True, 40, "male"}
print(set1)
######acess items############
s={"apple","banana","orange","hello"}
for i in s:
    print(i)
x={"apple","banana","orange","hello"}
print("banana" in x)
#Change Items
#we cannot change the items in sets but we can add the items in sets
x={"apple","banana","orange","hello"}
x.add("sabeena")
print(x)
#To add items from another set into the current set, use the update() method.
#set 2 will update in set1
set1 = {"abc", 34, True, 40, "male"}
x={"apple","banana","orange","hello"}
set1.update(x)
print(set1)
#The object in the update() method does not have to be a set,
#it can be any iterable object (tuples, lists, dictionaries etc.)
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)
#remove sets we use remove(),discard(),pop()
x={"apple","banana","orange","hello"}
x.remove("apple")
print(x)
x.discard("hello")
print(x)

#y=x.pop("orange")
#print(y)
#Remove a random item by using the pop() method:

#The del keyword will delete the set completely:
#x={"apple","banana","orange","hello"}
#y=delete(x)
#print(y)

#Join Two Sets 1.unino(),2.update()
thisset = {"apple", "banana", "cherry"}
mylist = {"kiwi", "orange"}
thisset.update(mylist)
print(thisset)
thisset = {"apple", "banana", "cherry"}
mylist = {"kiwi", "orange"}
set=thisset.union(mylist)
print(set)
##############################################dictionary#############################################
#Dictionary is a collection of key:value pairs.
#which is ordered*, changeable and do not allow duplicates.
#Dictionaries are written with curly brackets, and have keys and values:
x={"name":"hannu","age":9,"school":"andrews"}
print(x)
#acess th eitem
#x={"name":"hannu","age":9,"school":"andrews"}
#z=x["age"]
#print(z)
#y=x.keys("age")
#print(y)
#only return keys and  values
x={"name":"hannu","age":9,"school":"andrews"}
s=x.keys()
print(s)
c=x.values()
print(c)

#Add a new item to the original dictionary, and see that the items list gets updated as well:
x={"name":"hannu","age":9,"school":"andrews"}
d=x.items()
x["sister"]="ammu"
print(x)
if "sister" in x:
    print("yes")
#Change Values
#You can change the value of a specific item by referring to its key name:
x={"name":"hannu","age":9,"school":"andrews"}
x["name"]="khaja"
x.update({"name":"mohit"})
print(x)
#remove items
#pop,del,clear,pop items
x={"name":"hannu","age":9,"school":"andrews"}
x.pop("age")
print(x)
#will remove last key value
y={"name":"hannu","age":9,"school":"andrews"}
#y.popitem()
#print(y)
#y.clear()#shows empty dic
#print(y)
del y["school"]
print(y)
#loops
#prints only key
y={"name":"hannu","age":9,"school":"andrews","home":"sec"}
#for i in y:
for i in y.keys():
    print(i)
#print only values
z={"name":"hannu","age":9,"school":"andrews","home":"sec"}
#for i in z:
   # print(z[i])

#for i in z.values():
#for both key and values
z={"name":"hannu","age":9,"school":"andrews","home":"sec"}
for i, j in z.items():
    print(i,j)
# copy directory
z = {"name": "hannu", "age": 9, "school": "andrews", "home": "sec"}
sabeena = z.copy()
print(sabeena)
#Nested Dictionaries
#A dictionary can contain dictionaries, this is called nested dictionaries.
x={"hannu":{"nikname":"khaja","school":"andrews"},"fathima":{"nikname":"ammu","school":"littleflower"},"aahil":{"nickname":"pandu","school":"army"}}
print(x)
######################################################tuple##########################################################
x=("apple","banana","pineapple")
print(type(x))
z= ("apple", "banana", "cherry", "apple", "cherry")
print(len(z))
c=("apple")
print(type(c))
d=("apple",)
print(type(d))
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)
#Access Tuple Items
#You can access tuple items by referring to the index number, inside square brackets:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])
#Range of Negative Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
#Check if Item Exists
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#Change Tuple Values
#Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
#You can convert the tuple into a list, change the list, and convert the list back into a tuple.
x = ("apple", "banana", "cherry")
y = list(x)
print(y)
y[1]="kiwi"
x=tuple(y)
print(x)

s= ("hannu","ammu","dil","johny")
d = list(s)
print(d)
d.append("sabeena")
s=tuple(d)
print(s)
#You can loop through the tuple items by using a for loop.
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#join method,tuple with while loop

output=subprocess.run("ipconfig",capture_output=True)
print("command output",output)
