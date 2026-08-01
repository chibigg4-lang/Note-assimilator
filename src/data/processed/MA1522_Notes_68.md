Example

Let $\mathbf{A} = \begin{pmatrix} 4 & 11 & 14 \\ 8 & 7 & -2 \end{pmatrix}$.

$$\mathbf{A}^\top\mathbf{A} = \begin{pmatrix} 4 & 8 \\ 11 & 7 \\ 14 & -2 \end{pmatrix} \begin{pmatrix} 4 & 11 & 14 \\ 8 & 7 & -2 \end{pmatrix} = \begin{pmatrix} 80 & 100 & 40 \\ 100 & 170 & 140 \\ 40 & 140 & 200 \end{pmatrix}.$$
$$\det(x\mathbf{I} - \mathbf{A}^\top\mathbf{A}) = \begin{vmatrix} x - 80 & -100 & -40 \\ -100 & x - 170 & -140 \\ -40 & -140 & x - 200 \end{vmatrix} = x(x - 90)(x - 360). \quad \mu = 0, 90, 360.$$

So, the singular values are
$$\sigma_1 = \sqrt{360} = 6\sqrt{10}, \quad \sigma_2 = \sqrt{90} = 3\sqrt{10}, \quad \sigma_3 = 0,$$

and
$$\mathbf{\Sigma} = \begin{pmatrix} 6\sqrt{10} & 0 & 0 \\ 0 & 3\sqrt{10} & 0 \end{pmatrix}$$

***

# Singular Value Decomposition

Suppose $\mathbf{A}$ is a $m \times n$ matrix. Let $\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n\}$ be an orthonormal basis for $\mathbb{R}^n$ consisting of eigenvectors of $\mathbf{A}^\top\mathbf{A}$.
Let
$$\sigma_1 \geq \sigma_2 \geq \dots \geq \sigma_r > 0$$
be the nonzero singular values of $\mathbf{A}$. Define
$$\mathbf{u}_i = \frac{1}{\sigma_i}\mathbf{A}\mathbf{v}_i, \quad i = 1, \dots, r.$$

Lemma
$\{\mathbf{u}_1, \dots, \mathbf{u}_r\}$ is an orthonormal basis for the column space of $\mathbf{A}$, and $\text{rank}(\mathbf{A}) = r$.

***

# Singular Value Decomposition

Using the notations from above, extend $\{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_r\}$ to an orthonormal basis $\{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_m\}$ for $\mathbb{R}^m$ (if $r \neq m$).
Define
$$\mathbf{U} = \begin{pmatrix} \mathbf{u}_1 & \mathbf{u}_2 & \dots & \mathbf{u}_m \end{pmatrix},$$
it is an order $m$ orthogonal matrix. Define
$$\mathbf{V} = \begin{pmatrix} \mathbf{v}_1 & \mathbf{v}_2 & \dots & \mathbf{v}_n \end{pmatrix},$$
then $\mathbf{V}$ is an order $n$ orthogonal matrix. Let $\mathbf{\Sigma}$ be the matrix defined by the nonzero singular values $\sigma_1, \sigma_2, \dots, \sigma_r$.
Then
$$\mathbf{A} = \mathbf{U}\mathbf{\Sigma}\mathbf{V}^\top.$$

Proof.
Since $\mathbf{V}$ is orthogonal, suffice to show that $\mathbf{A}\mathbf{V} = \mathbf{U}\mathbf{\Sigma}$, but by construction,
$$\mathbf{A}\mathbf{V} = \begin{pmatrix} \mathbf{A}\mathbf{v}_1 & \dots & \mathbf{A}\mathbf{v}_r & \mathbf{A}\mathbf{v}_{r+1} & \dots & \mathbf{A}\mathbf{v}_n \end{pmatrix} = \begin{pmatrix} \sigma_1\mathbf{u}_1 & \dots & \sigma_r\mathbf{u}_r & 0 & \dots & 0 \end{pmatrix} = \mathbf{U}\mathbf{\Sigma}.$$