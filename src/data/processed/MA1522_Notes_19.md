Equivalent statements
Let $A_{n \times n}$

> **Theorem (Equivalent statements of invertibility)**
> Let $\mathbf{A}$ be a square matrix of order $n$. The following statements are equivalent.
> (i) $\mathbf{A}$ is invertible.
> (ii) $\mathbf{A}^T$ is invertible.
> (iii) (left inverse) There is a matrix $\mathbf{B}$ such that $\mathbf{BA} = \mathbf{I}$.
> (iv) (right inverse) There is a matrix $\mathbf{B}$ such that $\mathbf{AB} = \mathbf{I}$.
> (v) The reduced row-echelon form of $\mathbf{A}$ is the identity matrix.
> (vi) $\mathbf{A}$ can be expressed as a product of elementary matrices.
> (vii) The homogeneous system $\mathbf{Ax} = \mathbf{0}$ has only the trivial solution.
> (viii) For any $\mathbf{b}$, the system $\mathbf{Ax} = \mathbf{b}$ has a unique solution.

***

Example
Consider the matrix $\mathbf{A} = \begin{pmatrix} 1 & -1 & 1 \\ -1 & 1 & 1 \\ 0 & -1 & 1 \end{pmatrix}$. Reducing, we have
$$\begin{pmatrix} 1 & -1 & 1 \\ -1 & 1 & 1 \\ 0 & -1 & 1 \end{pmatrix} \xrightarrow{R_1-R_3, R_2+R_1, R_3+R_2, \frac{1}{2}R_3, R_2-R_3} \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}.$$
Here we can conclude that the reduced row-echelon form of $\mathbf{A}$ is the identity matrix, and from the previous section,
$$\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & -1 \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1/2 \end{pmatrix} \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 & -1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \mathbf{A} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}.$$
By taking the inverse of the elementary matrices, we get
$$\mathbf{A} = \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 & 0 \\ -1 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & -1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{pmatrix} \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{pmatrix}.$$
Observe that $\mathbf{A}$ is a product of elementary matrices!