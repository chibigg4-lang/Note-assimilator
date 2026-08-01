### Definition
Let **A** be a square matrix of order $n$, the *characteristic polynomial* of **A**, denoted as $\text{char}(\mathbf{A})$, is the degree $n$ polynomial
$$\det(x\mathbf{I} - \mathbf{A}).$$

### Example
1. Let $\mathbf{A} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$. $\det(x\mathbf{I}-\mathbf{A}) = \left| \begin{pmatrix} x & 0 \\ 0 & x \end{pmatrix} - \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \right| = \left| \begin{smallmatrix} x & -1 \\ -1 & x \end{smallmatrix} \right| = x^2 - 1$.
2. Let $\mathbf{A} = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$. $\det \left( \begin{pmatrix} x-1 & -1 \\ -1 & x-1 \end{pmatrix} \right) = \left| \begin{smallmatrix} x-1 & -1 \\ -1 & x-1 \end{smallmatrix} \right| = (x-1)^2 - 1 = x(x-2)$.
3. Let $\mathbf{A} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 2 \\ 0 & 3 & 1 \end{pmatrix}$. $\left| \begin{smallmatrix} x-1 & 0 & 0 \\ 0 & x & -2 \\ 0 & -3 & x-1 \end{smallmatrix} \right| = (x-1)[x(x-1)-6] = (x-1)(x+2)(x-3)$.

---

**Definition**
Let $\lambda$ be an eigenvalue of **A**. The *algebraic multiplicity* of $\lambda$ is the largest integer $r_\lambda$ such that
$$\det(x\mathbf{I} - \mathbf{A}) = (x - \lambda)^{r_\lambda} p(x),$$
for some polynomial $p(x)$.
Alternatively, $r_\lambda$ is the positive integer such that in the above equation, $\lambda$ is not a root of $p(x)$.

Suppose **A** is an order $n$ square matrix such that $\det(x\mathbf{I} - \mathbf{A})$ can be factorize into linear factors completely.
Then we can write
$$\det(x\mathbf{I} - \mathbf{A}) = (x - \lambda_1)^{r_1} (x - \lambda_2)^{r_2} \cdots (x - \lambda_k)^{r_k}$$
where $r_1 + r_2 + \cdots + r_k = n$, and $\lambda_1, \lambda_2, \dots, \lambda_k$ are the distinct eigenvalues of **A**.
Then the algebraic multiplicity of $\lambda_i$ is $r_i$ for $i = 1, \dots, k$.

**Theorem**
The eigenvaules of a triangular matrix are the diagonal entries. The algebraic multiplicity of the eigenvalue is the number of times it appears as a diagonal entry of **A**.

---

1. Let $\mathbf{A} = \mathbf{0}_n$ be the order $n$ zero matrix. Then $\det(x\mathbf{I} - \mathbf{0}) = \det(x\mathbf{I}) = x^n$. $\lambda = 0$ is the only eigenvalue of **A**, with algebraic multiplicity $r_0 = n$.
2. $\mathbf{A} = \begin{pmatrix} 1 & 2 & 5 \\ 0 & 1 & -2 \\ 0 & 0 & 3 \end{pmatrix}$. $\det(x\mathbf{I} - \mathbf{A}) = (x - 1)^2(x - 3)$. The eigenvalues of **A** are $\lambda = 1, 3$, with algebraic multiplicities $r_1 = 2, r_3 = 1$, respectively.
3. $\mathbf{A} = \begin{pmatrix} 3 & 1 & -1 \\ 1 & 3 & -1 \\ 0 & 0 & 2 \end{pmatrix}$. Then $\det(x\mathbf{I} - \mathbf{A}) = (x - 2)^2(x - 4)$. The eigenvalues are $\lambda = 2, 4$, with algebraic multiplicities $r_2 = 2, r_4 = 1$, respectively.
4. $\mathbf{A} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & -1 \\ 0 & 1 & 0 \end{pmatrix}$. Then $\det(x\mathbf{I} - \mathbf{A}) = (x - 1)(x^2 + 1)$. The eigenvalue is $\lambda = 1$ only, with algebraic multiplicity $r_1 = 1$. In this case **A** has only one (real) eigenvalue.