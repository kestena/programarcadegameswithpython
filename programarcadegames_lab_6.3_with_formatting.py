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
