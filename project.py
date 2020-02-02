#Import 'sys' to catch errors!
import sys

#'colors' to show them in terminal
class colors:
    Black="\033[0;30m"
    RedBold="\033[1;31m"
    GreenBold="\033[1;32m"
    Yellow="\033[0;33m" 
    BlueBold="\033[1;34m"   
    PurpleBold="\033[1;35m" 
    CyanBold="\033[1;36m"
    Reset = "\033[0;0m"

#Show Welcome Message
print(f"{colors.BlueBold}Welcome To My Simple Calc!\n(Type 'Done' After Finish){colors.Reset}")

#'done' is empty to keep loop working
done = ""

#The wile loop
while done.lower() != "done" :

#trying to cath erros
    try :

#'float' to convert input type from words to numbers
        firstnumber = float(input(f"\n{colors.PurpleBold}First Number: {colors.Reset}"))
        secondnumber = float(input(f"{colors.PurpleBold}Second Number: {colors.Reset}"))

#this to select operator
        userselection = input(f"\n{colors.CyanBold}What Operator you want to use ?: {colors.Reset}")

#if statment to calculate user input
        if userselection == "+" :
            print(f"\nYour Numbers Are: {colors.GreenBold} {firstnumber + secondnumber} {colors.Reset}")
        elif userselection == "-" :
            print(f"\nYour Numbers Are: {colors.GreenBold} {firstnumber * secondnumber} {colors.Reset}")
        elif userselection == "*" :
            print(f"\nYour Numbers Are: {colors.GreenBold} {firstnumber - secondnumber} {colors.Reset}")
        elif userselection == "/" :
            print(f"\nYour Numbers Are: {colors.GreenBold} {firstnumber / secondnumber} {colors.Reset}")
        else:
            print(f"\n{colors.RedBold}Please Type A Vaild Operator{colors.Reset}")

#'break' means like end to exit app if it caught error
            break

#show message if you typed nonsense things in numbers           
    except ValueError :
        print(f"\n{colors.RedBold}Please Type A Number{colors.Reset}")
        break

#show message if you typed want to divide on 0           
    except ZeroDivisionError :
        print(f"\n{colors.RedBold}Really ?{colors.Reset}")

#show error name in case user got new error!
    except:
        error = sys.exc_info()
        print(f"\n{colors.RedBold}Seems you got an error! {error}{colors.Reset}")
        
print(f"{colors.BlueBold}\nThanks For Using My App! :-){colors.Reset}")

