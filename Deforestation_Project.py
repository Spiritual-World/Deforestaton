import sys
# The Program Starts here..
def Afforestation_or_Deforestation(First_Year,Last_Year):
    if First_Year > Last_Year :
        print("DEFORESTATION has occured")
    elif Last_Year > First_Year :
        print("Congratulations! AFFORESTATION has occured")
    else :
        print("There has been no AFFORESTATION or DEFORESTATION")
        

def RateOfChange(Data1,Data2,Year1,Year2):
    RateOfChange = ((Data2 - Data1)/Data1) * 100
    if RateOfChange > 0 :
        print("The Rate of AFFORESTATION from",Year1,"to",Year2,"is",RateOfChange,"%")
    elif RateOfChange < 0 :
        print("The Rate of DEFORESTATION from",Year1,"to",Year2,"is",-1 * RateOfChange,"%")
    else :
        print("There has been no change from",Year1,"to",Year2)
        

def CheckUP(Data1,Data2,Data3,Data4,Data5,Data6,Data7,Data8,Data9,Data10):
    if Data1 <= 0 or Data2 <= 0 or Data3 <= 0 or Data4 <= 0 or Data5 <= 0 or Data6 <= 0 or Data7 <= 0 or Data8 <= 0 or Data9 <= 0 or Data10:
        print("SORRY, THIS IS NOT A FOREST")
        print("           END OF PROGRAM          ")
        sys.exit()
    else :
        print("                   YOUR FOREST RESULTS :               ")
Forest_Name = input("Enter the Forest Name : ")
print("Enter the number of trees in",Forest_Name,"in Year 1")
Data1 = int(input("Input it here -> "))
Data2 = int(input("Enter the number of trees in Year 2 : "))
Data3 = int(input("Enter the number of trees in Year 3 : "))
Data4 = int(input("Enter the number of trees in Year 4 : "))
Data5 = int(input("Enter the number of trees in Yea4 5 : "))
Data6 = int(input("Enter the number of trees in Year 6 : "))
Data7 = int(input("Enter the number of trees in Year 7 : "))
Data8 = int(input("Enter the number of trees in Year 8 : "))
Data9 = int(input("Enter the number of trees in Year 9 : "))
Data10 = int(input("Enter the number of trees in Year 10 : "))

CheckUP(Data1,Data2,Data3,Data4,Data5,Data6,Data7,Data8,Data9,Data10)

print("                   The",Forest_Name,"                   ")
Afforestation_or_Deforestation(Data1,Data10)
print("Note : We have compared first year with last year")
""" By Applying Rate of change formulae we have done the following ...
Formulae - Rate of Change = (V2 - V1)/V1 * 100 """
RateOfChange(Data1,Data2,"Year 1","Year 2")
RateOfChange(Data2,Data3,"Year 2","Year 3")
RateOfChange(Data3,Data4,"Year 3","Year 4")
RateOfChange(Data4,Data5,"Year 4","Year 5")
RateOfChange(Data5,Data6,"Year 5","Year 6")
RateOfChange(Data6,Data7,"Year 6","Year 7")
RateOfChange(Data7,Data8,"Year 7","Year 8")
RateOfChange(Data8,Data9,"Year 8","Year 9")
RateOfChange(Data9,Data10,"Year 9","Year 10")
print("OVERALL RATE OF CHANGE IN TEN YEARS")
RateOfChange(Data1,Data10,"Year 1","Year 10")
print("              END OF PROGRAM                     ")







