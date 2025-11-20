#Scenario:You are a security engineer at a high-tech facility. 
# To enter the building, employees must type in a secret code on a keypad. 
#The code for today is "123". You need to write a program that checks if the person has entered the correct code.
while True:
    code = input("Enter the access code:\n> ")
    if code == "123":
        print("Access granted. Welcome inside!")
        break
    else:
        print("Access denied. Incorrect code.")