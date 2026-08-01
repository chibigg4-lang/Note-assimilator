Explicitly,

$$\mathbf{a}_1 = r_{11}\mathbf{q}_1 = (\mathbf{q}_1 \quad \dots \quad \mathbf{q}_n) \begin{pmatrix} r_{11} \\ 0 \\ \vdots \\ 0 \end{pmatrix}$$

$$\mathbf{a}_2 = r_{12}\mathbf{q}_1 + r_{22}\mathbf{q}_2 = (\mathbf{q}_1 \quad \dots \quad \mathbf{q}_n) \begin{pmatrix} r_{12} \\ r_{22} \\ \vdots \\ 0 \end{pmatrix}$$

$$\vdots$$

$$\mathbf{a}_n = r_{1n}\mathbf{q}_1 + r_{2n}\mathbf{q}_2 + \dots + r_{nn}\mathbf{q}_n = (\mathbf{q}_1 \quad \dots \quad \mathbf{q}_n) \begin{pmatrix} r_{1n} \\ r_{2n} \\ \vdots \\ r_{nn} \end{pmatrix}$$

Thus, we may write

$$\mathbf{A} = (\mathbf{a}_1 \quad \mathbf{a}_2 \quad \dots \quad \mathbf{a}_n)$$
$$= (\mathbf{q}_1 \quad \mathbf{q}_2 \quad \dots \quad \mathbf{q}_n) \begin{pmatrix} r_{11} & r_{12} & \dots & r_{1n} \\ 0 & r_{22} & \dots & r_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & r_{nn} \end{pmatrix}$$
$$= \mathbf{QR}$$

for some $m \times n$ matrix $\mathbf{Q}$ with orthonormal columns, and a upper triangular $n \times n$ matrix $\mathbf{R}$.

**Exercise**

1. Prove that $\mathbf{Q}^T\mathbf{Q} = \mathbf{I}_n$.
2. Prove that the diagonal entries of $\mathbf{R}$ are positive, $r_{ii} > 0$ for all $i = 1, \dots, n$.
3. Prove that the upper triangular matrix $\mathbf{R} = \begin{pmatrix} r_{11} & r_{12} & \dots & r_{1n} \\ 0 & r_{22} & \dots & r_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & r_{nn} \end{pmatrix}$ is invertible.

**Theorem** (QR Factorization)

Suppose $\mathbf{A}$ is a $m \times n$ matrix with linearly independent columns. Then $\mathbf{A}$ can be written as

$$\mathbf{A} = \mathbf{QR}$$

for some $m \times n$ matrix $\mathbf{Q}$ such that $\mathbf{Q}^T\mathbf{Q} = \mathbf{I}_n$ and invertible upper triangular matrix $\mathbf{R}$ with positive diagonal entries.

**Definition**

The decomposition given in the theorem above is called a **QR factorization** of $\mathbf{A}$.

**Algorithm to QR Factorization**

Let $\mathbf{A}$ be a $m \times n$ matrix with linearly independent columns.
1. Perform Gram-Schmidt on the columns of $\mathbf{A} = (\mathbf{a}_1 \quad \mathbf{a}_2 \quad \dots \quad \mathbf{a}_n)$ to obtain an orthonormal set $\{\mathbf{q}_1, \mathbf{q}_2, \dots, \mathbf{q}_n\}$.
2. Set $\mathbf{Q} = (\mathbf{q}_1 \quad \mathbf{q}_2 \quad \dots \quad \mathbf{q}_n)$.
3. Compute $\mathbf{R} = \mathbf{Q}^T\mathbf{A}$.

**Exercise**

Use QR factorization to prove the following.

**Corollary**

Suppose $\mathbf{A}$ is a $m \times n$ matrix with linearly independent columns, i.e. $rank(\mathbf{A}) = n$. Then $\mathbf{A}^T\mathbf{A}$ is invertible, and $\mathbf{A}$ has a left inverse; that is, there is a $\mathbf{B}$ such that

$$\mathbf{BA} = \mathbf{I}_n.$$