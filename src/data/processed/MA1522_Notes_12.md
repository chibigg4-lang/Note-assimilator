# Block multiplication:

$$
A = 
\begin{pmatrix}
a_{11} & a_{12} & \dots & a_{1n} \\
a_{21} & a_{22} & \dots & a_{2n} \\
\vdots & \vdots & & \vdots \\
a_{m1} & a_{m2} & \dots & a_{mn}
\end{pmatrix}
\begin{matrix}
\rightarrow r_1 \\
\rightarrow r_2 \\
\\
\end{matrix}
$$
$$\quad \quad \quad \quad \quad c_1 \quad \quad c_2 \quad \quad \quad \quad c_n$$

$$
\begin{matrix}
A & & B & & AB \\
\left( \square \right)_{m \times p} & \left( \vert \right)_{p \times n} & = & \left( \square \right)
\end{matrix}
$$

Let $A = \begin{pmatrix} 3 & 2 & -1 \\ 5 & -1 & 3 \\ 2 & 1 & -1 \end{pmatrix}$. Find a $3 \times 3$ matrix $X$ such that

$$
\underbrace{\begin{pmatrix} 3 & 2 & -1 \\ 5 & -1 & 3 \\ 2 & 1 & -1 \end{pmatrix}}_{A} \underbrace{\begin{pmatrix} x_1 & x_2 & x_3 \\ y_1 & y_2 & y_3 \\ z_1 & z_2 & z_3 \end{pmatrix}}_{X} = \underbrace{\begin{pmatrix} 1 & 2 & 1 \\ 2 & 1 & 1 \\ 3 & 1 & 0 \end{pmatrix}}_{B}
$$

By block multiplication, we are solving for the 3 linear systems

$$
A \begin{pmatrix} x_1 \\ y_1 \\ z_1 \end{pmatrix} = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}, \quad A \begin{pmatrix} x_2 \\ y_2 \\ z_2 \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \\ 1 \end{pmatrix}, \quad A \begin{pmatrix} x_3 \\ y_3 \\ z_3 \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}
$$