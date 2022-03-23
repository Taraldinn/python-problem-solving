# By this program we will get max number from a python program 

def myList(list1):
    max = list1[0]
    for i in list1:
        if i > max:
            max = i
    return max


list1 = [10, 20, 4, 45, 99]
print("Largest element is:", myList(list1))
