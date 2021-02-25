import config


def globalsing():
    x = input("Type Number: ")
    config.globus = x
    Savinging()

def Savinging():
    SV = open("IDK testing globals.txt","w")
    SV.write(config.globus)
    exit

globalsing()