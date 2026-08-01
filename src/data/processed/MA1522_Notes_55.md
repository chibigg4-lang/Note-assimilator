Let $\mathbf{A} = \begin{pmatrix} 1 & 1 & 0 & 1 \\ 0 & 1 & 1 & 0 \\ 1 & 2 & 1 & 1 \end{pmatrix}$ and $\mathbf{b} = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}$. Find a least square solution of $\mathbf{Ax} = \mathbf{b}$, that is, solve $\mathbf{A}^T\mathbf{Ax} = \mathbf{A}^T\mathbf{b}$.

$$\mathbf{A}^T\mathbf{A} = \begin{pmatrix} 2 & 3 & 1 & 2 \\ 3 & 6 & 3 & 3 \\ 1 & 3 & 2 & 1 \\ 2 & 3 & 1 & 2 \end{pmatrix}, \mathbf{A}^T\mathbf{b} = \begin{pmatrix} 2 \\ 4 \\ 2 \\ 2 \end{pmatrix}$$

$$\begin{pmatrix} 2 & 3 & 1 & 2 & 2 \\ 3 & 6 & 3 & 3 & 4 \\ 1 & 3 & 2 & 1 & 2 \\ 2 & 3 & 1 & 2 & 2 \end{pmatrix} \xrightarrow{RREF} \begin{pmatrix} 1 & 0 & -1 & 1 & 0 \\ 0 & 1 & 1 & 0 & 2/3 \\ 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{pmatrix}$$

General solution: $\begin{pmatrix} 0 \\ 2/3 \\ 0 \\ 0 \end{pmatrix} + s \begin{pmatrix} 1 \\ -1 \\ 1 \\ 0 \end{pmatrix} + t \begin{pmatrix} -1 \\ 0 \\ 0 \\ 1 \end{pmatrix}, s, t \in \mathbb{R}$. This shows that least square solution might not be unique.

---

### Example

Find the least square solutions to
$$\begin{cases} x & - & y & + & z & = & 1 \\ -x & + & y & + & z & = & 2 \\ x & & & + & z & = & 2 \\ -x & + & y & - & z & = & -1 \end{cases}$$

$$(\mathbf{A}^T\mathbf{A} \mid \mathbf{A}^T\mathbf{b}) = \begin{pmatrix} 4 & -3 & 2 & 2 \\ -3 & 3 & -1 & 0 \\ 2 & -1 & 4 & 6 \end{pmatrix} \xrightarrow{RREF} \begin{pmatrix} 1 & 0 & 0 & 1/2 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & 3/2 \end{pmatrix}$$

Unique least square solution: $\begin{pmatrix} 1/2 \\ 1 \\ 3/2 \end{pmatrix}$.

In this case, observe that $\mathbf{A}^T\mathbf{A}$ is invertible. So, could have computed the least square solution by

$$\mathbf{u} = (\mathbf{A}^T\mathbf{A})^{-1}\mathbf{A}^T\mathbf{b} = \begin{pmatrix} 11/8 & 5/4 & -3/8 \\ 5/4 & 3/2 & -1/4 \\ -3/8 & -1/4 & 3/8 \end{pmatrix} \begin{pmatrix} 2 \\ 0 \\ 6 \end{pmatrix} = \begin{pmatrix} 1/2 \\ 1 \\ 3/2 \end{pmatrix}$$

---

### Orthogonal Projection (Revisit)
We may use least square solutions to find the projection of a vector onto a subspace.

* Let $V$ be subspace of $\mathbb{R}^n$. Let $S = \{\mathbf{u}_1, \dots, \mathbf{u}_k\}$ be a basis for $V$.
* Define $\mathbf{A} = \begin{pmatrix} \mathbf{u}_1 & \dots & \mathbf{u}_k \end{pmatrix}$, by construction, the column space of $\mathbf{A}$ is $V$, $V = \text{Col}(\mathbf{A})$.
* Let $\mathbf{w}$ be a vector in $\mathbb{R}^n$, and $\mathbf{u}$ a least square solution to $\mathbf{Ax} = \mathbf{w}$. Then $\mathbf{w}_p = \mathbf{Au}$ is the projection of $\mathbf{w}$ onto $\text{Col}(\mathbf{A}) = V$.

[Image of a geometric projection showing vector w projecting onto a plane labeled V=span{u1,...,uk} = Col(A=(u1 ... uk)) resulting in wp = Au = A(A^TA)^-1A^Tw]