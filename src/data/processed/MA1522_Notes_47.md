Theorem
Let $\mathbf{A}$ be a square matrix of order $n$. The following statements are equivalent.
1. $\mathbf{A}$ is invertible.
2. $\mathbf{A}^T$ is invertible.
3. $\mathbf{A}$ has a left-inverse, that is, there is a matrix $\mathbf{B}$ such that $\mathbf{BA} = \mathbf{I}$.
4. $\mathbf{A}$ has a right-inverse, that is, there is a matrix $\mathbf{B}$ such that $\mathbf{AB} = \mathbf{I}$.
5. The reduced row-echelon form of $\mathbf{A}$ is the identity matrix.
6. $\mathbf{A}$ can be expressed as a product of elementary matrices.
7. The homogeneous system $\mathbf{Ax} = \mathbf{0}$ has only the trivial solution.
8. For any $\mathbf{b}$, the system $\mathbf{Ax} = \mathbf{b}$ is consistent.
9. The determinant of $\mathbf{A}$ is nonzero, $\det(\mathbf{A}) \neq 0$.
10. The columns/rows of $\mathbf{A}$ are linearly independent for $\mathbb{R}^n$.
11. The columns/rows of $\mathbf{A}$ spans $\mathbb{R}^n$.
12. $\mathbf{A}$ is of full rank, $rank(\mathbf{A}) = n$.
13. $nullity(\mathbf{A}) = 0$.

Theorem (Full Rank Equals Number of Columns)
Suppose $\mathbf{A}$ is a $m \times n$ matrix. The following statements are equivalent.
1. $\mathbf{A}$ is full rank, where the rank is equal to the number of columns, $rank(\mathbf{A}) = n$.
2. The rows of $\mathbf{A}$ spans $\mathbb{R}^n$, $\text{Row}(\mathbf{A}) = \mathbb{R}^n$.
3. The columns of $\mathbf{A}$ are linearly independent.
4. The homogeneous system $\mathbf{Ax} = \mathbf{0}$ has only the trivial solution, that is, $Null(\mathbf{A}) = \{\mathbf{0}\}$.
5. $\mathbf{A}^T\mathbf{A}$ is an invertible matrix of order $n$.
6. $\mathbf{A}$ has a left inverse.

The reduced row-echelon form of $\mathbf{A}$ is
$$ \mathbf{R} = \begin{pmatrix} \mathbf{I}_n \\ \mathbf{0}_{(m-n) \times n} \end{pmatrix}. $$

Theorem (Full Rank Equals Number of Rows)
Suppose $\mathbf{A}$ is a $m \times n$ matrix. The following statements are equivalent.
1. $\mathbf{A}$ is full rank, where the rank is equal to the number of rows, $rank(\mathbf{A}) = m$.
2. The columns of $\mathbf{A}$ spans $\mathbb{R}^m$, $\text{Col}(\mathbf{A}) = \mathbb{R}^m$.
3. The rows of $\mathbf{A}$ are linearly independent.
4. The linear system $\mathbf{Ax} = \mathbf{b}$ is consistent for every $\mathbf{b} \in \mathbb{R}^m$.
5. $\mathbf{AA}^T$ is an invertible matrix of order $m$.
6. $\mathbf{A}$ has a right inverse.

The reduced row-echelon form of $\mathbf{A}$ has the form
$$ \begin{pmatrix} 1 & \dots & 0 & \dots & 0 & \dots & 0 & \dots \\ 0 & \dots & 1 & \dots & 0 & \dots & 0 & \dots \\ 0 & \dots & 0 & \dots & 1 & \dots & 0 & \dots \\ \vdots & \dots & \vdots & \dots & \vdots & \dots & \vdots & \dots \\ 0 & \dots & 0 & \dots & 0 & \dots & 1 & \dots \end{pmatrix} $$

Challenge
Let $\mathbf{A}$ be a $m \times n$ matrix such that $rank(\mathbf{A}) = m$. Suppose $m > n$. By the equivalent statements of full rank equals number of columns, $(\mathbf{A}^T\mathbf{A})$ invertible and $(\mathbf{A}^T\mathbf{A})^{-1}\mathbf{A}^T$ is a left inverse of $\mathbf{A}$.
Now consider the system $\mathbf{Ax} = \mathbf{b}$ for some vector $\mathbf{b} \in \mathbb{R}^m$. Premultiplying the left inverse above on both sides of the equation, we get
$$ \mathbf{x} = ((\mathbf{A}^T\mathbf{A})^{-1}\mathbf{A}^T)\mathbf{Ax} = ((\mathbf{A}^T\mathbf{A})^{-1}\mathbf{A}^T)\mathbf{b}, $$
that is, $((\mathbf{A}^T\mathbf{A})^{-1}\mathbf{A}^T)\mathbf{b}$ is a solution to $\mathbf{Ax} = \mathbf{b}$. But this is true for every $\mathbf{b}$, which by the equivalent statements of full rank equals number or rows, means that the rank of $\mathbf{A}$ is equal to $m$, the number of row. This is a contradiction to $m > n$.
What is the mistake in the argument above?