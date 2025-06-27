age = int(input("How old are you? "))


if age >= 18:
    
    print("Congratulations! You are eligible to vote. Go make a difference! 🎉")
else:
    
    years_to_wait = 18 - age
    
   
    if years_to_wait == 1:
        
        print(f"Oops! You're not eligible yet. But hey, only 1 more year to go! ⏳")
    else:
        print(f"Oops! You're not eligible yet. But hey, only {years_to_wait} more years to go! ⏳")


print("\nRemember: Every vote counts")