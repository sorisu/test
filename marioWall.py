#-----------Dependancies-------------#



#-----Juicy part of the program------#

def main():
    height = getHeight()
    width = getWidth()
    buildWall(height, width)


#-----Function Definition Space-----#

def getHeight():
    while True:
        try:
            n = int(input("Set wall height: "))
        except ValueError:
            print("Please enter a number")
            getHeight
        else:
            if n > 0:
                return n

def getWidth():
    while True:
        try:
            n = int(input("Set wall width: "))
        except ValueError:
            print("Please enter a number")
        else:
            if n > 0:
                return n

def buildWall(height, width):
    for i in range(height):
        print("#" * width)


#-----------Call main()------------#
main()