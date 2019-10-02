# CS


## What does it mean to be a Turing-complete?

It can run any program that a Turing machine can. A programming language fulfills certain basic properties
that allow a developer to write a set of instructions to the computer.
Ex: conditionals, loops, variables, etc

## What's the difference between stack and heap, when would you use one and when the other?
* Stack
  - data structure. Can be backed by an array or a linked list
  - Last In First Out
  - Insert -> place at the top of the stack O(1) (using append of an array)
  - Pop -> Removes the element from the top of the stack and returns it O(1) (uses pop method from an array)
* Heap
  - Backed by an array based on the indexes of the array it represented a binary tree
  - MinHeap: the root node (including at the subtrees) is the min value
  - MaxHeap: the root node (including at the subtrees) in the max value
  - Priority Queue: useful when you want to put/ take things out in a priority. 
    An element with high priority is served before an element with low priority.
    The elements served don't have to be in exactly sorted order
  - Insert: O(log N)
  - Delete: O(log N) 
* When to use stack vs heap?
  - Stack is useful when having a strict order, heap is useful when having
  an order with some values having higher priority than others. But not all values
  have strict priority

## What is a hashtable? When should one be used? What is meant by collisions? What are some strategies for resolving collisions?

Hash table maps keys to values. It is backed by an array data structure where the index would relate to the hashed value.
And the value in the array would be a linked list.
Ex: If 'hello world' was put through a hash function and returns 2340. An algorithm for the hash table would
determine the key for 'hello world'. One idea is to use module 10.
2340 % 10 = 0. So at the 0 index 'hello world' is stored in the linked list.
A linked list is used to help resolve collisions.

Hash function -> maps data to an arbitrary value. Always the same value

When to use:
They are dictionaries in python. Useful as key, value store. Fast lookup times

Collision Strategies:
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

## Please write function to compute Fibonacci numbers in an iterative manner?

```python
def fib_iter(n):
    f0, f1 = 0, 1
    for i in range(0, n):
        f0, f1 = f0, f0 + f1
    return f1
```

# Linear Algebra


## What do you know about the cross product?
* requires both vectors to be 3 dimensional
* Two vectors being multiplied ( a X b)
* the result of the cross product is the vector that 
is perpendicular to both a and b (which implies that it's 
normal in the plane containing them)
* Dot product vs cross product
  - Dot product: result is a number
  - Cross product: result is a vector
* determinant of a 3 X 3 Matrix

a x b = | i  j  k  | 
        | a1 a2 a3 |
        | b1 b2 b3 |

## Can you explain what a jacobian matrix is?

[ 
  partial derivative of f1 with respect to x  partial derivative of f1 with respect to y
  partial derivative of f2 with respect to x  partial derivative of f2 with respect to y
]

What a transformation looks like at a specific point. * I don't understand the intuition of a Jacobian *

# Stat/ Probability


## What is a random variable?
* possible outcomes are numerical outcomes of a random phenomenon
* Discrete
  - There are a finite set of outcomes
  - A countable number of outcomes
* Continuous 
  - There are a infinite set of outcomes
  - Defined over an interval of values
  - The probability of observing a specific single value is 0
  - So an integral is used to determine the probability over a set of values

## What is mean, median and mode of a probability distribution?
Continuous Distribution:
- mode: The maximum of the distribution
- mean: The central location. Locate the pivot to see where it's balanced. 
Often called expected value. Integral from -infinity to infinity. x * f(x) dx
- median: Is the point at which the distribution function has the value 0.5.

Discrete Distribution:
- mode: most frequently occurring value
- mean: the average value
- median: the middle value. Separating out the lower half from the upper half

## Describe and explain Bayes theorem?
* Governs reversing the direction of conditional probabilities

             P(E) * P(F | E)
 P(E | F) = ----------------
                P(F)

# Behavioral


## What are the things you regret in your life?
* I wish I had a stronger foundation in the core knowledge for computer science. 
  - I wish I had time to take additional foundational courses in computer science while in college
  - It would have helped me during interview prep and understanding the trade offs on the job 
  - I would like to attend grad school at some point to gain that knowledge

* Taking up my current job with Tempus
  - After a few months into the job I realized it wasn't a good fit for me
  - They're focus is getting things done as quickly as possible, and quality isn't
  a big priority
  - I enjoy a place where I can work on creating a product with high quality while
  also meeting deadlines
  - On the positive side, I've still learned a lot by looking at code that was written
  quickly and thinking about how it could be improved for efficiency and readability

## Please describe some technique of deepmind.
* Using games as a testing ground for AI
  - games can be a good first start to experiment on different algorithms
  - parts of simple games and certainly more complex games can be representative of human life
  - star craft and alpha go
  - Like a labatory for AI
  - The research done to beat other players in a game may be applicable to ai in science, health, energy, etc
* Using the brain as inspiration for AI
  - creating artifical general intelligence requires the AI to be versed in many different
  scenarios
  - things that humans can do, are sometimes difficult for the AI, 
  suddenly remembering to pick up someting from the grocery store
  - This is an area of research
  - Additionally, how the brain handles and learns certain things can be inspiration for AI research

## How do you deal with tight deadlines and short notice projects?

## Tell me why you think you are or are not suited for X role

## Interests within AI
