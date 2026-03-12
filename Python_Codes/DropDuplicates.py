l1=int(input("Enter number of elements : "))
l2=[]
for i in range(l1):
    user_inp=int(input())
    l2.append(user_inp)
print(l2)
del_duplicate=input("Do you want to delete duplicate with sorted from the list? yes/no: ")
if del_duplicate == "yes":
    print(list(set(l2)))
else:
    print(f"Ok boss! then you can see {l2}")


del_specific_value= input("Do you want to delete specific value from the list? yes/no : ")
if del_specific_value == "yes":
    item=int(input("Which value? : "))
    new_list=[x for x in l2 if x != item]
    print(f"You have deleted {item} from the list : ",new_list)
else:
    print(f"Ok boss! then you can see {l2}")




