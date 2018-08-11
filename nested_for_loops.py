'''
I have to create the following pattern:

0 1 2 3 4 5 6 7 8 9 
0 1 2 3 4 5 6 7 8 9 
0 1 2 3 4 5 6 7 8 9 
0 1 2 3 4 5 6 7 8 9 
0 1 2 3 4 5 6 7 8 9 
0 1 2 3 4 5 6 7 8 9 
0 1 2 3 4 5 6 7 8 9 
0 1 2 3 4 5 6 7 8 9 
0 1 2 3 4 5 6 7 8 9 
0 1 2 3 4 5 6 7 8 9

Below you will find my way and the answer's way.

Is my way bad or still works?'''

#my way - is it a bad way?
for i in range(10):
    for j in range (-1, 9):
        print (j+1, end=" ")
    print()

#answer's way
for i in range(10):
    for j in range (10):
        print (j, end=" ")
    print()
