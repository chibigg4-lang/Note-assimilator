# Properties of determinant.

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

**Theorem** (Determinant of product is the product of determinant)

Let $\mathbf{A}$ and $\mathbf{B}$ be square matrices of the same size. Then
$$\det(\mathbf{AB}) = \det(\mathbf{A}) \det(\mathbf{B}).$$

By induction, for square matrices $\mathbf{A}_1, \mathbf{A}_2, \dots, \mathbf{A}_k$ of the same size,
$$\det(\mathbf{A}_1 \mathbf{A}_2 \cdots \mathbf{A}_k) = \det(\mathbf{A}_1) \det(\mathbf{A}_2) \cdots \det(\mathbf{A}_k).$$

**Theorem** (Determinant of inverse is the inverse of determinant)

If $\mathbf{A}$ is invertible, then
$$\det(\mathbf{A}^{-1}) = \det(\mathbf{A})^{-1}.$$

For any square matrix $A$ of order $n$ and scalar $c$
$\det(cA) = \det((cI)A) = \det(cI) \det A$
$= \begin{vmatrix} c & & 0 \\ & \ddots & \\ 0 & & c \end{vmatrix} \det(A)$
$\rightarrow \det(cA) = c^n \cdot \det(A)$

**Adjoint :**
$A_{n \times n}$
$\text{adj}(A)$ is the $n \times n$ square matrix in which $(i,j)$ entry is $(j,i)$-cofactor of $A$