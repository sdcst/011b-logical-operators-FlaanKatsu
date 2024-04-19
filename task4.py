#! python3
"""
Ask the user to enter a name. 
If the name is one of the names on a list of special users, greet them by name.
You will need to use a logical statement that checks to see if any of the names
matches the input name.  Don't be surprised if there are many and/or connectors.

(2 points) 

Inputs:
Name (string)

Outputs:
You are not a VIP.
Hi xxxxxx! You are a VIP!

Example:
Enter your name=>Gertrude
Hi Gertrude! You are a VIP!

Enter your name=>Gordon
You are not a VIP.
"""

VIPNames = ("Guile","Blanka","Christine","Carol","Richard","Daniel","Chun-Li")
name1 = str("Guile")
name2 = str("Blanka")
name3 = str("Christine")
name4 = str("Carol")
name5 = str("Richard")
name6 = str("Daniel")
name7 = str("Chun-li")


Name = str(input("Welsome to Lord Beelzebub's VIP club! Please enter your name: "))
if Name == name1 or Name == name2 or Name == name3 or Name == name4 or Name == name5 or Name == name6 or Name == name7:
    print(f"Welcome, {Name}! You are a VIP!")
else:
    print("Unfortunately, you are not a VIP, and will now be executed.")