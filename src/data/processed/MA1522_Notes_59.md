### Definition
The eigenspace associated to an eigenvalue $\lambda$ of $\mathbf{A}$ is
$$E_{\lambda} = \{ \mathbf{v} \in \mathbb{R}^n \mid \mathbf{A}\mathbf{v} = \lambda\mathbf{v} \} = Null(\lambda\mathbf{I} - \mathbf{A}).$$
The geometric multiplicity of an eigenvalue $\lambda$ is the dimension of its associated eigenspace,
$$\dim(E_{\lambda}) = nullity(\lambda\mathbf{I} - \mathbf{A}).$$

### Question
1. Let $\mathbf{A}$ and $\mathbf{B}$ be row equivalent order $n$ square matrices.
    A. If $\lambda$ is an eigenvalue of $\mathbf{A}$, is it an eigenvalue of $\mathbf{B}$?
    B. If $\mathbf{v}$ is an eigenvector of $\mathbf{A}$, is it an eigenvector of $\mathbf{B}$?
2. Can we compute the characteristic polynomial of a square matrix using row reduction instead of cofactor expansion?

### Challenge
Let $\mathbf{A}$ be an $n \times n$ matrix.
1. Show that the characteristic polynomial of $\mathbf{A}$ is equal to the characteristic polynomial of $\mathbf{A}^T$. Hence $\mathbf{A}$ and $\mathbf{A}^T$ has the same eigenvalues.
2. Let $\lambda$ be an eigenvalue of $\mathbf{A}$. Show that the geometric multiplicity of $\lambda$ as an eigenvalue of $\mathbf{A}$ is equal to its geometric multiplicity as an eigenvalue of $\mathbf{A}^T$.

---

### Example
Let $\mathbf{A} = \begin{pmatrix} 1 & 1 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 2 \end{pmatrix}$. We will first find the eigenvalues.
$$\det(x\mathbf{I} - \mathbf{A}) = \begin{vmatrix} x - 1 & -1 & 0 \\ -1 & x - 1 & 0 \\ 0 & 0 & x - 2 \end{vmatrix} = (x-2)((x-1)^2 - 1) = x(x-2)^2.$$
So, the eigenvalues are $\lambda = 0, 2$, with algebraic multiplicities $r_0 = 1, r_2 = 2$, respectively.

Next, we will find a basis for the eigenspaces.
For eigenvalue $\lambda = 0$: $0\mathbf{I} - \mathbf{A} = \begin{pmatrix} -1 & -1 & 0 \\ -1 & -1 & 0 \\ 0 & 0 & 2 \end{pmatrix} \xrightarrow{RREF} \begin{pmatrix} 1 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}$ So, $E_0 = \text{span} \left\{ \begin{pmatrix} -1 \\ 1 \\ 0 \end{pmatrix} \right\}$.
for eigenvalue $\lambda = 2$: $2\mathbf{I} - \mathbf{A} = \begin{pmatrix} 1 & -1 & 0 \\ -1 & 1 & 0 \\ 0 & 0 & 0 \end{pmatrix} \xrightarrow{RREF} \begin{pmatrix} 1 & -1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$ So, $E_2 = \text{span} \left\{ \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} \right\}$.

$$A = \begin{pmatrix} x-1 & -1 & -1 \\ -1 & x-1 & -1 \\ -2 & -4 & x-2 \end{pmatrix} \to \det(A) = x^3 - 4x^2 - 2x$$
$$\hookrightarrow 2+\sqrt{6}, 2-\sqrt{6}, 0$$
$$A = \begin{pmatrix} x-5 & -1 & -2 \\ 0 & x-6 & 0 \\ -1 & 1 & x-4 \end{pmatrix}$$