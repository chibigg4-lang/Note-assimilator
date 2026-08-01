Example
Let $\mathbf{A} = \begin{pmatrix} 3 & 1 & -1 \\ 1 & 3 & -1 \\ 0 & 0 & 2 \end{pmatrix}$. The characteristic polynomial is
$$x\mathbf{I} - \mathbf{A} = \begin{vmatrix} x-3 & -1 & 1 \\ -1 & x-3 & 1 \\ 0 & 0 & x-2 \end{vmatrix} = (x-2)[(x-3)^2 - 1] = (x-2)(x^2-6x+8) = (x-2)(x-2)(x-4).$$
$\lambda = 2, 4$ , $r_2=2, r_4=1$
$1 \le \dim(E_4) \le r_4=1 \implies \dim(E_4)=1=r_4$.

Find a basis for the eigenspaces.
$2\mathbf{I} - \mathbf{A} = \begin{pmatrix} -1 & -1 & 1 \\ -1 & -1 & 1 \\ 0 & 0 & 0 \end{pmatrix} \xrightarrow{RREF} \begin{pmatrix} 1 & 1 & -1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$. So, $\left\{ \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix} \right\}$ is a basis for $E_2$, and $\dim(E_2) = 2 = r_2$.
$4\mathbf{I} - \mathbf{A} = \begin{pmatrix} 1 & -1 & 1 \\ -1 & 1 & 1 \\ 0 & 0 & 2 \end{pmatrix} \xrightarrow{RREF} \begin{pmatrix} 1 & -1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}$. So, $\left\{ \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} \right\}$ is a basis for $E_4$, and $\dim(E_4) = 2 = r_4$.
$\mathbf{A}$ is diagonalizable with
$$\begin{pmatrix} 3 & 1 & -1 \\ 1 & 3 & -1 \\ 0 & 0 & 2 \end{pmatrix} = \overbrace{\begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 1 & 1 & 0 \end{pmatrix}}^{P} \overbrace{\begin{pmatrix} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 4 \end{pmatrix}}^{D} \overbrace{\begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 1 & 1 & 0 \end{pmatrix}^{-1}}^{P^{-1}}$$

---

Not Diagonalizable

A square matrix $\mathbf{A}$ is diagonalizable if
(i) The characteristic polynomial splits into linear factors,
$$\det(x\mathbf{I} - \mathbf{A}) = (x - \lambda_1)^{r_{\lambda_1}} (x - \lambda_2)^{r_{\lambda_2}} \cdots (x - \lambda_k)^{r_{\lambda_k}},$$
(ii) and the algebraic multiplicity is equal to the geometric multiplicity,
$$r_\lambda = \dim(E_\lambda),$$
for every eigenvalue $\lambda$ of $\mathbf{A}$.

To show that a square matrix $\mathbf{A}$ of order $n$ is not diagonalizable, show that either
(i) $\det(x\mathbf{I} - \mathbf{A})$ does not split into linear factors, or
(ii) there exists an eigenvalue $\lambda$ such that $\dim(E_\lambda) < r_\lambda$.

---

Suppose $\mathbf{A}$ is a $n \times n$ matrix with $n > 1$. Show that if $\mathbf{A}$ has only 1 eigenvalue $\lambda$, then $\mathbf{A}$ is diagonalizable if and only if $\mathbf{A}$ is the scalar matrix, $\mathbf{A} = \lambda\mathbf{I}_n$.

Hence, all non-scalar matrix with only 1 eigenvalue is not diagonalizable.