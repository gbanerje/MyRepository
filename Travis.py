known_users = ["name1", "name2", "name3", "name4","name5","name6","name7","name8","name9"]
print(known_users)

while True:
    print ("My name is travis")
    name = input("what is your name?:").strip()
    if name in known_users:
        print ("Hello {}".format(name))
        user_remove = input("Would you like to remove the yourself (y/n)?" ).strip().lower()
        if user_remove == "y":
            print(known_users)
            known_users.remove(name)
            print(known_users)
        elif user_remove == "n":
            print ("Thank you! User is not removed")

    else:
        print ("Hello {}!".format(name))
        user_add = input("Name is not recognized, would you like to add it in database (y/n)?:").strip().lower()
        if user_add == "y":
            print(known_users)
            known_users.append(name)
            print(known_users)
        elif user_add == "n":
            print ("Thank you! User is not added")

