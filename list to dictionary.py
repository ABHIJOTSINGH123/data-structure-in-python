def test(mylist):
    result={}
    for item in mylist:
        result[item[0]]=item[1:]
        return result
student=[[1,'Gurinder singh brar',9],[1,'Abhijot singh',9],[1,'karanveer singh cheema',9]]
print("original list of list")
print(student)
print("\nconverted list to dictionary")
print(test(student))