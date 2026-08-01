Inverse of $2 \times 2$ square matrices
$$A^{-1} = \frac{1}{ad-bc} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$$
Inversible when $ad-bc \neq 0$

Cancellation law for matrices.
Let $A$ be an invertible matrix of order $n$
(Left cancellation) if $B \& C$ are $n \times m$ matrices with $AB = AC$
Then $B = C$
(Right cancellation) if $B \& C$ are $m \times n$ matrices with $BA = CA$
Then $B = C$.
if $AB = CA$ , cannot conclude $B = C$

Invertibility and Linear System:
Suppose $A$ is an $n \times n$ invertible square matrix
For any $n \times 1$ vector, $Ax = b$ has unique solution
existance : $u = A^{-1}b$ $\quad A(A^{-1}b) = I.b = b$
uniqueness : $\quad$ sol $Ax = b$ $\quad Av = b = Au$
$\quad \quad \quad \quad \quad v = A^{-1}Av = A^{-1}Au = u.$

Corollary.
A is invertible. The trivial solution is the only solution to the homogenous system $Ax = 0$
$b = 0$ $\quad \rightarrow$ done!