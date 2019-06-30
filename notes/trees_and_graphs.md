#### Trees and Graphs

### Trees
- Trees vs. Binary Trees
  * beware which type your interviewer is asking for
  * Binary tree - each node can have a max of 2 children (this is not 
  necessarily true of other types of trees)
- Leaf node - when a node has no children

- Binary Search Tree
  * has a specific ordering
  * all left descendants <= n 
  * all right descendants > n
  * definitions can vary so clarify definition with interviewer
  * ALL nodes on the left must be less than the root and ALL nodes on the right
  must be greater than the root

- Balanced Trees
  * Does not necessarily mean the right and subtrees are exactly the same size
  * but it does ensure it is balanced enough to ensure O(log N) time for insert and find
  * Topics to review red-black trees and AVL trees

- Complete Binary Tree
  * Every level of the tree is filled excepts perhaps the last level
  * It is filled left to right
  * see pg 102 for example

- Full Binary Tree
  * Every node has either zero or two children
  * No node has 1 child

- Perfect Binary Tree
  * All nodes have 2 children
  * The last level has 0 children
  * All leaf nodes at the same level

- Min heaps
  * Complete binary tree (except the right most elements on the last level)
  * each node is smaller than its children
  * root, therefore, is the minimum
  * inserting
    - we insert at the rightmost spot 
    - then we "fix" the tree
      - swap the new element with its parent
      - until we find the best spot for it
      - keep bubbling up elements until the tree is back to a min heap
      - this take O(log N)

* TO DO: Review Binary Heaps and Tries

### Graphs
* Time Complexity for an adjacency list is O(N + M)
Explanation: O(N + summation(all the degrees on a graph))
summation(all the degrees on a graph) = 2M Ex: 5 edges will have 10 traversals
because each edge is connected by 2 vertices
