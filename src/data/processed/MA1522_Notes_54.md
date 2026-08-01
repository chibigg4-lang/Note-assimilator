# Least Square Approximation

### Definition
Let $\mathbf{A}$ be a $m \times n$ matrix and $\mathbf{b}$ a vector in $\mathbb{R}^m$. A vector $\mathbf{u}$ in $\mathbb{R}^n$ is a *least square solution* of $\mathbf{Ax} = \mathbf{b}$ if for every vector $\mathbf{v} \in \mathbb{R}^n$,
$$\|\mathbf{Au} - \mathbf{b}\| \leq \|\mathbf{Av} - \mathbf{b}\|.$$

### Theorem
Let $\mathbf{A}$ be a $m \times n$ matrix and $\mathbf{b}$ a vector in $\mathbb{R}^m$. A vector $\mathbf{u}$ in $\mathbb{R}^n$ is a least square solution to $\mathbf{Ax} = \mathbf{b}$ if and only if $\mathbf{Au}$ is the projection of $\mathbf{b}$ onto the column space of $Col(\mathbf{A})$.

### Theorem
Let $\mathbf{A}$ be a $m \times n$ matrix and $\mathbf{b}$ a vector in $\mathbb{R}^m$. A vector $\mathbf{u}$ in $\mathbb{R}^n$ is a least square solution to $\mathbf{Ax} = \mathbf{b}$ if and only if $\mathbf{u}$ is a solution to $\mathbf{A}^T\mathbf{Ax} = \mathbf{A}^T\mathbf{b}$.

### Remark.
Least square solutions are not unique, but projection is unique.

### Challenge
Let $\mathbf{A}$ be a $m \times n$ matrix and $\mathbf{b}$ a vector in $\mathbb{R}^m$.
Prove that for any choice of least square solution $\mathbf{u}$, that is, for any solution $\mathbf{u}$ of $\mathbf{A}^T\mathbf{Ax} = \mathbf{A}^T\mathbf{b}$, the projection $\mathbf{Au}$ is unique.

***

Let $\mathbf{A} = \begin{pmatrix} 1 & 1 & 0 & 1 \\ 0 & 1 & 1 & 0 \\ 1 & 2 & 1 & 1 \end{pmatrix}$ and $\mathbf{b} = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}$. Find a least square solution of $\mathbf{Ax} = \mathbf{b}$, that is, solve $\mathbf{A}^T\mathbf{Ax} = \mathbf{A}^T\mathbf{b}$.

General solution to $\mathbf{A}^T\mathbf{Ax} = \mathbf{A}^T\mathbf{b}$:
$$\begin{pmatrix} 0 \\ 2/3 \\ 0 \\ 0 \end{pmatrix} + s \begin{pmatrix} 1 \\ -1 \\ 1 \\ 0 \end{pmatrix} + t \begin{pmatrix} -1 \\ 0 \\ 0 \\ 1 \end{pmatrix}, s, t \in \mathbb{R}.$$

Now for any $s, t \in \mathbb{R}$,
$$\mathbf{A} \left( \begin{pmatrix} 0 \\ 2/3 \\ 0 \\ 0 \end{pmatrix} + s \begin{pmatrix} 1 \\ -1 \\ 1 \\ 0 \end{pmatrix} + t \begin{pmatrix} -1 \\ 0 \\ 0 \\ 1 \end{pmatrix} \right) = \mathbf{A} \begin{pmatrix} 0 \\ 2/3 \\ 0 \\ 0 \end{pmatrix} = \frac{2}{3} \begin{pmatrix} 1 \\ 1 \\ 2 \end{pmatrix}.$$

So, for any choice of least square solution $\mathbf{u}$, the projection $\mathbf{Au}$ is unique.