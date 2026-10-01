""" #string for characters
name = "Dev"
print("X".isupper())
#input asks the user a question and records the answer
#what we write in input argument is what user sees
bill = input("How much was the bill")
#input always outputs a string
print(bill)
#integer uses whole numbers
input(99.99)
#Float uses decimals
amt = 99.99
servicefeedback = print("How was your experience?")
servicefeedback = input("amazing")
if servicefeedback == input("amazing"):
        tipoptions = print("Wow thank you! Would you likem to leave a tip of 25%?")
        input("of course")
        if tipoptions == ("of course"):
                bill = (amt*1.25)
        else: print("DUDE YOU HAD AN AMAZING EXPERIENCE JUST TIP")
        input("nah")
servicefeedback = input("good")
if servicefeedback == "good":
        tipoptions = input("Thank you!, do you want to tip?")
        input("yes")
        if tipoptions == "yes":
                x = 1.10
                print("Okay, do you want to tip 10%?")
                input("yes")
                bill = (amt*10)
        else: print("man screw you") 
servicefeedback = input("bad")
if servicefeedback == "bad":
        print("What was wrong with your experience?")
        input("too expensive")
        print("I hate you dude, i work 80 hours every week just for you to say you had a bad experience")
#BooLean
#x = True
#y = False """

""" bill = 99.99
print (bill)
tipoptions = [0, 10, 20, 25, 50,]
servicefeedback = ["bad", "okay", "good", "great", "amazing"]
servicefeedback = input("your bill is $99.99, how was your service")
if servicefeedback == "bad":
       print("i hate you dude i work my ahh off just to ensure that you can have nice service, but people like you are the reason the world is becoming worse and worse. I hate you so much")
if servicefeedback == "okay":
        print("ok, now you are adding 10 percent extra, here is your new total")
        print(bill*1.1)
if servicefeedback == "good":
        print("ok, now your bill has a 20 percent tip added, here is your new tip")
        print(bill*1.2)
if servicefeedback == "great":
        print("Thanks! Your bill has a 25 percent tip added, here is your new total")
        print(bill*1.25)
if servicefeedback == "amazing":
        print("Wow! Thank you so much, your total now has a 50 percent tip added to it, here is your new total")
        print(bill*1.5) 
 """
""" numberinput = input("Input number: ")
number = int(numberinput)
if number % 2 == 0:
    print("even")
else:
    print("odd") """


""" numberinput = int(input("Input number"))
factors = []
for i in range(1, numberinput, 1):
        if numberinput % i == 0:
                factors.append(i)
                print(f"The factors of {numberinput} are {factors}") """

""" def spaces(n, y, t):
        occupied = 0
        for i in range(n):
                if y[i] == "C" and t[i] =="C":
                        occupied = occupied+1
                        return occupied
spaces(5, "CC..C", ".CC..") """

def GCF(num1, num2):
    num1 = input("enter first number")
    num2 = input("enter second number")

    print("the GCF of", num1 "and", num2+)