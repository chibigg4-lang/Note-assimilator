Challenge

Definition
A steady-state vector, or equilibrium vector for a stochastic matrix $\mathbf{P}$ is a probability vector that is an eigenvector associated to eigenvalue $1$.

Theorem
Let $\mathbf{P}$ be a $n \times n$ stochastic matrix and
$$\mathbf{x}_0, \mathbf{x}_1 = \mathbf{P}\mathbf{x}_0, \dots, \mathbf{x}_k = \mathbf{P}\mathbf{x}_{k-1}$$
be a Markov chain for some probability vector $\mathbf{x}_0$. If the Markov chain converges, it will converge to an equilibrium vector.

Proof.
Exercise. Hint:
(i) Show that $1$ is always an eigenvalue of a stochastic matrix.
(ii) Show that if $\mathbf{v}$ is a probability vector and $\mathbf{P}$ a stochastic matrix, then $\mathbf{P}\mathbf{v}$ is also a probability vector.
(iii) Show that if the Markov chain do converge, then the state vectors will converge to an equilibrium vector.

# Singular Value Decomposition.

Theorem (Singular value decomposition)

Let $\mathbf{A}$ be a $m \times n$ matrix. Then
$$\mathbf{A} = \mathbf{U}\mathbf{\Sigma}\mathbf{V}^T,$$

where $\mathbf{U}$ is an order $m$ orthogonal matrix, $\mathbf{V}$ an order $n$ orthogonal matrix, and the matrix $\mathbf{\Sigma}$ has the form
$$\mathbf{\Sigma} = \begin{pmatrix} \mathbf{D} & \mathbf{0}_{r \times (n-r)} \\ \mathbf{0}_{(m-r) \times r} & \mathbf{0}_{(m-r) \times (n-r)} \end{pmatrix},$$

for some diagonal matrix $\mathbf{D}$ of order $r$, where $r \leq \min\{m, n\}$.

1. $\begin{pmatrix} 4 & 11 & 14 \\ 8 & 7 & -2 \end{pmatrix} = \underbrace{\begin{pmatrix} 3/\sqrt{10} & 1/\sqrt{10} \\ 1/\sqrt{10} & -3/\sqrt{10} \end{pmatrix}}_{U_{2 \times 2}} \underbrace{\begin{pmatrix} 6\sqrt{10} & 0 & 0 \\ 0 & 3\sqrt{10} & 0 \end{pmatrix}}_{\Sigma_{2 \times 3}} \begin{pmatrix} 1/3 & 2/3 & 2/3 \\ -2/3 & -1/3 & 2/3 \\ 2/3 & -2/3 & 1/3 \end{pmatrix}_{V^T_{3 \times 3}}.$

2. $\begin{pmatrix} 1 & -1 \\ -2 & 2 \\ 2 & -2 \end{pmatrix} = \underbrace{\begin{pmatrix} 1/3 & 2/\sqrt{5} & -2/\sqrt{45} \\ -2/3 & 1/\sqrt{5} & 4/\sqrt{45} \\ 2/3 & 0 & 5/\sqrt{45} \end{pmatrix}}_{U} \begin{pmatrix} 3\sqrt{2} & 0 \\ 0 & 0 \\ 0 & 0 \end{pmatrix} \begin{pmatrix} 1/\sqrt{2} & -1/\sqrt{2} \\ 1/\sqrt{2} & 1/\sqrt{2} \end{pmatrix}.$