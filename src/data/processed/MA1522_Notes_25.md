# Determinant by cofactor expansion

1. $\det(A)$ or $|A|$
   $n=1 \quad A = (a), \det(A) = a \quad \to \det(A) = \det(A^T)$
   $n=2 \quad A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}, \det(A) = ad-bc$

---

### Inductive Step: Matrix Minor

Suppose we have defined the determinant of all square matrices of order $\le n-1$. Let $\mathbf{A}$ be a square matrix of order $n$.

Define $M_{ij}$, called the $(i,j)$ matrix minor of $\mathbf{A}$, to be the matrix obtained from $\mathbf{A}$ be deleting the $i$-th row and $j$-th column.

Example

$$\mathbf{A} = \begin{pmatrix} 5 & 1 & 2 & -1 \\ -1 & -3 & 1 & 3 \\ 3 & 8 & 2 & 1 \\ 2 & 0 & 1 & 11 \end{pmatrix}$$

$$M_{11} = \begin{pmatrix} -3 & 1 & 3 \\ 8 & 2 & 1 \\ 0 & 1 & 11 \end{pmatrix}, M_{12} = \begin{pmatrix} -1 & 1 & 3 \\ 3 & 2 & 1 \\ 2 & 1 & 11 \end{pmatrix}, M_{23} = \begin{pmatrix} 5 & 1 & -1 \\ 3 & 8 & 1 \\ 2 & 0 & 11 \end{pmatrix}, M_{43} = \begin{pmatrix} 5 & 1 & -1 \\ -1 & -3 & 3 \\ 3 & 8 & 1 \end{pmatrix}$$

---

### Inductive Step: Cofactor

The $(i,j)$-cofactor of $\mathbf{A}$, denoted as $A_{ij}$, is the (real) number given by
$$A_{ij} = (-1)^{i+j} \det(M_{ij}).$$

Take note of the sign of the $(i,j)$-entry, $(-1)^{i+j}$. Here's a visualization of the sign of the entries of the matrix

$$\begin{pmatrix} + & - & + & \cdots \\ - & + & - & \cdots \\ + & - & + & \cdots \\ \vdots & \vdots & \vdots & \ddots \end{pmatrix}$$