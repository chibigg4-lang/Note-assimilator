**Theorem**
Let $V$ be a subspace of $\mathbb{R}^n$ and $B$ a basis for $V$. Suppose $B$ contains $k$ vectors, $|B| = k$. Let $\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_m$ be vectors in $V$. Then
1. $\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_m$ is linearly independent (respectively, dependent) if and only if $[\mathbf{v}_1]_B, [\mathbf{v}_2]_B, \dots, [\mathbf{v}_m]_B$ is linearly independent (respectively, dependent) in $\mathbb{R}^k$; and
2. $\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_m\}$ spans $V$ if and only if $\{[\mathbf{v}_1]_B, [\mathbf{v}_2]_B, \dots, [\mathbf{v}_m]_B\}$ spans $\mathbb{R}^k$.

**Corollary**
Let $V$ be a subspace of $\mathbb{R}^n$ and $B$ a basis for $V$. Suppose $B$ contains $k$ vectors, $|B| = k$.
1. If $S = \{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_m\}$ is a subset of $V$ with $m > k$, then $S$ is linearly dependent.
2. If $S = \{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_m\}$ is a subset of $V$ with $m < k$, then $S$ cannot span $V$.

**Corollary**
Suppose $S = \{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_k\}$ and $T = \{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_m\}$ are bases for a subspace $V \subseteq \mathbb{R}^n$. Then $k = m$.

**Definition**
Let $V$ be a subspace of $\mathbb{R}^n$. The dimension of $V$, denoted by $\dim(V)$, is defined to be the number of vectors in any basis of $V$.

**Theorem** (Dimension of solution space)
Let $\mathbf{A}$ be a $m \times n$ matrix. The number of non-pivot columns in the reduced row-echelon form of $\mathbf{A}$ is the dimension of the solution space
$$V = \{ \mathbf{u} \in \mathbb{R}^n \mid \mathbf{A}\mathbf{u} = \mathbf{0} \}.$$

**Theorem** (Spanning Set Theorem)
Let $S = \{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_k\}$ be a subset of vectors in $\mathbb{R}^n$, and let $V = \text{span}(S)$. Suppose $V$ is not the zero space, $V \neq \{\mathbf{0}\}$. Then there must be a subset of $S$ that is a basis for $V$.

**Theorem** (Linear Independence Theorem)
Let $V$ be a subspace of $\mathbb{R}^n$ and $S = \{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_k\}$ a linearly independent subset of $V, S \subseteq V$. Then there must be a set $T$ containing $S, S \subseteq T$ such that $T$ is a basis for $V$.

1. The dimension of the Euclidean $n$-space, $\mathbb{R}^n$ is $n$, since the standard basis $E = \{\mathbf{e}_1, \mathbf{e}_2, \dots, \mathbf{e}_n\}$ has $n$ vectors.
2. $V = \left\{ \begin{pmatrix} x \\ y \\ z \end{pmatrix} \mid z = 0 \right\}$ is 2-dimensional since the basis $\left\{ \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} \right\}$ has 2 vectors.
3. $V = \left\{ \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix} \mid a_1 x_1 + a_2 x_2 + \dots + a_n x_n = 0 \right\}$ is $n - 1$-dimensional if not all $a_i = 0$. This is called a hyperplane in $\mathbb{R}^n$.

**Theorem**
Let $U$ and $V$ be subspaces of $\mathbb{R}^n$.
1. If $U \subseteq V$, then $\dim(U) \leq \dim(V)$.
2. If $U \subseteq V$ and $U \neq V$, then $\dim(U) < \dim(V)$
That is, $U \subseteq V$, then $\dim(U) \leq \dim(V)$ with equality if and only if $U = V$.

**Theorem (B1)**
Let $V$ be a $k$-dimensional subspace of $\mathbb{R}^n, \dim(V) = k$. Suppose $S \subseteq V$ is a linearly independent subset containing $k$ vectors, $|S| = k$. Then $S$ is a basis for $V$.

**Theorem (B2)**
Let $V$ be a $k$ dimensional subspace of $\mathbb{R}^n, \dim(V) = k$. Suppose $S$ is a set containing $k$ vectors, $|S| = k$, such that $V \subseteq \text{span}(S)$. Then $S$ is a basis for $V$.

In summary, we have the following table for checking for basis:

| Definition | (B1) | (B2) |
| :--- | :--- | :--- |
| 1. $\text{span}(S) = V$ | 1. $|S| = \dim(V)$ | 1. $|S| = \dim(V)$ |
| 2. $S$ is linearly independent | 2. $S \subseteq V$ | 2. $V \subseteq \text{span}(S)$ |
| | 3. $S$ is linearly independent | |