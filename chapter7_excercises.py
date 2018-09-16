#Excercise with slicing
months = "JanFebMarAprMayJunJulAugSepOctNovDec"
n = int(input("Enter a month number (1-12): "))
print ("You chose month: ", months[(n*3)-3:n*3])
