### Example
Let $V$ be the solution set to
$$
\begin{cases}
x_1 &+& x_2 & & &+& 2x_4 &+& x_5 &=& 0 \\
2x_1 &-& x_2 &+& 3x_3 & & &+& 3x_5 &=& 0 \\
x_1 &-& 2x_2 &+& 3x_3 &-& 2x_4 &+& 2x_5 &=& 0 \\
2x_1 &-& x_2 &+& 3x_3 & & &+& 3x_5 &=& 0
\end{cases}
$$
Solving the system,
$$
\begin{pmatrix} 1 & 1 & 0 & 2 & 1 & | & 0 \\ 2 & -1 & 3 & 0 & 3 & | & 0 \\ 1 & -2 & 3 & -2 & 2 & | & 0 \\ 2 & -1 & 3 & 0 & 3 & | & 0 \end{pmatrix} \xrightarrow{RREF} \begin{pmatrix} 1 & 0 & 1 & 2/3 & 4/3 & | & 0 \\ 0 & 1 & -1 & 4/3 & -1/3 & | & 0 \\ 0 & 0 & 0 & 0 & 0 & | & 0 \\ 0 & 0 & 0 & 0 & 0 & | & 0 \end{pmatrix} \leftarrow
$$
$$
S = \left\{ \begin{pmatrix} -1 \\ 1 \\ 1 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} -2/3 \\ -4/3 \\ 0 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} -4/3 \\ 1/3 \\ 0 \\ 0 \\ 1 \end{pmatrix} \right\} \text{ spans } V. \text{ Using the last 3 coordinates, we can also conclude that } S \text{ is linearly}
$$
independent (details left to readers). Hence, $S$ is a basis for $V$.
$$
\begin{pmatrix} -1 \\ 1 \\ 1 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} -2/3 \\ -4/3 \\ 0 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} -4/3 \\ 1/3 \\ 0 \\ 0 \\ 1 \end{pmatrix}
$$

### Introduction

### Example
Let $V = \left\{ \begin{pmatrix} x \\ y \\ z \end{pmatrix} \bigg| x + y - z = 0 \right\}$. It was shown that $T = \left\{ \begin{pmatrix} -1 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix} \right\}$ is a basis for $V$. Show that
$S = \left\{ \begin{pmatrix} -1 \\ 2 \\ 1 \end{pmatrix}, \begin{pmatrix} 1 \\ 1 \\ 2 \end{pmatrix} \right\}$ is a basis for $V$.

1. First we show that $\text{span}(S) = V = \text{span}(T)$.
   (i) $\begin{pmatrix} -1 & 1 & | & -1 & 1 \\ 1 & 0 & 2 & 1 \\ 0 & 1 & 1 & 2 \end{pmatrix} \xrightarrow{RREF} \begin{pmatrix} 1 & 0 & 2 & 1 \\ 0 & 1 & 1 & 2 \\ 0 & 0 & 0 & 0 \end{pmatrix}$ shows that $\text{span}(S) \subseteq \text{span}(T)$.
   (ii) $\begin{pmatrix} -1 & 1 & | & -1 & 1 \\ 2 & 1 & 1 & 0 \\ 1 & 2 & 0 & 1 \end{pmatrix} \xrightarrow{RREF} \begin{pmatrix} 1 & 0 & 2/3 & -1/3 \\ 0 & 1 & -1/3 & 2/3 \\ 0 & 0 & 0 & 0 \end{pmatrix}$ shows that $\text{span}(T) \subseteq \text{span}(S)$.
   refore, $\text{span}(S) = \text{span}(T) = V$.
   *since there is no non-pivot column*

2. Next, since $S$ contains 2 vectors that are not a multiple of each other, $S$ is linearly independent.
   Hence, $S$ is a basis for $V$ too. This also shows that basis for a subspace may not be unique.