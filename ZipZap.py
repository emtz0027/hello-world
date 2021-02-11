#Estephania Martinez
#02/04/21
#in-class
#will determing if the number given is divisible by 5 or 7

def ZipZap(n):
    #if the number is divisible by both 5 and 7
    #ZipZap will be returned
    if n%5 == 0 and n%7 == 0:
        print("ZipZap")
    #if the number is only divisible by 5
    #Zip will be returned
    elif n%5 == 0:
        print("Zip")
    #if the number is divisible by 7
    #Zap will be returned
    elif n%7 == 0:
        print("Zap")
    #if the number sin't divisible by 5 and 7
    #the number will be returned
    else:
        print(n)
