#-----Juicy part of the program------#

def main():
    userinput = int(input("How many times should the cat meow? ")) #Requests user input and only access numbers
    meow(userinput) #calls meow() which is defined below.


#-----Function Definition Space-----#

#meow() function definition
def meow(n):
    for i in range(n): #Loops through n-times. n is dynamic, set by the user input defined in main()
        print("meow")


#-----------Call main()------------#
main()
