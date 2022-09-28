# Given a Python list of numbers. Turn every item of a list into its square.
# Given: mylist = [1,2,3,4,5,6,7]

def myprog():
    mylist=[1, 2, 3, 4, 5, 6, 7]
    for i in range (7):
        print(mylist[i]*mylist[i], end=", ")
myprog()
