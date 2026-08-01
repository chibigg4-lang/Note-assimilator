# Solution Sets to a linear system

## Solution Sets to a Linear system

Recall that the set of solutions to a linear system $\mathbf{Ax} = \mathbf{b}$ is a subset in $\mathbb{R}^n$ (it is the empty set if the system is inconsistent). We may express this set implicitly as
$$V = \{ \mathbf{u} \in \mathbb{R}^n \mid \mathbf{Au} = \mathbf{b} \},$$
or explicitly as
$$V = \{ \mathbf{u} + s_1\mathbf{v}_1 + s_2\mathbf{v}_2 + \cdots + s_k\mathbf{v}_k \mid s_1, s_2, \dots, s_k \in \mathbb{R} \},$$
where $\mathbf{u} + s_1\mathbf{v}_1 + s_2\mathbf{v}_2 + \cdots + s_k\mathbf{v}_k, s_1, s_2, \dots, s_k \in \mathbb{R}$ is the general solution.

Consider the linear system
$$3x + 2y - z = 1$$
$$y - z = 0$$

Implicitly, it can be written as
$$\left\{ \begin{pmatrix} x \\ y \\ z \end{pmatrix} \middle| 3x + 2y - z = 1, y - z = 0 \right\}.$$

The general solution is
$$x = \frac{1}{3}(1 - s), \quad y = s, \quad z = s, \quad s \in \mathbb{R}$$

So, explicitly, the solution set is
$$\left\{ \begin{pmatrix} 1/3 \\ 0 \\ 0 \end{pmatrix} + s \begin{pmatrix} -1/3 \\ 1 \\ 1 \end{pmatrix} \middle| s \in \mathbb{R} \right\}.$$

Write the implicit expression of the following solution set
$$\left\{ \begin{pmatrix} 1 \\ 2 \\ -1 \end{pmatrix} + s \begin{pmatrix} -2 \\ 1 \\ 0 \end{pmatrix} + t \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix} \middle| s, t \in \mathbb{R} \right\}.$$

① $x = 1 - 2s + t, \quad y = 2 + s, \quad z = t - 1 \Rightarrow x + 2y - z = 6$
③ $x = 1 - 2(y - 2) + z + 1$

So, implicitly, the set has the expression
$$\left\{ \begin{pmatrix} x \\ y \\ z \end{pmatrix} \middle| x + 2y - z = 6 \right\}.$$