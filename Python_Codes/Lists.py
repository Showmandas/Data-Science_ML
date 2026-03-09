snacks=['chips','chocolate','biscuits','cake']
print(snacks)

snacks.append("cookies")
print("After adding cookies : ",snacks)

snacks.remove('chips')
print("Chips will be removed : ",snacks)

snacks.sort()
print("Sorted :",snacks)

print("Length of snacks :",len(snacks))
print("Last item :",snacks[-1]) #last item

snacks[2]="juice"
print("After replace 3rd item :",snacks)

snacks.insert(1,"bread")
print("After inserting bread :",snacks)

del snacks[4]
print("After deleting cookies:",snacks)

poppedItem=snacks.pop()
print("Popped item from snacks :",poppedItem)
print("After popping item : ",snacks)

print("After clearing :",snacks.clear()) #clear the list

#nested lists
bags=[
    ["juice","biscuits"],
    ["cake","chips"],
    ["drinks","pizza"]
]

for items in bags:
    for item in items:
        print(item)