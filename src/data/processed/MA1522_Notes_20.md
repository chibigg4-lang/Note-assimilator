Example

Next, let us evaluate the product of the elementary matrices in the reduction of $\mathbf{A}$,
$$\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & -1 \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1/2 \end{pmatrix} \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 & -1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \mathbf{A} = \begin{pmatrix} 1 & 0 & -1 \\ 1/2 & 1/2 & -1 \\ 1/2 & 1/2 & 0 \end{pmatrix} \mathbf{A}.$$
Observe that if we multiply the matrix to the right of $\mathbf{A}$, we do get the identity matrix too,
$$\begin{pmatrix} 1 & -1 & 1 \\ -1 & 1 & 1 \\ 0 & -1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 & -1 \\ 1/2 & 1/2 & -1 \\ 1/2 & 1/2 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}.$$
This shows that $\mathbf{A}^{-1} = \begin{pmatrix} 1 & 0 & -1 \\ 1/2 & 1/2 & -1 \\ 1/2 & 1/2 & 0 \end{pmatrix}.$

***

Example

Now consider the linear system $\mathbf{Ax} = \mathbf{b}$, where $\mathbf{b} = \begin{pmatrix} b_1 \\ b_2 \\ b_3 \end{pmatrix}$, for some $b_1, b_2, b_3 \in \mathbb{R}$. Let's solve the equation by row reduction
$$\begin{pmatrix} 1 & -1 & 1 & | & b_1 \\ -1 & 1 & 1 & | & b_2 \\ 0 & -1 & 1 & | & b_3 \end{pmatrix} \xrightarrow{R_1-R_3, R_2+R_1, R_3+R_2, \frac{1}{2}R_3, R_2-R_3} \begin{pmatrix} 1 & 0 & 0 & | & b_1 - b_3 \\ 0 & 1 & 0 & | & b_1/2 + b_2/2 - b_3 \\ 0 & 0 & 1 & | & b_1/2 + b_2/2 \end{pmatrix}.$$
This shows that the system is not only consistent, but have a unique solution for every $\mathbf{b}$. In fact,
$$\mathbf{A}^{-1}\mathbf{b} = \begin{pmatrix} 1 & 0 & -1 \\ 1/2 & 1/2 & -1 \\ 1/2 & 1/2 & 0 \end{pmatrix} \begin{pmatrix} b_1 \\ b_2 \\ b_3 \end{pmatrix} = \begin{pmatrix} b_1 - b_3 \\ b_1/2 + b_2/2 - b_3 \\ b_1/2 + b_2/2 \end{pmatrix}.$$

***

$$\frac{4}{5} v = \left( \frac{4}{5}, 0, \frac{4}{5} \right)$$
$$u = (1, 2, 2)$$