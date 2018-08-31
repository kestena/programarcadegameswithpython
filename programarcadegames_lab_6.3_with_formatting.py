user_choice = int(input("Please enter a number: "))
m = 2*user_choice
cust_range1 = 1
cust_range2 = 2
#triangle 1
for i in range (0, user_choice):
    for j in range (cust_range1, m, 2):
        print ("{:2}".format(j), end=" ")
    for j in range (i):
        print ("{:2}".format(" "), end=" ")
    for j in range (i):
        print ("{:2}".format(" "), end= " ")
    for j in range (m-1, cust_range1-1, -2):
        print ("{:2}".format(j), end=" ")
    print()
    cust_range1 += 2

#triangle 2  
for i in range (0, user_choice):
    for j in range (m-1, m-cust_range2, -2):
        print ("{:2}".format(j), end=" ")
    for j in range (1, user_choice-i):
        print ("{:2}".format(" "), end=" ")
    for j in range (1, user_choice-i):
        print ("{:2}".format(" "), end=" ")
    for j in range (m-1, m-cust_range2, -2):
        print ("{:2}".format(j), end=" ")
    print()
    cust_range2 += 2
    
