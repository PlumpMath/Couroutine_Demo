"""Non-Blocking Functions

These functions should perform better than their slow cousins in
slow_chain.py because the yield their value at each step. This way, when
chained to other functions that accept generators the next function can
start working right away--It doesn't have to wait for the previous
function to return the complete results.
"""
import bisect
import time

from . import export

def fast_list_append(agen, bgen):
    """Append bgen to the end of agen"""
    yield from agen
    yield from bgen
    print("Finished Appending")

def fast_list_power_filter(agen, power):
    """Raise each element in agen to power"""
    for elem in agen:
        time.sleep(1)
        yield elem ** power
    print("Finished Power Filtering")

def fast_list_sort(agen):
    """FIX THIS"""
    gen = yield from agen
    sl = []
    bisect.insort(sl, gen)
    yield sl[-1]
    print("Finished Sorting")

@export
def fast_function_chain():
    """Test the coroutine function chain."""
    agen = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900]
    bgen = [153, 729, 12, 1634, 42, 300112, 64]
    power = 5
    
    fla = fast_list_append(agen, bgen)
    flpf = fast_list_power_filter(fla, power)
    fls = fast_list_sort(flpf)

    for item in fls:
        if item is None:
            pass
        else:
            print(item)
    
if __name__ == '__main__':
    fast_function_chain()
