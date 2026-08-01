Subspaces of $\mathbb{R}^2$

I. Zero space: $\left\{ \begin{pmatrix} 0 \\ 0 \end{pmatrix} \right\}$.
This is a point.
II. Lines: $L = \text{span} \left\{ \begin{pmatrix} x_1 \\ y_1 \end{pmatrix} \right\}$ for some fixed $\begin{pmatrix} x_1 \\ y_1 \end{pmatrix} \neq \begin{pmatrix} 0 \\ 0 \end{pmatrix}$.
These are lines, which looks like $\mathbb{R}^1$.
III. Whole $\mathbb{R}^2$.

Subspaces of $\mathbb{R}^3$

I. Zero space: $\left\{ \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} \right\}$.
This is a point.
II. Lines: $L = \text{span} \left\{ \begin{pmatrix} x_1 \\ y_1 \\ z_1 \end{pmatrix} \right\}$ for some fixed $\begin{pmatrix} x_1 \\ y_1 \\ z_1 \end{pmatrix} \neq \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}$.
These are lines, which looks like $\mathbb{R}^1$.
III. Planes, $P = \text{span} \left\{ \begin{pmatrix} x_1 \\ y_1 \\ z_1 \end{pmatrix}, \begin{pmatrix} x_2 \\ y_2 \\ z_2 \end{pmatrix} \right\}$ for some $\begin{pmatrix} x_1 \\ y_1 \\ z_1 \end{pmatrix}, \begin{pmatrix} x_2 \\ y_2 \\ z_2 \end{pmatrix}$ that are not a scalar multiple of each other.
These are planes, which looks like $\mathbb{R}^2$.
IV. Whole $\mathbb{R}^3$.

---

Affine spaces

Recall that
$$\mathbf{u} + s_1\mathbf{v}_1 + s_2\mathbf{v}_2 + \dots + s_k\mathbf{v}_k, s_1, s_2, \dots, s_k \in \mathbb{R}$$
is a general solution to a consistent non-homogeneous system $\mathbf{Ax} = \mathbf{b}, \mathbf{b} \neq \mathbf{0}$ if and only if
$$s_1\mathbf{v}_1 + s_2\mathbf{v}_2 + \dots + s_k\mathbf{v}_k, s_1, s_2, \dots, s_k \in \mathbb{R}$$
is a general solution to the homogeneous system $\mathbf{Ax} = \mathbf{0}$, where $\mathbf{u}$ is a particular solution to the non-homogeneous system $\mathbf{Ax} = \mathbf{b}$.

Theorem (Affine spaces)
The solution set $W = \{ \mathbf{w} \mid \mathbf{Aw} = \mathbf{b} \}$ of a non-homogeneous linear system $\mathbf{Ax} = \mathbf{b}, \mathbf{b} \neq \mathbf{0}$ is given by
$$\mathbf{u} + V := \{ \mathbf{u} + \mathbf{v} \mid \mathbf{v} \in V \},$$
where $V = \{ \mathbf{v} \mid \mathbf{Av} = \mathbf{0} \}$ is the solution space to the associated homogeneous system and $\mathbf{u}$ is a particular solution, $\mathbf{Au} = \mathbf{b}$.
That is, vectors in $\mathbf{u} + V$ are of the form $\mathbf{u} + \mathbf{v}$ for some $\mathbf{v}$ in $V$.