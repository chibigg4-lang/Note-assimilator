Example

Set $\mathbf{V} = \begin{pmatrix} 1/3 & -2/3 & 2/3 \\ 2/3 & -1/3 & -2/3 \\ 2/3 & 2/3 & 1/3 \end{pmatrix}$. Finally,

$$\mathbf{u_1} = \frac{1}{6\sqrt{10}} \mathbf{Av_1} = \frac{1}{6\sqrt{10}} \begin{pmatrix} 4 & 11 & 14 \\ 8 & 7 & -2 \end{pmatrix} \begin{pmatrix} 1/3 \\ 2/3 \\ 2/3 \end{pmatrix} = \frac{1}{6\sqrt{10}} \begin{pmatrix} 18 \\ 6 \end{pmatrix} = \begin{pmatrix} 3/\sqrt{10} \\ 1/\sqrt{10} \end{pmatrix},$$
$$\mathbf{u_2} = \frac{1}{3\sqrt{10}} \mathbf{Av_2} = \frac{1}{3\sqrt{10}} \begin{pmatrix} 4 & 11 & 14 \\ 8 & 7 & -2 \end{pmatrix} \begin{pmatrix} -2/3 \\ -1/3 \\ 2/3 \end{pmatrix} = \frac{1}{3\sqrt{10}} \begin{pmatrix} 3 \\ -9 \end{pmatrix} = \begin{pmatrix} 1/\sqrt{10} \\ -3/\sqrt{10} \end{pmatrix}.$$

$\{\mathbf{u_1}, \mathbf{u_2}\}$ is already an orthonormal basis for $\mathbb{R}^2$. Set

$$\mathbf{U} = \begin{pmatrix} 3/\sqrt{10} & 1/\sqrt{10} \\ 1/\sqrt{10} & -3/\sqrt{10} \end{pmatrix}.$$

Then

$$\begin{pmatrix} 4 & 11 & 14 \\ 8 & 7 & -2 \end{pmatrix} = \begin{pmatrix} 3/\sqrt{10} & 1/\sqrt{10} \\ 1/\sqrt{10} & -3/\sqrt{10} \end{pmatrix} \begin{pmatrix} 6\sqrt{10} & 0 & 0 \\ 0 & 3\sqrt{10} & 0 \end{pmatrix} \begin{pmatrix} 1/3 & 2/3 & 2/3 \\ -2/3 & -1/3 & 2/3 \\ 2/3 & -2/3 & 1/3 \end{pmatrix}$$

***

Example

$\mathbf{A} = \begin{pmatrix} 1 & -1 \\ -2 & 2 \\ 2 & -2 \end{pmatrix}$. Observe that $\text{rank}(\mathbf{A}) = 1$

$\sqrt{18} = \sqrt{9 \times 2} = 3\sqrt{2}$

$\mathbf{A^T A} = \begin{pmatrix} 9 & -9 \\ -9 & 9 \end{pmatrix}$. $\det(x\mathbf{I} - \mathbf{A^T A}) = \begin{vmatrix} x - 9 & 9 \\ 9 & x - 9 \end{vmatrix} = x(x - 18) \Rightarrow \mu_1 = 18, \mu_2 = 0 \Rightarrow \mathbf{\Sigma} = \begin{pmatrix} 3\sqrt{2} & 0 \\ 0 & 0 \\ 0 & 0 \end{pmatrix}$.

$\mu_1=18 : 18\mathbf{I} - \mathbf{A^T A} = \begin{pmatrix} 9 & 9 \\ 9 & 9 \end{pmatrix} \xrightarrow{\text{RREF}} \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix} \rightsquigarrow \begin{pmatrix} 1 \\ -1 \end{pmatrix} \rightsquigarrow \begin{pmatrix} 1/\sqrt{2} \\ -1/\sqrt{2} \end{pmatrix}$

$\mu_2=0 : 0\mathbf{I} - \mathbf{A^T A} = \begin{pmatrix} -9 & 9 \\ 9 & -9 \end{pmatrix} \xrightarrow{\text{RREF}} \begin{pmatrix} 1 & -1 \\ 0 & 0 \end{pmatrix} \rightsquigarrow \begin{pmatrix} 1 \\ 1 \end{pmatrix} \rightsquigarrow \begin{pmatrix} 1/\sqrt{2} \\ 1/\sqrt{2} \end{pmatrix}$

$\Rightarrow \mathbf{V} = \begin{pmatrix} 1/\sqrt{2} & 1/\sqrt{2} \\ -1/\sqrt{2} & 1/\sqrt{2} \end{pmatrix}$.