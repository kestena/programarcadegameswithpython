#I am not sure if this is the correct way to be done
#but apparently it is working for any inputed number
#provided it is an int. I'm not yet there to ask the
#user for only specific numbers. This will come.
#I based my program on the example given not in the 
#assignment but in the building area.

'''
Create a big box out of n rows of little o's for any desired size n. Use an input statement to allow the user to enter the value for n and then print the properly sized box.

E.g. n = 3
oooooo
o    o
oooooo
 
E.g. n = 8
oooooooooooooooo
o              o
o              o
o              o
o              o
o              o
o              o
oooooooooooooooo
'''

#get input from user
user_input = int(input("Input a number: "))
#as seen from example the top and bottom are twice the input from user
top_and_bottom_range = 2*user_input
#placeholder for spaces to be used
space_var = " "
for i in range (0, top_and_bottom_range):
    print ("o", end="")
print()
for i in range (0, user_input+1): 
    if user_input == 1:
        print ("oo")
    else:
        print ("o", (top_and_bottom_range-4)*space_var, "o")
for i in range (0, top_and_bottom_range):
    print ("o", end = "")
