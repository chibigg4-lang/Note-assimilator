# Column Space, Row space, and null space

Definition
Let $\mathbf{A}$ be an $m \times n$ matrix,
$$\mathbf{A} = \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{pmatrix}$$
The row space of $\mathbf{A}$ is the subspace of $\mathbb{R}^n$ spanned by the rows of $\mathbf{A}$.
$$\text{Row}(\mathbf{A}) = \text{span}\{(a_{11} \quad a_{12} \quad \cdots \quad a_{1n}), (a_{21} \quad a_{22} \quad \cdots \quad a_{2n}), \dots, (a_{m1} \quad a_{m2} \quad \cdots \quad a_{mn})\}$$
The column space of $\mathbf{A}$ is the subspace of $\mathbb{R}^m$ spanned by the columns of $\mathbf{A}$.
$$\text{Col}(\mathbf{A}) = \text{span}\left\{ \begin{pmatrix} a_{11} \\ a_{21} \\ \vdots \\ a_{m1} \end{pmatrix}, \begin{pmatrix} a_{12} \\ a_{22} \\ \vdots \\ a_{m2} \end{pmatrix}, \dots, \begin{pmatrix} a_{1n} \\ a_{2n} \\ \vdots \\ a_{mn} \end{pmatrix} \right\}$$
Remark: May write the vectors in row space as column vectors.

Finding basis for row space
Theorem (Row operations preserve row space)
Suppose $\mathbf{A}$ and $\mathbf{B}$ are row equivalent matrices. Then $\text{Row}(\mathbf{A}) = \text{Row}(\mathbf{B})$.
Theorem (Basis for row space)
For any matrix $\mathbf{A}$, the nonzero rows of the reduced row-echelon form of $\mathbf{A}$ form a basis for the row space of $\mathbf{A}$.

More on Column Space and Row Space

## Question

Let
$$\mathbf{A} = \begin{pmatrix} 2 & 1 & 4 & 1 & 2 \\ 4 & 2 & 2 & 3 & 2 \\ 2 & 1 & -2 & 2 & 0 \\ 6 & 3 & 6 & 4 & 4 \end{pmatrix} \xrightarrow{\text{RREF}} \mathbf{R} = \begin{pmatrix} 1 & 1/2 & 0 & 5/6 & 1/3 \\ 0 & 0 & 1 & -1/6 & 1/3 \\ 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{pmatrix}$$
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$r$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$s$ &nbsp;&nbsp;&nbsp;$t$

1. Find a basis for the nullspace of $\mathbf{A}$.
$$\text{Basis} : \left\{ \begin{pmatrix} -1/2 \\ 1 \\ 0 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} -5/6 \\ 0 \\ 1/6 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} -1/3 \\ 0 \\ -1/3 \\ 0 \\ 1 \end{pmatrix} \right\}$$
$$\begin{pmatrix} 1 & 0 & -1 & 0 & 1 \\ 0 & 0 & 0 & 1 & -2 \\ 0 & 0 & 0 & 0 & 0 \\ & r & & s & & t \end{pmatrix}$$
2. What is the nullity of $\mathbf{A}$?
$$\text{nullity}(\mathbf{A}) =$$
$$\begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \\ 0 \\ r \end{pmatrix} \begin{pmatrix} 1 \\ -1 \\ 0 \\ 1 \\ 0 \\ s \end{pmatrix} \begin{pmatrix} -1 \\ 2 \\ 0 \\ 0 \\ 1 \\ t \end{pmatrix}$$