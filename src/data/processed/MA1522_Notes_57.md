# Eigenvalues & eigen vectors

**Definition**
Let $\mathbf{A}$ be a square matrix of order $n$. A real number $\lambda$ is an eigenvalue of $\mathbf{A}$ if there is a nonzero vector $\mathbf{v}$ in $\mathbb{R}^n$, $\mathbf{v} \neq \mathbf{0}$, such that
$$\mathbf{A}\mathbf{v} = \lambda\mathbf{v}.$$

In this case, the nonzero vector $\mathbf{v}$ is called an eigenvector associated to $\lambda$.
Let $\mathbf{A}$ be a square matrix of order $n$, the characteristic polynomial of $\mathbf{A}$, denoted as $\text{char}(\mathbf{A})$, is the degree $n$ polynomial
$$\det(x\mathbf{I} - \mathbf{A}).$$

**Theorem**
Let $\mathbf{A}$ be a square matrix of order $n$. $\lambda \in \mathbb{R}$ is an eigenvalue of $\mathbf{A}$ if and only if the homogeneous system $(\lambda\mathbf{I} - \mathbf{A})\mathbf{x} = \mathbf{0}$ has nontrivial solutions.

**Theorem**
Let $\mathbf{A}$ be a square matrix of order $n$. $\lambda$ is an eigenvalue of $\mathbf{A}$ if and only if $\lambda$ is a root of the characteristic polynomial $\det(x\mathbf{I} - \mathbf{A})$.

**Theorem**
A square matrix $\mathbf{A}$ is invertible if and only if $\lambda = 0$ is not an eigenvalue of $\mathbf{A}$.

***

**Theorem** (Equivalent statements for invertibility)

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
14. $0$ is not an eigenvalue of $\mathbf{A}$.