# if statement
# if age < 18:
#     print("Still growing")
# elif age >=18 and age <21:
#     print("You are an adolescent") 
# else:
#     print("You're an adult")

# for loop
# users = ["lucky","wami","taburu"]

# for user in users:
#     print(user)

# while loop
# age = 10

# while(age<15):
#     if (age %2) ==0:
#      print(age)
#     age +=1

# user=["badboy Tim","Seniorman Alex","Caleb Large","Covidful","badman Dafe","Sexofia"]

# index = 0
# length=len(user)

# while index < length:
#     print(user[index])
#     index +=1



value1=input("Please enter any value:\n")
value2=input("Please enter another number:\n")
print("") 

print("You have entered  " +  str(value1)+ " and " + str(value2))
print("")

choice=input("Please enter 1 if you want to add\n"+" or enter 2 if you want to subtract \n"+" or enter 3 if you want to multiply\n"+"or enter 4 if you want to divide. \n")

if choice == 1:
    answer=value1+value2
    print("The answer is "+ str(answer))
elif choice == 2:
    answer=value1-value2
    print("The answer is "+ str(answer))
elif choice == 3:
    answer=value1*value2
    print("The answer is "+ str(answer))
elif choice == 4:
    answer=value1/value2
    print("The answer is "+ str(answer))
print("")
print("Thank you. This is the end of the program")
print("")


