Orthogonal Projection (Revisit)

* Now $\mathbf{u}$ is a least square solution to $\mathbf{A}\mathbf{x} = \mathbf{w}$ if and only if it is a solution to $\mathbf{A}^\mathsf{T}\mathbf{A}\mathbf{x} = \mathbf{A}^\mathsf{T}\mathbf{w}$. But since the columns of $\mathbf{A}$ are linearly independent, $\mathbf{A}^\mathsf{T}\mathbf{A}$ is invertible.
* This means that $\mathbf{u} = (\mathbf{A}^\mathsf{T}\mathbf{A})^{-1}\mathbf{A}^\mathsf{T}\mathbf{w}$.
* Hence, the projection is 
$$\mathbf{w}_p = \mathbf{A}(\mathbf{A}^\mathsf{T}\mathbf{A})^{-1}\mathbf{A}^\mathsf{T}\mathbf{w}.$$

Theorem
Let $V$ be a subspace of $\mathbb{R}^n$ and $S = \{\mathbf{u}_1, \mathbf{u}_2, ..., \mathbf{u}_k\}$ be a basis for $V$. Then the orthogonal projection of a vector $\mathbf{w}$ onto $V$ is
$$\mathbf{w}_p = \mathbf{A}(\mathbf{A}^\mathsf{T}\mathbf{A})^{-1}\mathbf{A}^\mathsf{T}\mathbf{w},$$
where $\mathbf{A} = \begin{pmatrix} \mathbf{u}_1 & \mathbf{u}_2 & \cdots & \mathbf{u}_k \end{pmatrix}$.

$(\mathbf{A}^\mathsf{T}\mathbf{A})^{-1}\mathbf{A}^\mathsf{T}\mathbf{b}$ is the unique solution to $\mathbf{A}\mathbf{x}=\mathbf{b}$

---

Examples

Let $S = \left\{ \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 1 \\ -1 \\ 0 \end{pmatrix} \right\}$ and $V = \text{span}(S)$. Let $\mathbf{A} = \begin{pmatrix} 1 & 1 \\ 1 & -1 \\ 0 & 0 \end{pmatrix}$. Then the orthogonal projection of $\mathbf{w} = \begin{pmatrix} x \\ y \\ z \end{pmatrix}$ onto $V$ is

$$\mathbf{A}(\mathbf{A}^\mathsf{T}\mathbf{A})^{-1}\mathbf{A}^\mathsf{T}\mathbf{w} = \begin{pmatrix} 1 & 1 \\ 1 & -1 \\ 0 & 0 \end{pmatrix} \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}^{-1} \begin{pmatrix} x+y \\ x-y \end{pmatrix}$$
$$= \begin{pmatrix} 1/2 & 1/2 \\ 1/2 & -1/2 \\ 0 & 0 \end{pmatrix} \begin{pmatrix} x+y \\ x-y \end{pmatrix}$$
$$= \begin{pmatrix} x \\ y \\ 0 \end{pmatrix}.$$

Indeed, since $V$ is the $xy$-plane in $\mathbb{R}^3$.