Algorithm to Singular Value Decomposition

Let $\mathbf{A}$ be a $m \times n$ matrix with $\text{rank}(\mathbf{A}) = r$.
1. Find the eigenvalues of $\mathbf{A}^T\mathbf{A}$. Arrange the nonzero eigenvalues in descending order (counting multiplicity)
$$\mu_1 \ge \mu_2 \ge \dots \ge \mu_r > 0 = \mu_{r+1} = \dots = \mu_n,$$
and let $\sigma_i = \sqrt{\mu_i}, i = 1, \dots, r$. Set
$$\boldsymbol{\Sigma} = \begin{pmatrix} \mathbf{D} & \mathbf{0}_{r \times (n-r)} \\ \mathbf{0}_{(m-r) \times r} & \mathbf{0}_{(m-r) \times (n-r)} \end{pmatrix} \text{, where } \mathbf{D} = \begin{pmatrix} \sigma_1 & 0 & \dots & 0 \\ 0 & \sigma_2 & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & \sigma_r \end{pmatrix}.$$
2. Find an orthogonal basis for each eigenspace, and let $\mathbf{v}_i$ be the unit vector associated to $\mu_i$. Set
$$\mathbf{V} = \begin{pmatrix} \mathbf{v}_1 & \mathbf{v}_2 & \dots & \mathbf{v}_n \end{pmatrix}.$$
3. Let $\mathbf{u}_i = \frac{1}{\sigma_i} \mathbf{A}\mathbf{v}_i$ for $i = 1, \dots, r$. Extend $\{\mathbf{u}_1, \dots, \mathbf{u}_r\}$ to an orthonormal basis $\{\mathbf{u}_1, \dots, \mathbf{u}_r, \mathbf{u}_{r+1}, \dots, \mathbf{u}_m\}$ of $\mathbb{R}^m$, that is, solve for $(\mathbf{u}_1 \dots \mathbf{u}_r)^T \mathbf{x} = \mathbf{0}$ and find an orthonormal basis for the solution space. Let
$$\mathbf{U} = \begin{pmatrix} \mathbf{u}_1 & \mathbf{u}_2 & \dots & \mathbf{u}_m \end{pmatrix}$$

***

Example

Let $\mathbf{A} = \begin{pmatrix} 4 & 11 & 14 \\ 8 & 7 & -2 \end{pmatrix}$.

Eigenvalues are $\mu_1 = 360, \mu_2 = 90, \mu_3 = 0$. Here $\text{rank}(A) = 2$, so,
$$\boldsymbol{\Sigma} = \begin{pmatrix} 6\sqrt{10} & 0 & 0 \\ 0 & 3\sqrt{10} & 0 \end{pmatrix}.$$

$$\mu_1 = 360 : 360\mathbf{I} - \mathbf{A}^T\mathbf{A} = \begin{pmatrix} 280 & -100 & -40 \\ -100 & 190 & -140 \\ -40 & -140 & 160 \end{pmatrix} \xrightarrow{\text{rref}} \begin{pmatrix} 1 & 0 & -1/2 \\ 0 & 1 & -1 \\ 0 & 0 & 0 \end{pmatrix} \Rightarrow \begin{pmatrix} 1/2 \\ 1 \\ 1 \end{pmatrix} \leadsto \mathbf{v}_1 = \begin{pmatrix} 1/3 \\ 2/3 \\ 2/3 \end{pmatrix}$$

$$\mu_2 = 90 : 90\mathbf{I} - \mathbf{A}^T\mathbf{A} = \begin{pmatrix} 10 & -100 & -40 \\ -100 & -80 & -140 \\ -40 & -140 & -110 \end{pmatrix} \xrightarrow{\text{rref}} \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1/2 \\ 0 & 0 & 0 \end{pmatrix} \Rightarrow \mathbf{v}_2 = \begin{pmatrix} -2/3 \\ -1/3 \\ 2/3 \end{pmatrix}$$

$$\mu_2 = 0 : -\mathbf{A}^T\mathbf{A} = \begin{pmatrix} -80 & -100 & -40 \\ -100 & -170 & -140 \\ -40 & -140 & -200 \end{pmatrix} \xrightarrow{\text{rref}} \begin{pmatrix} 1 & 0 & -2 \\ 0 & 1 & 2 \\ 0 & 0 & 0 \end{pmatrix} \Rightarrow \mathbf{v}_3 = \begin{pmatrix} 2/3 \\ -2/3 \\ 1/3 \end{pmatrix}$$