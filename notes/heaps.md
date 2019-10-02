#### Heaps

* Tree based data structure
* Tree is a complete binary tree
* Max-heap: value present at the root node is the largest value. True for all subtrees as well 

     100
    /   \
  40    50
 /  \   / \
10  15 20 30

* Min-heap: value present at the root node is the smallest value: True for all subtrees as well
     10
    /   \
  20    30
 /  \   / \
40  50 60 70

* partially ordered data structure
* Useful data structure when you need to remove the highest/ lowest priority
* Height of the heap is O(log N)

* Priority Queue Implementation:
      10
    /   \
  30    20
 /  \   / \
40  50 60 70

[None, 10, 30, 20, 40, 50, 60, 70]
* The 0 index is skipped (for convenience)

For the kth element
* left child: 2k index
* right child: 2k + 1 index
* parent: k / 2

Insert:
* the new element is usually appended to the end of the array. The heap property is kept up by comparing the
newly inserted element with the parent, and moving it up a level if need be

Ex - inserting 5:

      10
    /   \
  30    20
 /  \   / \
40  50 60  5 (new element) 

[None, 10, 30, 20, 40, 50, 60, 5]
[None, 10, 30, 5, 40, 50, 60, 20]
[None, 5, 30, 10, 40, 50, 60, 20]

Deletion: 
* the min element is found at the root (1st element in the array). Remove the root and replace with the last element in
array. Then restore the heap property. 

Ex - deleting 10:

      10
    /   \
  30    20
 /  \   / 
40  50 60 

[None, 60, 30, 20, 40, 50]
[None, 20, 30, 60, 40, 50]

When to use:
* Priority Queues - Useful for processing elements based on some priority. An element with a high priority is served 
before an element with a low priority. If two elements have the same priority they are served according to the order 
in which they are enqueued (in some implementations). A binary heap can be used for this

Runtimes:
* Insert: O(log N)
* deleteMin: O(log N)
* remove: O(log N)
* findMin: O(1)
