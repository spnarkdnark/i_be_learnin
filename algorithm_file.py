import math
import random

#insertionsort

array1 = [1,5,3,7,9,5,6,9,23,5,57,83,100]

def get_array(size):
    return [random.randint(1,101) for i in range(0,size)]

def insertion_sort(array):

    for i in range(1,len(array)):
        for j in range(i-1,-1,-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]

            else:
                break

    print(array)

def optomized_insertion_sort(array):

    for i in range(1,len(array)):
        curnum = array[i]
        for j in range(i-1,-1,-1):
            if array[j] > curnum:
                array[j+1] = array[j]
                array[j] = curnum
            else:
                array[j+1] = curnum
                break

    print(array)


def textbook_insertion(array):

    for j in range(1,len(array)):
        curnum = array[j]
        i = j-1
        while i>=0 and array[i] > curnum:
            array[i+1] = array[i]
            i -= 1
        array[i+1] = curnum

    print(array)


def bottomsort(t):
    for j in range(len(t) - 1, -1, -1):
        currow = t[j]
        for i in range(0, len(currow) - 1):
            m = max(currow[i], currow[i + 1])
            t[j - 1][i] = t[j - 1][i] + m

    return currow


def linearsearch(A,v):
    for i in range(0,len(A)):
        if A[i] == v:
            return i+1
            break
    return 0

graph = {}

graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

graph['a'] = {}
graph['a']['fin'] = 1

graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5

graph['fin'] = {}

print(graph)

infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

print(parents)

processed = []


