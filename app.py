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

bill = 99.99
print (bill)
tipoptions = [0, 10, 20, 25, 50, 75, 100]
servicefeedback = ["bad", "okay", "good", "great", "amazing"]
servicefeedback = input("your bill is $99.99, how was your service")
if servicefeedback == "bad":
       print("i hate you dude i work my ahh off just to ensure that you can have nice service, but people like you are the reason the world is becoming worse and worse. I hate you so much")
if servicefeedback == "okay":
        print("ok, now you are adding 10 percent extra, here is your new total")
        print(bill*1.1)
if servicefeedback == "good":
        print(bill*1.2)