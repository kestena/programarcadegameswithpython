'''
I actually made it work with double digit numbers as well :)

Assignment:
Print the following for any positive integer n. Use an input statement to allow the user to enter 
the value for n and then print the properly sized box.

E.g. n = 3
 
1 3 5 5 3 1
3 5     5 3
5         5
5         5
3 5     5 3
1 3 5 5 3 1
 
E.g. n = 5
1 3 5 7 9 9 7 5 3 1
3 5 7 9     9 7 5 3
5 7 9         9 7 5
7 9             9 7
9                 9
9                 9
7 9             9 7
5 7 9         9 7 5
3 5 7 9     9 7 5 3
1 3 5 7 9 9 7 5 3 1

'''


user_choice = int(input("Please enter a number: "))
m = 2*user_choice
#triangle 1
for i in range (0, user_choice):
    for j in range ((i*2)+1, m, 2):
        print ("{:2}".format(j), end=" ")
    for j in range (i):
        print ("{:2}".format(" "), end=" ")
    for j in range (i):
        print ("{:2}".format(" "), end= " ")
    for j in range (m-1, i*2, -2):
        print ("{:2}".format(j), end=" ")
    print()

#triangle 2  
for i in range (0, user_choice):
    for j in range ((m-1)-i*2, m, 2):
        print ("{:2}".format(j), end=" ")
    for j in range (1, user_choice-i):
        print ("{:2}".format(" "), end=" ")
    for j in range (1, user_choice-i):
        print ("{:2}".format(" "), end=" ")
    for j in range (m-1, (m-2)-i*2, -2):
        print ("{:2}".format(j), end=" ")
    print()
