Example
$$\mathbf{A} = \begin{pmatrix} 1 & 1 & 1 \\ 0 & 2 & 2 \\ 0 & 0 & 3 \end{pmatrix}.$$ Eigenvalues are: $\lambda = 1, 2, 3$.

$$\lambda = 1: \begin{pmatrix} 0 & -1 & -1 \\ 0 & -1 & -2 \\ 0 & 0 & -2 \end{pmatrix} \rightarrow \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix} \Rightarrow E_1 = \text{span} \left\{ \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} \right\}$$

$$\lambda = 2: \begin{pmatrix} 1 & -1 & -1 \\ 0 & 0 & -2 \\ 0 & 0 & -1 \end{pmatrix} \rightarrow \begin{pmatrix} 1 & -1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix} \Rightarrow E_2 = \text{span} \left\{ \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} \right\}$$

$$\lambda = 3: \begin{pmatrix} 2 & -1 & -1 \\ 0 & 1 & -2 \\ 0 & 0 & 0 \end{pmatrix} \rightarrow \begin{pmatrix} 2 & 0 & -3 \\ 0 & 1 & -2 \\ 0 & 0 & 0 \end{pmatrix} \Rightarrow E_3 = \text{span} \left\{ \begin{pmatrix} 3 \\ 4 \\ 2 \end{pmatrix} \right\}$$

$$\Rightarrow \mathbf{A} = \begin{pmatrix} 1 & 1 & 3 \\ 0 & 1 & 4 \\ 0 & 0 & 2 \end{pmatrix} \begin{pmatrix} 1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 3 \end{pmatrix} \begin{pmatrix} 1 & 1 & 3 \\ 0 & 1 & 4 \\ 0 & 0 & 2 \end{pmatrix}^{-1}$$

Algorithm to Diagonalization

Let $\mathbf{A}$ be an order $n$ square matrix.
1. Compute the characteristic polynomial
$$\text{det}(x\mathbf{I} - \mathbf{A}) = (x - \lambda_1)^{r_1} (x - \lambda_2)^{r_2} \cdots (x - \lambda_k)^{r_k}.$$
If the characteristic polynomial do not split into linear factors, $\mathbf{A}$ is not diagonalizable.
2. For each eigenvalue $\lambda_i$ of $\mathbf{A}$, $i = 1, ..., k$, find a basis $S_{\lambda_i}$ for the eigenspace, that is, find a basis $S_{\lambda_i}$ for the solution space of the following linear system,
$$(\lambda_i\mathbf{I} - \mathbf{A})\mathbf{x} = \mathbf{0}.$$
Compute first the eigenspace associated to eigenvalues with algebraic multiplicity greater than 1. If $\dim(E_\lambda) < r_\lambda$, $\mathbf{A}$ is not diagonalizable.
3. Let $S = \cup_{i=1}^k S_{\lambda_i}$. Then $S = \{\mathbf{u}_1, \mathbf{u}_2, ..., \mathbf{u}_n\}$ is a basis for $\mathbb{R}^n$ consisting of eigenvectors of $\mathbf{A}$.
4. Let $\mathbf{P} = (\mathbf{u}_1 \ \mathbf{u}_2 \ \cdots \ \mathbf{u}_n)$, and $\mathbf{D} = \text{diag}(\mu_1, \mu_2, ..., \mu_n)$, where $\mu_i$ is the eigenvalue associated to $\mathbf{u}_i$, $i = 1, ..., n$, $\mathbf{A}\mathbf{u}_i = \mu_i\mathbf{u}_i$. Then
$$\mathbf{A} = \mathbf{P}\mathbf{D}\mathbf{P}^{-1}.$$

Example
Let $\mathbf{A} = \begin{pmatrix} 1 & 1 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 2 \end{pmatrix}.$
The characteristic polynomial is $\left| \begin{matrix} x-1 & -1 & 0 \\ -1 & x-1 & 0 \\ 0 & 0 & x-2 \end{matrix} \right| = x(x-2)^2$. So, the eigenvalues are $\lambda = 0, 2$ with algebraic multiplicities, $r_0 = 1, r_2 = 2$, respectively. Now find a basis for the eigenspaces.
▶ $2\mathbf{I} - \mathbf{A} = \begin{pmatrix} 1 & -1 & 0 \\ -1 & 1 & 0 \\ 0 & 0 & 0 \end{pmatrix} \xrightarrow{\text{RREF}} \begin{pmatrix} 1 & -1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$. So, $E_2 = \text{span} \left\{ \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} \right\}$
▶ $0\mathbf{I} - \mathbf{A} = \begin{pmatrix} -1 & -1 & 0 \\ -1 & -1 & 0 \\ 0 & 0 & 2 \end{pmatrix} \xrightarrow{\text{RREF}} \begin{pmatrix} 1 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}$. So, $E_0 = \text{span} \left\{ \begin{pmatrix} -1 \\ 1 \\ 0 \end{pmatrix} \right\}$
Hence, $\mathbf{A}$ is diagonalizable, with
$$\mathbf{A} = \begin{pmatrix} -1 & 1 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 0 \end{pmatrix} \begin{pmatrix} -1 & 1 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}^{-1}$$