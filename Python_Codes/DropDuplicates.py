l1=int(input("Enter number of elements : "))
l2=[]
for i in range(l1):
    user_inp=int(input())
    l2.append(user_inp)
print(l2)
del_duplicate=input("Do you want to delete duplicate from the list? yes/no: ")
if del_duplicate == "yes":
    print(list(set(l2)))
else:
    print("Ok boss")




