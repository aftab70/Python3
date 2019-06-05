
#!/usr/bin/python3

age = int(input("How old are you ? :"))

if(age>=18):
        print("Go get your beer")

else:
        print("You are under age")
 
##########################################################################################################################################

#!/usr/bin/python3

name = input("Enter your name: ")

if name == "Aftab":
        print("Hello Aftab")
elif name == "Sam":
        print("Hello Sam")
else:
        print("Record not updated..")
        
###########################################################################################################################################

#!/usr/bin/python3

i = 1

while(i<=10):
        print("Hello world")
        i = i+1
print("Executed")

##########################################################################################################################################

#!/usr/bin/python3

def function_name():
        print("functions")
        print("I am working")

function_name()


########################################################################################################################################
#!/usr/bin/python3

try:
        number = int(input("Enter number"))
        n = number + 1
        print(n)
except:
        print("Its seems like you are not enter number")

##########################################################################################################################################

#!/usr/bin/python3

import threading

class Messenger(threading.Thread):
        def run(self):
          for i in range(10):
            print(threading.currentThread().getName())
x = Messenger(name="Sending Messeges")
y = Messenger(name="Recived Messsages")
x.start()
y.start()

#########################################################################################################################################







