
info=("karim",25,"Bangladesh","Programmer")
another_info=("rahim","26","Australia","Engineer")
#unpack the info variable's values in separate variables

name,age,country,profession=info

print(f"Name : {name}")
print(f"age : {age}")
print(f"Country : {country}")
print(f"Profession : {profession}")

#comparison operators between tuples
comp_tuple=info > another_info
print(comp_tuple)

comp_tuple=info < another_info
print(comp_tuple)

comp_tuple=info == another_info
print(comp_tuple)


#The main difference between list and tuple is mutability. It means List can be changeable, on the other hand Tuple is unchangeable.
