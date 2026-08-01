Algorithm to LU Factorization

Suppose $\mathbf{A} \xrightarrow{r_1, r_2, \dots, r_k} \mathbf{U}$, where each row operation $r_i$ is of the form $R_i + cR_j$ for some $i > j$ and real number $c$, and $\mathbf{U}$ is an row-echelon form of $\mathbf{A}$.

$$\mathbf{E}_k \cdots \mathbf{E}_2 \mathbf{E}_1 \mathbf{A} = \mathbf{U} \quad \Rightarrow \quad \mathbf{A} = \mathbf{E}_1^{-1} \mathbf{E}_2^{-1} \cdots \mathbf{E}_k^{-1} \mathbf{U} = \mathbf{LU},$$

where $\mathbf{L} = \mathbf{E}_1^{-1} \mathbf{E}_2^{-1} \cdots \mathbf{E}_k^{-1}$

$$\mathbf{A} = \mathbf{LU} = \begin{pmatrix} 1 & 0 & \cdots & 0 \\ * & 1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ * & * & \cdots & 1 \end{pmatrix} \begin{pmatrix} * & \cdots & * \\ 0 & \cdots & * \\ \vdots & & \vdots \\ 0 & \cdots & * \end{pmatrix}$$

is a LU factorization of $\mathbf{A}$.

In this case, we could obtain $\mathbf{L}$ quickly without computing $\mathbf{E}_1^{-1} \mathbf{E}_2^{-1} \cdots \mathbf{E}_k^{-1}$. For each row operation $r_i = R_i + c_i R_j$ for some $i > j$ and real number $c_i$, we will put $-c_i$ in the $(i,j)$-entry of $\mathbf{L}$.

Example

$$\mathbf{A} = \begin{pmatrix} 2 & 4 & 1 & 5 & -2 \\ -4 & -5 & 3 & -8 & 1 \\ 2 & -5 & -4 & 1 & 8 \\ -6 & 0 & 7 & -3 & 1 \end{pmatrix} \xrightarrow[R_4 - 3R_1]{R_3 - R_1, R_2 + 2R_1} \begin{pmatrix} 2 & 4 & 1 & 5 & -2 \\ 0 & 3 & 5 & 2 & -3 \\ 0 & -9 & -5 & -4 & 10 \\ 0 & 12 & 10 & 12 & -5 \end{pmatrix} \xrightarrow[R_4 - 4R_2]{R_3 + 3R_2} \begin{pmatrix} 2 & 4 & 1 & 5 & -2 \\ 0 & 3 & 5 & 2 & -3 \\ 0 & 0 & 10 & 2 & 1 \\ 0 & 0 & -10 & 4 & 7 \end{pmatrix}$$

$$\xrightarrow{R_4 + R_3} \begin{pmatrix} 2 & 4 & 1 & 5 & -2 \\ 0 & 3 & 5 & 2 & -3 \\ 0 & 0 & 10 & 2 & 1 \\ 0 & 0 & 0 & 6 & 8 \end{pmatrix}$$

$$\mathbf{L} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ -2 & 1 & 0 & 0 \\ 1 & -3 & 1 & 0 \\ -3 & 4 & -1 & 1 \end{pmatrix}$$

$$\mathbf{A} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ -2 & 1 & 0 & 0 \\ 1 & -3 & 1 & 0 \\ -3 & 4 & -1 & 1 \end{pmatrix} \begin{pmatrix} 2 & 4 & 1 & 5 & -2 \\ 0 & 3 & 5 & 2 & -3 \\ 0 & 0 & 10 & 2 & 1 \\ 0 & 0 & 0 & 6 & 8 \end{pmatrix}$$

Example

Solve the system

$$\begin{pmatrix} 2 & 4 & 1 & 5 & -2 \\ -4 & -5 & 3 & -8 & 1 \\ 2 & -5 & -4 & 1 & 8 \\ -6 & 0 & 7 & -3 & 1 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \\ x_5 \end{pmatrix} = \begin{pmatrix} 6 \\ 1 \\ -4 \\ 7 \end{pmatrix}$$

First solve $\mathbf{Ly} = \mathbf{b}$, $\begin{pmatrix} 1 & 0 & 0 & 0 \\ -2 & 1 & 0 & 0 \\ 1 & -3 & 1 & 0 \\ -3 & 4 & -1 & 1 \end{pmatrix} \begin{pmatrix} y_1 \\ y_2 \\ y_3 \\ y_4 \end{pmatrix} = \begin{pmatrix} 6 \\ 1 \\ -4 \\ 7 \end{pmatrix}$ is the unique solution. Now solve for $\mathbf{Ux} = \mathbf{y}$,

$$\begin{pmatrix} 2 & 4 & 1 & 5 & -2 \\ 0 & 3 & 5 & 2 & -3 \\ 0 & 0 & 10 & 2 & 1 \\ 0 & 0 & 0 & 6 & 8 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \\ x_5 \end{pmatrix} = \begin{pmatrix} 6 \\ 13 \\ 29 \\ 2 \end{pmatrix} \text{. The general solution is } \begin{pmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \\ x_5 \end{pmatrix} = \frac{1}{36} \begin{pmatrix} 71 + 37s \\ -22 + 58s \\ 102 + 6s \\ 12 - 48s \end{pmatrix}, s \in \mathbb{R}.$$