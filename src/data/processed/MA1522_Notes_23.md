In the example above, we may write $\mathbf{A}$ as a product of a lower triangular matrix and a row-echelon of $\mathbf{A}$,
$$\mathbf{A} = \begin{pmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 3 & 5/2 & 1 \end{pmatrix} \begin{pmatrix} 1 & 2 & 1 & -1 & 0 \\ 0 & -2 & 0 & 0 & 0 \\ 0 & 0 & -3 & 3 & 3 \end{pmatrix}.$$
Observe furthermore that the diagonal entries of the lower triangular matrix are 1. Such matrices are known as *unit lower triangular* matrices. We will write it as $\mathbf{A} = \mathbf{LU}$, where $\mathbf{L}$ is a unit lower triangular matrix, and $\mathbf{U}$ is a row-echelon form of $\mathbf{A}$.

Consider now the linear system $\mathbf{Ax} = \begin{pmatrix} 1 \\ 2 \\ 1 \end{pmatrix}$. $\quad \mathbf{LUx=b} \implies \mathbf{Ly=b}$.
$$\begin{pmatrix} 1 & 0 & 0 & | & 1 \\ 1 & 1 & 0 & | & 2 \\ 3 & 5/2 & 1 & | & 1 \end{pmatrix}$$
We can observe that $y_1 = 1, y_2 = 1, y_3 = -9/2$ is the unique solution. $\quad \mathbf{Ux=y}$.
$$\begin{pmatrix} 1 & 2 & 1 & -1 & 0 & | & 1 \\ 0 & -2 & 0 & 0 & 0 & | & 1 \\ 0 & 0 & -3 & 3 & 3 & | & -9/2 \end{pmatrix} \xrightarrow[-\frac{1}{3}R_3]{-\frac{1}{2}R_2} \begin{pmatrix} 1 & 2 & 1 & -1 & 0 & | & 1 \\ 0 & 1 & 0 & 0 & 0 & | & -1/2 \\ 0 & 0 & 1 & -1 & -1 & | & 3/2 \end{pmatrix}$$
tells us that $x_1 = \frac{1}{2} - t$, $x_2 = -\frac{1}{2}$, $x_3 = \frac{3}{2} + s + t$, $x_4 = s$, $x_5 = t$, $s, t \in \mathbb{R}$ is the general solution.

A square matrix $L$ is a *unit lower triangular* matrix if $L$ is a *lower triangular matrix with 1 in diagonal entries.*

An LU factorization of $m \times n$ matrix $A$ is the decomposition
$$A = LU \quad \longleftrightarrow \begin{cases} L: \text{unit lower triangular} \\ U: \text{REF of } A \end{cases}$$

If $A, B$ - unit lower triangular matrixes. $\rightarrow AB$ is also a unit lower triangular matrix.

$$R_i + cR_j \longleftrightarrow E = \begin{pmatrix} 1 & \dots & 0 \\ \vdots & c & \dots & \vdots \\ 0 & \dots & 1 \end{pmatrix} \begin{matrix} j \\ i \end{matrix}$$
$$R_i - cR_j \longleftrightarrow E^{-1} \begin{pmatrix} 1 & \dots & 0 \\ \vdots & -c & \dots & \vdots \\ 0 & \dots & 1 \end{pmatrix} i$$
$E_k \dots E_2 E_1 \rightarrow E_1^{-1} E_2^{-1} \dots E_k^{-1}$ is a unit lower triangular matrix.