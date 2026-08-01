# Diagonalization

## Diagonalization

That is, **A** is diagonalizable if and only if we can find

$$ \mathbf{P} = \begin{pmatrix} \mathbf{u}_1 & \mathbf{u}_2 & \cdots & \mathbf{u}_n \end{pmatrix}, \text{ and } \mathbf{D} = \begin{pmatrix} \mu_1 & 0 & \cdots & 0 \\ 0 & \mu_2 & \cdots & 0 \\ \vdots & & \ddots & \vdots \\ 0 & 0 & \cdots & \mu_n \end{pmatrix}, $$

where $\mu_i$ is the eigenvalue associated to eigenvector $\mathbf{u}_i$, $i = 1, ..., n$, $\mathbf{A}\mathbf{u}_i = \mu_i\mathbf{u}_i$.

**P** is invertible if and only if $\{\mathbf{u}_1, \mathbf{u}_2, ..., \mathbf{u}_n\}$ is a basis for $\mathbb{R}^n$.

Note that $\mu_i$ may not be distinct.

---

That is, **A** is diagonalizable if and only if we can find

$$ \mathbf{P} = \begin{pmatrix} \mathbf{u}_1 & \mathbf{u}_2 & \cdots & \mathbf{u}_n \end{pmatrix}, \text{ and } \mathbf{D} = \begin{pmatrix} \mu_1 & 0 & \cdots & 0 \\ 0 & \mu_2 & \cdots & 0 \\ \vdots & & \ddots & \vdots \\ 0 & 0 & \cdots & \mu_n \end{pmatrix}, $$

where $\mu_i$ is the eigenvalue associated to eigenvector $\mathbf{u}_i$, $i = 1, ..., n$, $\mathbf{A}\mathbf{u}_i = \mu_i\mathbf{u}_i$.

**P** is invertible if and only if $\{\mathbf{u}_1, \mathbf{u}_2, ..., \mathbf{u}_n\}$ is a basis for $\mathbb{R}^n$.

Note that $\mu_i$ may not be distinct.

## Not Diagonalizable

Not all square matrices are diagonalizable. For example, consider

$$ \mathbf{A} = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}. $$

This is a triangular matrix, with only one eigenvalue $\lambda = 0$.

$$ 0\mathbf{I} - \mathbf{A} = \begin{pmatrix} 0 & -1 \\ 0 & 0 \end{pmatrix} \xrightarrow{RREF} \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} $$

tells us that **A** has only 1 linearly independent eigenvector associated to the only eigenvalue $\lambda = 0$. Hence, **A** is not diagonalizable.