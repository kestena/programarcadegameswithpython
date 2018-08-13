'''
Assignment 6.1 Create the following pattern:
10
11 12
13 14 15
16 17 18 19
20 21 22 23 24
25 26 27 28 29 30
31 32 33 34 35 36 37
38 39 40 41 42 43 44 45
46 47 48 49 50 51 52 53 54
'''

some_var = 10 #define a variable to store the starting point
for i in range (1, 10):
    for j in range (1, i+1): #start from range 1 to avoid printing twice on first time
        #print the variable instead of j. j will print 0, 1, 2, 3 etc. which is not what we want
        print (some_var, end = " ")
        #increase the variable with 1 everytime
        some_var +=1 
    print()
