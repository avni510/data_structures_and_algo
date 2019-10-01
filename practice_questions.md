* What does it mean to be a Turing-complete ?

It can run any program that a Turing machine can. A programming language fulfills certain basic properties
that allow a developer to write a set of instructions to the computer.
Ex: conditionals, loops, variables, etc

* What is mean, median and mode of a probability distribution?
Continuous Distribution:

Discrete Distribution:

* What's the difference between stack and heap, when would you use one and when the other?

* Please write function to compute Fibonacci numbers in an iterative manner?

* What are the things you regret in your life?

* What do you know about the cross product?

* Please describe some technique of deepmind.

* Can you explain what a jacobian matrix is?

* What is a random variable?

* How do you deal with tight deadlines and short notice projects?

* Tell me why you think you are or are not suited for X role

* What is a hashtable? When should one be used? What is meant by collisions? What are some strategies for resolving collisions?

Hash table maps keys to values. It is backed by an array data structure where the index would relate to the hashed value.
And the value in the array would be a linked list.
Ex: If 'hello world' was put through a hash function and returns 2340. An algorithm for the hash table would
determine the key for 'hello world'. One idea is to use module 10.
2340 % 10 = 0. So at the 0 index 'hello world' is stored in the linked list.
A linked list is used to help resolve collisons.

Hash function -> maps data to an arbitary value. Always the same value

When to use:
They are dictionaries in python. Useful as key, value store. Fast lookup times

Collison Strategies:
- Linked List
- Linear probing - hash value if index is taken continue to look for an open spot
until one is found. Same for finding an element, hash the value. Continue to scan the
array for the correct key

Space and Time Complexity:
        Average       Worst Case
Space    O(N)            O(N)
Search   O(1)            O(N)
Insert   O(1)            O(N)
Delete   O(1)            O(N)

* Interests within AI

* Describe and explain Bayes theorem?
