mylist=["apple", "orange", "banana", "burger", "cherry", "cheese"]
#length of list
print("length of the list:",len(mylist))
#first item in list
print("first element:",mylist[0])
#last item in list
print("last element:",mylist[-1])
mylist.append("shardai")
#list of append
print("updated list:",mylist)
mylist.remove("shardai")
#list of remove
print("updated list:",mylist)
#sorting the list in ascending order
mylist.sort()
print("sorted list:",mylist)
#reversing the list
mylist.reverse()
print("reversed list:",mylist)
#pop of list
mylist.pop(2)
print("updated list after popping:",mylist)
#multiply
print("multiplication of list:",mylist*2)
#slice list
mylist=mylist[:3]
print("updated list after slicing:",mylist)
# clear
mylist.clear()
print("updated list after clearing:",mylist)