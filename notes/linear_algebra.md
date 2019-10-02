### Linear Algebra

# Vector
  - quantity having direction or magnitude

# Matrix Multiplication
  - # of columns in A must equal # of rows in B
  - dot product
    [ 1 2 3] * [ 4
                 5        = 4 + 10 + 18 = 32
                 6 ]

  - outer product
    [ 1
      2    * [ 4 5 6 7 8 ] = [ 4   5   6   7   8
      3 ]                      8  10  12  14  16
                               12 15  18  21  24 ] 
  - matrix - matrix products
    
    A = [ 1   2  3
          10  2  1 ]

    A is a 2 X 3 matrix

    B = [ 4  1
          2  3
          1  5 ]

    B is a 3 X 2 matrix
  
    # of rows in A == # of columns in B

    A X B = [ 4 + 4 + 3     1 + 6 + 15
              40 + 4 + 1    10 + 6 + 5 ] 

    A X B = [ 11    22
              45    21 ]

    - properties
      * Associative: (AB)C = A(BC)
      * Distributive: A(B + C) = AB + AC
      * NOT communicative ex: AB != BA

    - To compute the dimensions of the product
      A = 1 X 3
      B = 3 X 2
      
      * Matrix multiplication is possible because # of columns in A == # of rows in B
      * The product matrix will be 1 X 2 (# of rows in A and # of columns in B)

# Transposition
  * Flipping rows and columns 

   A = [ 1  2  3
         4  5  6 ]

   A^T = [ 1  4
           2  5
           3  6 ]

  * (A^T)^T = A
  * (AB)^T = (B^T)(A^T)
  * (A + B)^T = A^T + B^T

# Identity Matrix
  * 1's for the diagonals, 0's everywhere else
  * AI = A = IA
  * if A = 2 X 3 then for AI = A, I = 3 X 3
  * if A = 2 X 3 then A = IA, I = 2 X 2

# Diagonal Matrix
  * All non-diagonal elements are 0 ex:
   [ 1  0  0 
     0  2  0
     0  0  3 ]

# Symmetric Matrix and Anti Symmetric
  * Symmetric
    * A = A^T
    * Only square matricies can be symmetric
    * A = 
      [ 1  2
        2  3 ] 
  * Anti symmetric
    * A = -A^T
    * Only square matricies can be symmetric
    * A =  
      [ 0  -1
        1   0 ] 

# The trace
  * Sum of Diagonal Elements
  * Properties
    * tr(A + B) = tr(A) + tr(B)
    * tr(A) = tr(A^T)
    * tr(tA) = t * tr(A)

# Linear combination
  * Matrices that all have the same dimensions
  * Take a set of matrices, multiply each one of them by a scalar, add together all the products -> linear combination

# Linear Transformation
  * Function such that: T: U -> V. Transforms a vector from vector space U to vector space V
  * Properties
    * T(U1 + U2) = T(U1) + T(U2)
    * T(aU) = a * T(U)

# Linear Independence and Linear Dependence
  * Linear independence
    * For two or more vectors if none of them can be written as a linear combination of the others 
      
      A = [ 0          B = [ 1
            1 ]              0 ]

  * Linear Dependence
    * If at least one of them can be written as a linear combination of the others
      
    A = [ 1        B = [ 4         C = [  2
          2              1               -3
          3 ]            5 ]              1 ]

    C = -2A + B

# Inverse
  * Only square matrices can have inverses
  * Denoted by A ^ -1
  * A^-1 * A = I = A * A^-1 -> for a matrix to be invertible this property must hold (ex: there must be an A^-1)
  * not all square matrices have an inverse. A square matrix is not invertible (singular) if and only if its determinant is 0

# Determinant
     [ a  b 
  A =  c  d ] 

  Det(A) = |A| = | a b | = ad - bc
                 | c d |

  * Calculating determinants are recursive
  * 3 X 3 matrix determinant: https://www.chilimath.com/lessons/advanced-algebra/determinant-3x3-matrix/

# Jacobian
  

# Eigenvalues and Eigenvectors

