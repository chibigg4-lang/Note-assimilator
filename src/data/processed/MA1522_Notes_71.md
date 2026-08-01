Example

$$ \mathbf{u_1} = \frac{1}{3\sqrt{2}} \mathbf{Av_1} = \frac{1}{3\sqrt{2}} \begin{pmatrix} 1 & -1 \\ -2 & 2 \\ 2 & -2 \end{pmatrix} \begin{pmatrix} -1/\sqrt{2} \\ 1/\sqrt{2} \end{pmatrix} = \begin{pmatrix} -1/3 \\ 2/3 \\ -2/3 \end{pmatrix}. $$
Extend $\{\mathbf{u_1}\}$ to an orthonormal basis for $\mathbb{R}^3$.
$$ \begin{pmatrix} x \\ y \\ z \end{pmatrix} \cdot \begin{pmatrix} -1/3 \\ 2/3 \\ -2/3 \end{pmatrix} = 0 \Rightarrow -\frac{1}{3}x + \frac{2}{3}y - \frac{2}{3}z = 0 $$
General solution: $s \begin{pmatrix} 2 \\ 1 \\ 0 \end{pmatrix} + t \begin{pmatrix} -2 \\ 0 \\ 1 \end{pmatrix}, s, t \in \mathbb{R}$.

Performing Gram-Schmidt process, we get
$$ \mathbf{u_2} = \begin{pmatrix} 2/\sqrt{5} \\ 1/\sqrt{5} \\ 0 \end{pmatrix}, \quad \mathbf{u_3} = \begin{pmatrix} -2/(3\sqrt{5}) \\ 4/(3\sqrt{5}) \\ 5/(3\sqrt{5}) \end{pmatrix} \Rightarrow \mathbf{U} = \begin{pmatrix} -1/3 & 2/\sqrt{5} & -2/(3\sqrt{5}) \\ 2/3 & 1/\sqrt{5} & 4/(3\sqrt{5}) \\ -2/3 & 0 & 5/(3\sqrt{5}) \end{pmatrix} $$

So,
$$ \begin{pmatrix} 1 & -1 \\ -2 & 2 \\ 2 & -2 \end{pmatrix} = \begin{pmatrix} -1/3 & 2/\sqrt{5} & -2/(3\sqrt{5}) \\ 2/3 & 1/\sqrt{5} & 4/(3\sqrt{5}) \\ -2/3 & 0 & 5/(3\sqrt{5}) \end{pmatrix} \begin{pmatrix} 3\sqrt{2} & 0 \\ 0 & 0 \\ 0 & 0 \end{pmatrix} \begin{pmatrix} -1/\sqrt{2} & 1/\sqrt{2} \\ 1/\sqrt{2} & 1/\sqrt{2} \end{pmatrix} $$