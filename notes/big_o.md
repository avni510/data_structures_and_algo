#### Big O

* review time complexity for quick sort algo
- When you have a recursive function that make multiple calls, the time will often
look like O(branches ^ depth). Can calculate the runtime accordingly
- Drop the non-Dominant Terms. Ex:
  - O(2N) -> O(N)
  - O(N + log N) -> O(N)
- Time complexity to sort an array: O(N log(N))
- When you see an algo with multiple recursive calls, it's likely an exponential 
runtime


## Space Complexity
- Create an array of size n. Space Complexity: O(n)
- Two dimensional array. Space Complexity: O(n^2)
- Stack space in recursive calls take space. Ex: Recursion for factorial is O(N)
Space and Time Complexity
- Space and Time complexity doesn't always match

## Log N runtimes
- Binary Search on a sorted array
- When you see a problem where the number of elements gets halved each time, 
it will likely be a log n runtime
- cutting the problem space in half
- balanced binary search tree

## Examples to Review
- 3
- 7
- 8
- 9 (after reviewing balanced binary search tree)
- 12 (very difficult)
- 14
- 15
