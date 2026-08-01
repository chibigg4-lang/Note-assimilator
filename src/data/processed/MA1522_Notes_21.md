### Example
Now consider $\mathbf{A} = \begin{pmatrix} 1 & 1 & -1 \\ 1 & 0 & 0 \\ -1 & -1 & 1 \end{pmatrix}$. Reducing, we have
$$\begin{pmatrix} 1 & 1 & -1 \\ 1 & 0 & 0 \\ -1 & -1 & 1 \end{pmatrix} \xrightarrow{R_3+R_1, R_2 \leftrightarrow R_1, R_2-R_1} \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & -1 \\ 0 & 0 & 0 \end{pmatrix}.$$
The reduced row-echelon form of $\mathbf{A}$ has both a non-pivot column and a zero row. Now consider the linear system $\mathbf{Ax} = \mathbf{b}$, where $\mathbf{b} = \begin{pmatrix} b_1 \\ b_2 \\ b_3 \end{pmatrix}$, for some $b_1, b_2, b_3 \in \mathbb{R}$. Let's solve the equation by row reduction.
$$\begin{pmatrix} 1 & 1 & -1 & | & b_1 \\ 1 & 0 & 0 & | & b_2 \\ -1 & -1 & 1 & | & b_3 \end{pmatrix} \xrightarrow{R_3+R_1, R_2 \leftrightarrow R_1, R_2-R_1} \begin{pmatrix} 1 & 0 & 0 & | & b_2 \\ 0 & 1 & -1 & | & b_1-b_2 \\ 0 & 0 & 0 & | & b_1+b_3 \end{pmatrix}.$$

---

### Elementary Matrices and Inverse
**Theorem**
If $\mathbf{A} = \mathbf{E}_k \cdots \mathbf{E}_2\mathbf{E}_1$ is a product of elementary matrices, then $\mathbf{A}$ is invertible.

**Proof.**
$E_1, E_2, \dots, E_k$ invertible, $(E_k \cdots E_2 E_1)$ invertible. $\square$

**Corollary**
If the reduce row-echelon form of $\mathbf{A}$ is the identity matrix, then $\mathbf{A}$ is invertible.

**Proof.**
$A \text{ row equivalent to } I \implies I = E_k \cdots E_2 E_1 A$.
$$\cancel{E_1^{-1}} \cancel{E_2^{-1}} \cdots \cancel{E_k^{-1}} E_k \cdots E_2 E_1 A = E_1^{-1} E_2^{-1} \cdots E_k^{-1} I = E_1^{-1} E_2^{-1} \cdots E_k^{-1}.$$