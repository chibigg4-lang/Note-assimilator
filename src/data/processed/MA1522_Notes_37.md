Let $\mathbf{A} = \begin{pmatrix} -1 & 1 & 2 & 1 \\ 3 & 3 & 6 & 9 \\ 3 & -1 & -2 & 1 \end{pmatrix}$.

$$ \begin{pmatrix} -1 & 1 & 2 & 1 & 0 \\ 3 & 3 & 6 & 9 & 0 \\ 3 & -1 & -2 & 1 & 0 \end{pmatrix} \xrightarrow{RREF} \begin{pmatrix} 1 & 0 & 0 & 1 & 0 \\ 0 & 1 & 2 & 2 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{pmatrix} $$

tells us that the solution set to the homogeneous system is

$$ V = \left\{ s \begin{pmatrix} 0 \\ -2 \\ 1 \\ 0 \end{pmatrix} + t \begin{pmatrix} -1 \\ -2 \\ 0 \\ 1 \end{pmatrix} \;\middle|\; s, t \in \mathbb{R} \right\} = \text{span} \left\{ \begin{pmatrix} 0 \\ -2 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} -1 \\ -2 \\ 0 \\ 1 \end{pmatrix} \right\}. $$

The solution set $V$ is a subspace.

Let $\mathbf{b} = \begin{pmatrix} 1 \\ 3 \\ -5 \end{pmatrix}$.

$$ \begin{pmatrix} -1 & 1 & 2 & 1 & 3 \\ 3 & 3 & 6 & 9 & 3 \\ 3 & -1 & -2 & 1 & -5 \end{pmatrix} \xrightarrow{RREF} \begin{pmatrix} 1 & 0 & 0 & 1 & -1 \\ 0 & 1 & 2 & 2 & 2 \\ 0 & 0 & 0 & 0 & 0 \end{pmatrix} $$

tells us that the solution set to the non-homogeneous system is

$$ W = \left\{ \begin{pmatrix} -1 \\ 2 \\ 0 \\ 0 \end{pmatrix} + s \begin{pmatrix} 0 \\ -2 \\ 1 \\ 0 \end{pmatrix} + t \begin{pmatrix} -1 \\ -2 \\ 0 \\ 1 \end{pmatrix} \;\middle|\; s, t \in \mathbb{R} \right\} = \begin{pmatrix} -1 \\ 2 \\ 0 \\ 0 \end{pmatrix} + \text{span} \left\{ \begin{pmatrix} 0 \\ -2 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} -1 \\ -2 \\ 0 \\ 1 \end{pmatrix} \right\}. $$

The solution set $V$ is not a subspace as it does not contain the origin. It is shifted away from the origin via the vector $\mathbf{u} = \begin{pmatrix} -1 \\ 2 \\ 0 \\ 0 \end{pmatrix}$. Observe that $W$ and $V$ are parallel planes.

# Linear Independence

**Definition**
A set $\{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_k\}$ is **linearly independent** if the only coefficients $c_1, c_2, \dots, c_k$ satisfying the equation
$$ c_1\mathbf{u}_1 + c_2\mathbf{u}_2 + \dots + c_k\mathbf{u}_k = \mathbf{0}, $$
are $c_1 = c_2 = \dots = c_k = 0$. Otherwise, we say that the set is **linearly dependent**.

**Algorithm to Check for Linear Independence**
Let $\{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_k\}$ be a set of vectors in $\mathbb{R}^n$.
* $\{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_k\}$ is linearly independent if and only if the homogeneous system $(\mathbf{u}_1 \quad \mathbf{u}_2 \quad \dots \quad \mathbf{u}_k)\mathbf{x} = \mathbf{0}$ has only the trivial solution.
* The homogeneous system has only the trivial solution if and only if the reduce row-echelon form of $(\mathbf{u}_1 \quad \mathbf{u}_2 \quad \dots \quad \mathbf{u}_k)$ has no non-pivot column.

**Theorem** (Solution set of a homogeneous system is a subspace)
A subset $S = \{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_k\}$ of $\mathbb{R}^n$ is linearly independent if and only if the reduced row-echelon form of $\mathbf{A} = (\mathbf{u}_1 \quad \mathbf{u}_2 \quad \dots \quad \mathbf{u}_k)$ has no non-pivot columns.