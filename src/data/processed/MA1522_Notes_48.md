# Orthogonality

Two vectors $\mathbf{u}, \mathbf{v}$ in $\mathbb{R}^n$ are orthogonal if
$$\mathbf{u} \cdot \mathbf{v} = 0.$$
In this case, either one of the vectors is the zero vector, or that they are perpendicular.

### Definition
A set $S = \{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_k\}$ of vectors is orthogonal if $\mathbf{v}_i \cdot \mathbf{v}_j = 0$ for every $i \neq j$, that is, vectors in $S$ are pairwise orthogonal.
A set $S = \{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_k\}$ of vectors is orthonormal if for all $i, j = 1, \dots, k$,
$$\mathbf{v}_i \cdot \mathbf{v}_j = \begin{cases} 0 & \text{if } i \neq j, \\ 1 & \text{if } i = j. \end{cases}$$
That is, $S$ is orthogonal, and all the vectors are unit vectors.

---

### Example
Let $V$ be a subspace spanned by $S = \left\{ \mathbf{u}_1 = \begin{pmatrix} 1 \\ 1 \\ 1 \\ 2 \end{pmatrix}, \mathbf{u}_2 = \begin{pmatrix} 0 \\ 1 \\ -1 \\ 0 \end{pmatrix} \right\}$. A vector $\mathbf{w} = \begin{pmatrix} w_1 \\ w_2 \\ w_3 \\ w_4 \end{pmatrix}$ is orthogonal to $V$ if and only if $\mathbf{w} \cdot \mathbf{u}_1 = w_1 + w_2 + w_3 + 2w_4 = 0$ and $\mathbf{w} \cdot \mathbf{u}_2 = w_2 - w_3 = 0$. That is,
$$\begin{cases} w_1 + w_2 + w_3 + 2w_4 &= 0 \\ w_2 - w_3 &= 0 \end{cases} \text{ or } \begin{pmatrix} 1 & 1 & 1 & 2 \\ 0 & 1 & -1 & 0 \end{pmatrix} \mathbf{w} = \mathbf{0}.$$
Observe that the rows of the coefficient matrix are the vectors in $S$, $\mathbf{A} = \begin{pmatrix} 1 & 1 & 1 & 2 \\ 0 & 1 & -1 & 0 \end{pmatrix} = \begin{pmatrix} \mathbf{u}_1^T \\ \mathbf{u}_2^T \end{pmatrix}$. Solving the system,
$$\begin{pmatrix} 1 & 1 & 1 & 2 & | & 0 \\ 0 & 1 & -1 & 0 & | & 0 \end{pmatrix} \xrightarrow{RREF} \begin{pmatrix} 1 & 0 & 2 & 2 & | & 0 \\ 0 & 1 & -1 & 0 & | & 0 \end{pmatrix}$$
we conclude that $\mathbf{w}$ is orthogonal to $V$ is and only if it is in $\text{span} \left\{ \begin{pmatrix} -2 \\ 1 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} -2 \\ 0 \\ 0 \\ 1 \end{pmatrix} \right\}$.

---

Let $V$ be a subspace of $\mathbb{R}^n$. A vector $\mathbf{n} \in \mathbb{R}^n$ is orthogonal to $V$ if for every $\mathbf{v}$ in $V$, $\mathbf{n} \cdot \mathbf{v} = 0$, that is, $\mathbf{n}$ is orthogonal to every vector in $V$. We will denote it as $\mathbf{n} \perp V$.

### Theorem
Let $V$ be a subspace of $\mathbb{R}^n$ and $S = \{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_k\}$ be a spanning set for $V$, $\text{span}(S) = V$. Then a vector $\mathbf{w}$ is orthogonal to $V$ if and only if $\mathbf{w} \cdot \mathbf{u}_i = 0$ for all $i = 1, \dots, k$.

### Theorem
Let $V$ be a subspace of $\mathbb{R}^n$ and $S = \{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_k\}$ be a spanning set for $V$. Then $\mathbf{w}$ is orthogonal to $V$ if and only if $\mathbf{w}$ is in the nullspace of $\mathbf{A}^T$, where $\mathbf{A} = \begin{pmatrix} \mathbf{u}_1 & \mathbf{u}_2 & \cdots & \mathbf{u}_k \end{pmatrix}$;
$$\mathbf{w} \perp V \iff \mathbf{w} \in \text{Null}(\mathbf{A}^T).$$

### Orthogonal Complement
### Definition
Let $V$ be a subspace of $\mathbb{R}^n$. The orthogonal complement of $V$ is the set of all vectors that are orthogonal to $V$, and is denoted as
$$V^\perp = \{ \mathbf{w} \in \mathbb{R}^n \mid \mathbf{w} \cdot \mathbf{v} = 0 \text{ for all } \mathbf{v} \in V \}.$$

### Theorem
Let $V$ be a subspace of $\mathbb{R}^n$ and $S = \{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_k\}$ be a spanning set for $V$. Let $\mathbf{A} = \begin{pmatrix} \mathbf{u}_1 & \mathbf{u}_2 & \cdots & \mathbf{u}_k \end{pmatrix}$. Then the orthogonal complement of $V$ is the nullspace of $\mathbf{A}^T$.
$$V^\perp = \text{Null}(\mathbf{A}^T).$$

### Challenge
Let $\mathbf{A}$ be a $m \times n$ matrix. Show that the nullspace of $\mathbf{A}$ is the orthogonal complement of the row space of $\mathbf{A}$,
$$\text{Row}(\mathbf{A})^\perp = \text{Null}(\mathbf{A}).$$