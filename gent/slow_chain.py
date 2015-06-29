"""Lazy Functions

These functions are lazy not because they delay evaluation until needed
but because the take a one second break after every task. These are used
to test the usefulness of chaining generators into a process pipeline.
"""
import time

from . import export

def slow_list_append(alist, blist):
    # Append the elements of blist to alist
    for elem in blist:
        alist.append(elem)
        time.sleep(1)
    print("Finished Appending")
    return alist

def slow_list_power_filter(alist, power):
    # Raise each element in a list to power.
    for idx, elem in enumerate(alist):
        alist[idx] = elem ** power
        time.sleep(1)
    print("Finished Power Filtering")
    return alist

def slow_list_sort(alist):
    time.sleep(len(alist))
    print("Finished Sorting")
    slist = sorted(alist)
    return slist

@export
def slow_function_chain():
    start = time.time()
    alist = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900]
    blist = [153, 729, 12, 1634, 42, 300112, 64]
    power = 5
    
    sla = slow_list_append(alist, blist)
    slpf = slow_list_power_filter(sla, power)
    clist = alist + blist
    sls = slow_list_sort(clist)
    
    for elem in iter(sls):
        print(elem, end='\n')
    end = time.time()
    print("Slow Chain Exec Time: ", end-start)


if __name__ == '__main__':
    slow_function_chain()
