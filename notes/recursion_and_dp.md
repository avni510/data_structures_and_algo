### Recursion and Dynamic Programming

* Can be very space inefficent - each recursive call adds a layer to the stack
  - If it recurses to a depth of N. It uses at least O(n) Memory.A
* To figure out the time complexity. Drawing the code paths as a tree can be very helpful
* memoization - caching a result. Can be especially useful for recursion, so it doesn't have to
compute the same value twice. Ex: for Fibonacci, fib(2) will be called multiple times
