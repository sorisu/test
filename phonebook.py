#-----------Dependencies-------------#
import csv


#-----Juicy part of the program------#
def main():
    name = input("Name: ")
    number = input("Number: ")

    updatePhonebook(name, number)

#-----Function Definition Space-----#

def updatePhonebook(name, number):
    with open("phonebook.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow([name, number])

#-----------Call main()------------#
if __name__ == "__main__":
    main()