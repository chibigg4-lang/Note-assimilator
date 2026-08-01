**Theorem**
An $n \times n$ square matrix $\mathbf{A}$ is invertible if and only if the columns are linearly independent.

**Theorem**
An $n \times n$ square matrix $\mathbf{A}$ is invertible if and only if the columns spans $\mathbb{R}^n$.

**Corollary**
Let $S = \{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n\}$ be a subset of $\mathbb{R}^n$ containing $n$ vectors. Then $S$ is linearly independent if and only if $S$ spans $\mathbb{R}^n$.

**Corollary**
Let $S = \{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_k\}$ be a subset of $\mathbb{R}^n$ and $\mathbf{A} = (\mathbf{u}_1 \quad \mathbf{u}_2 \quad \dots \quad \mathbf{u}_k)$ be the matrix whose columns are vectors in $S$. Then $S$ is {basis} for $\mathbb{R}^n$ if and only if {k = n} and $\mathbf{A}$ is an invertible matrix.

**Theorem**
An $n \times n$ square matrix $\mathbf{A}$ is invertible if and only if the columns of $\mathbf{A}$ form a basis for $\mathbb{R}^n$.

**Theorem**
An $n \times n$ square matrix $\mathbf{A}$ is invertible if and only if the row of $\mathbf{A}$ form a basis for $\mathbb{R}^n$.

### Equivalent Statements for Invertibility

**Theorem**
Let $\mathbf{A}$ be a square matrix of order $n$. The following statements are equivalent.

1. $\mathbf{A}$ is invertible.
2. $\mathbf{A}^T$ is invertible.
3. $\mathbf{A}$ has a left-inverse, that is, there is a matrix $\mathbf{B}$ such that $\mathbf{B}\mathbf{A} = \mathbf{I}$.
4. $\mathbf{A}$ has a right-inverse, that is, there is a matrix $\mathbf{B}$ such that $\mathbf{A}\mathbf{B} = \mathbf{I}$.
5. The reduced row-echelon form of $\mathbf{A}$ is the identity matrix.
6. $\mathbf{A}$ can be expressed as a product of elementary matrices.
7. The homogeneous system $\mathbf{A}\mathbf{x} = \mathbf{0}$ has only the trivial solution.
8. For any $\mathbf{b}$, the system $\mathbf{A}\mathbf{x} = \mathbf{b}$ is consistent.
9. The determinant of $\mathbf{A}$ is nonzero, $\det(\mathbf{A}) \neq 0$.
10. The columns/rows of $\mathbf{A}$ are linearly independent for $\mathbb{R}^n$.
11. The columns/rows of $\mathbf{A}$ spans $\mathbb{R}^n$.

***

**Definition**
Let $S = \{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_k\}$ be a basis for a subspace $V$ of $\mathbb{R}^n$.

Then given any vector $\mathbf{v} \in V$, we can write $\mathbf{v}$ unique as
$$c_1\mathbf{u}_1 + c_2\mathbf{u}_2 + \dots + c_k\mathbf{u}_k.$$

The coordinates of $\mathbf{v}$ relative to the basis $S$ is defined to be the vector
$$[\mathbf{v}]_S = \begin{pmatrix} c_1 \\ c_2 \\ \vdots \\ c_k \end{pmatrix}.$$

$$\begin{pmatrix} x \\ y \\ z \end{pmatrix} = x \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} + y \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} + z \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$$

$$\begin{pmatrix} x \\ y \\ z \end{pmatrix}_E = \begin{pmatrix} x \\ y \\ z \end{pmatrix}$$

**Algorithm for Computing Relative Coordinate**
Let $S = \{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_k\}$ be a basis for a subspace $V$ of $\mathbb{R}^n$.

For $\mathbf{v} \in V$, find real numbers $c_1, c_2, \dots, c_k \in \mathbb{R}$ such that
$$c_1\mathbf{u}_1 + c_2\mathbf{u}_2 + \dots + c_k\mathbf{u}_k = \mathbf{v}.$$

That is, we are solving for
$$(\mathbf{u}_1 \quad \mathbf{u}_2 \quad \dots \quad \mathbf{u}_k \mid \mathbf{v}).$$