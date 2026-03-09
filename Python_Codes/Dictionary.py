intro={
    "name": "johny",
    "age":"28",
    "favourite_play": "cricket",
        "foods":["juice","bread"]
}

print("Name :",intro["name"])
print("Age :",intro["age"])

intro["favourite_play"]="football"
print(intro)

intro["phone"]="123 456 789"
print(intro)

intro.pop("age")
print(intro)

for key,value in intro.items():
    print(f"{key.upper()}:{value}")


guests={
    "guest_1":{"name":"arjun","color":"black"},
    "guest_2":{"name":"babu","color":"white"}
}

print(guests["guest_1"]["name"])

for guest_id, details in guests.items():
    print(guest_id,"-",details["name"],"likes",details["color"])
