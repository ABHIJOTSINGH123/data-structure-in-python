#empty dictionary
mydictionary={}
#adding elements to the dictionary
mydictionary={1:"apple", 2:"orange", 3:"banana"}
#second dictionaty
mydictionary={'name':'ABHIJOT SINGH',1:[2,4,3]}
#third dictionary
mydictionary={'age':'45','name':'JHONY'}
print(mydictionary)
print(mydictionary['name'])
print(mydictionary['age'])
mydictionary['age'] = 50
print(mydictionary)
#add
mydictionary['address']='punjab,sri muktsar shaib'
print(mydictionary)
# pop
mydictionary.pop('age')
print(mydictionary)
print("address",mydictionary.get("address"))
mydictionary.clear()
print(mydictionary)