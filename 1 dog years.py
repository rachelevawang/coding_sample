'''this is a program to convert human years into dog years
developed by XW STUDIO'''

# asks the user to input the age of their dog

# convert dog years into human years

# display output

print("Hello! This is a program to determine how old you would be if you were a dog.")
 
age = int(input("How old are you?"))

if age <= 15:
    dog = 1

elif age <= 24:
    dog = 2

elif age > 24:
    dog = 2 + (age - 24) * 5

if dog <= 2:
    print("Aw! You are only " + str(dog) + " years old. Still a puppy!")
elif dog <= 7:
    print("Amazing! You are a dog in the prime age of " + str(dog) + ". Way to go!")
elif dog <= 13:
    print("You are an old dog now. But you have " + str(dog) + " years of wisdom to look back upon!")
else:
    print("Oops! I'm afraid you have lived past most dogs. You would be " + str(dog) + " years old.")
    
    
