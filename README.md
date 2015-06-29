## Demonstration of Coroutines in Python
_By Noel Niles_


A generator function in Python is created using a `yield` expression.
When a generator function is called it returns an iterator called a
generator. When one of the generator's methods is called the execution
proceeds to the next `yield` statement. When execution reaches a yield
statement execution is suspended and the expression list is returned to
the generator's caller.

#### What happens when execution is suspend by a yield statement?
The following data is retained until another call to one of the
generators methods.

- local variables
- the instrucion pointer
- the eval stack
- exception handling state.

#### What does this have to do with coroutines?
Python generators have a lot in common with coroutines.

- They yield multiple times
- They have more than one entry point
- They can be suspended

The only difference between a coroutine and a Python generator is that a
generator always returns control to it's caller, but a coroutine can
decide resume execution in a different function.

#### How does the demo simulate execution time
The execution time is simulated with a call to `time.sleep()`. Although
arbitrary I tried to make the sleep times coorispond to operations. In
other words a function should perform and operation and then sleep in
order to pretend it's working hard and to give us something to watch.

#### How do I use the demo?
It's easy! There are two demonstrations. Each demonstration performs
three functions on a lists of integers. 
1. First two lists are added together; in other words the elements from one 
list are added to the end of another list.
2. Next each element in the list is raised to a power (the details aren't really important).
3. Finally the list is sorted and the results are returned.

##### Blocking Demo
Each function blocks so the execution time is the product of all three
operations.
'''
$ python -m gent slow
'''

##### Non-Blocking Demo
Each function yields the result as soon as it's computed.
'''
$ python -m gent fast
'''

### Exercises for the Reader
1. Fix the sort function in fast_chain.py so that it doesn't block but
   also returns the correct sorted value.
2. Add another function to the slow_chain and fast_chain. Both versions
   should consume a noticeable amount of time, but the fast_chain
   version should be able to yield values immediately.
3. Make a coroutine that receives values and yields results.
4. Implement a thread pool Task that offloads the generators to multiple
   threads.

###References
* [Task and Coroutines](https://docs.python.org/3/library/asyncio-task.html) 
* [Syntax for Delegating to a Subgenerator](https://www.python.org/dev/peps/pep-0380/)
* [A Curious Course on Corotutines and Concurrency](http://www.dabeaz.com/coroutines/index.html)
* [Generator Tricks for Systems Programmers](http://www.dabeaz.com/generators-uk/index.html)






Copyright 2015 Noel Niles
