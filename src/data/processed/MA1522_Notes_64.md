**Definition**

An order $n$ square matrix $\mathbf{A}$ is orthogonally diagonalizable if

$$\mathbf{A} = \mathbf{P}\mathbf{D}\mathbf{P}^T$$

for some orthogonal matrix $\mathbf{P}$ and diagonal matrix $\mathbf{D}$.

**Theorem** (The Spectral Theorem)

Let $\mathbf{A}$ be an $n \times n$ square matrix. $\mathbf{A}$ is orthogonally diagonalizable if and only if $\mathbf{A}$ is symmetric.

**Theorem** (Equivalent statements for orthogonally diagonalizable)

Let $\mathbf{A}$ be a square matrix of order $n$. The following statements are equivalent.

I. $\mathbf{A}$ is orthogonally diagonalizable.
II. There exists an orthonormal basis $\{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n\}$ of $\mathbb{R}^n$ of eigenvectors of $\mathbf{A}$.
III. $\mathbf{A}$ is symmetric matrix.

$\mathbf{A}$ orthogonally diagonalizable if and only if

$$\mathbf{P} = \begin{pmatrix} \mathbf{u}_1 & \mathbf{u}_2 & \dots & \mathbf{u}_n \end{pmatrix} \text{, and } \mathbf{D} = \begin{pmatrix} \mu_1 & 0 & \dots & 0 \\ 0 & \mu_2 & \dots & 0 \\ \vdots & & \ddots & \vdots \\ 0 & 0 & \dots & \mu_n \end{pmatrix},$$

where $\mu_i$ is the eigenvalue associated to eigenvector $\mathbf{u}_i, i = 1, \dots, n, \mathbf{A}\mathbf{u}_i = \mu_i\mathbf{u}_i$, and $\{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n\}$ is an orthonormal basis for $\mathbb{R}^n$.

**Theorem** (Eigenspaces of a symmetric matrix is orthogonal)

If $\mathbf{A}$ is a symmetric matrix, then the eigenspaces are orthogonal to each other. That is, suppose $\lambda_1$ and $\lambda_2$ are distinct eigenvalues of a symmetric matrix $\mathbf{A}, \lambda_1 \neq \lambda_2$, and $\mathbf{v}_i$ is an eigenvector associated to eigenvalue $\lambda_i$, for $i = 1, 2$. Then $\mathbf{v}_1 \cdot \mathbf{v}_2 = 0$.

$\mathbf{A} = \begin{pmatrix} 5 & -1 & -1 \\ -1 & 5 & -1 \\ -1 & -1 & 5 \end{pmatrix}$. Characteristic polynomial: $\begin{vmatrix} x - 5 & 1 & 1 \\ 1 & x - 5 & 1 \\ 1 & 1 & x - 5 \end{vmatrix} = (x - 3)(x - 6)^2$. Eigenvalues: $\lambda = 3, 6$.

$3\mathbf{I} - \mathbf{A} = \begin{pmatrix} -2 & 1 & 1 \\ 1 & -2 & 1 \\ 1 & 1 & -2 \end{pmatrix} \rightarrow \begin{pmatrix} 1 & 0 & -1 \\ 0 & 1 & -1 \\ 0 & 0 & 0 \end{pmatrix}$ So, $E_3 = \text{span} \left\{ \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} \right\}$

$6\mathbf{I} - \mathbf{A} = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & 1 \\ 1 & 1 & 1 \end{pmatrix} \rightarrow \begin{pmatrix} 1 & 1 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$ So, $E_6 = \text{span} \left\{ \begin{pmatrix} -1 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} -1 \\ 0 \\ 1 \end{pmatrix} \right\}$

Check that the eigenspaces are orthogonal.

$$\begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} \cdot \begin{pmatrix} -1 \\ 1 \\ 0 \end{pmatrix} = 0, \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} \cdot \begin{pmatrix} -1 \\ 0 \\ 1 \end{pmatrix} = 0 \Rightarrow E_3 \perp E_6.$$