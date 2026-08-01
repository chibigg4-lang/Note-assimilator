Independence of Eigenspaces

Suppose $\lambda_1$ and $\lambda_2$ are distinct eigenvalues. Let $\mathbf{v}_1$ be an eigenvector associated to eigenvalue $\lambda_1$. Then since $\lambda_1 \neq \lambda_2$,
$$\mathbf{A}\mathbf{v}_1 = \lambda_1\mathbf{v}_1 \neq \lambda_2\mathbf{v}_1,$$
$\mathbf{v}_1$ cannot be in the eigenspace associated to $\lambda_2$. This demonstrates that vectors from different eigenspaces are linearly independent. The proof of the following theorem is given in the appendix.

Theorem (Eigenspaces are linearly independent)
Let $\mathbf{A}$ be a $n \times n$ square matrix. Let $\lambda_1$ and $\lambda_2$ are distinct eigenvalues of $\mathbf{A}$, $\lambda_1 \neq \lambda_2$. Suppose $\{\mathbf{u}_1, \dots, \mathbf{u}_k\}$ is a linearly independent subset of eigenspace associated to eigenvalue $\lambda_1$, and $\{\mathbf{v}_1, \dots, \mathbf{v}_m\}$ is a linearly independent subset of of eigenspace associated to eigenvalue $\lambda_2$. Then the union $\{\mathbf{u}_1, \dots, \mathbf{u}_k, \mathbf{v}_1, \dots, \mathbf{v}_m\}$ is linearly independent.

---

Is it possible for the geometric multiplicity to be $0$, $\dim(E_\lambda) = 0$?

$\lambda$ eigenvalue of $A \Rightarrow Av = \lambda v$, $v \neq 0$ $\Leftrightarrow$ $(\lambda I - A)v = 0$ $\neq 0$.

geometric multiplicity = $\text{nullity}(\lambda I - A) = \dim(E_\lambda) \ge 1$

---

Equivalent Statements for Diagonalizability

Theorem
Let $\mathbf{A}$ be a square matrix of order $n$. The following statements are equivalent.
(i) $\mathbf{A}$ is diagonalizable.
(ii) There exists a basis $\{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n\}$ of $\mathbb{R}^n$ of eigenvectors of $\mathbf{A}$.
(iii) The characteristic polynomial of $\mathbf{A}$ splits into linear factors,
$$\det(x\mathbf{I} - \mathbf{A}) = (x - \lambda_1)^{r_{\lambda_1}} (x - \lambda_2)^{r_{\lambda_2}} \dots (x - \lambda_k)^{r_{\lambda_k}},$$
where $r_{\lambda_i}$ is the algebraic multiplicity of $\lambda_i$, for $i = 1, \dots, k$, and the eigenvalues are distinct, $\lambda_i \neq \lambda_j$ for all $i \neq j$, and the geometric multiplicity is equal to the algebraic multiplicity for each eigenvalue $\lambda_i$,
$$\dim(E_{\lambda_i}) = r_{\lambda_i}.$$