movies = {
    "Finding Dory": [3,3],
    "Avengers": [18,3],
    "Rio": [5,3],
    "Up": [7,3]
    }

print (movies)

while True:

    choice = input("Welcome to the Cinema, please enter your choice:").strip().title()

    if choice in movies:
        age = int(input("What is your age?:").strip())

        if age >= movies[choice][0]:
            num_seats = movies[choice][1]
            if num_seats > 0:
                movies[choice][1] = movies[choice][1] - 1
                print("Please enjoy your movie")
            else:
                print ("Seats sold out!")
                
        else:
            print("You are not old enough for the movie")

            
            
    else:
        print( " movie is not available")
            
    

    
