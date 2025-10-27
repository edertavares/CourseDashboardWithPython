""" def welcome(): # Function to print a welcome message
    print("Welcome to the Course Dashboard!")

for i in range(20):
    welcome() """

def average_calculate(): # Function to calculate the average of notes movies
    num_ratings = int(input("How many movie ratings do you want to enter?   \n "))
    total = 0
    for i in range(num_ratings):
        rating = float(input(f"Enter rating {i + 1}: "))
        total += rating
    if num_ratings == 0:
        print("No ratings entered.")
        return average 
    else:
        average = total / num_ratings
        #print(f"The average rating is: {average}")
        return average


print(f"The average rating is: {average_calculate():.2f}")