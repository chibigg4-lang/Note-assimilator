# Algorithm for Finding Inverse

$A_{n \times n}$
Step 1: Form $n \times 2n$ (augmented) matrix $(A \mid I_n)$

Step 2: Reduce $(A \mid I) \to (R \mid B)$ to RREF

Step 3: If RREF $R \neq I$ or REF has a $0$ row
$\to A$ is non-invertible
If $R = I$ or REF has no $0$ row
$\to A$ is invertible, $A^{-1} = B$

# LU factorization:

Example

Consider the matrix $\mathbf{A} = \begin{pmatrix} 1 & 2 & 1 & -1 & 0 \\ 1 & 0 & 1 & -1 & 0 \\ 3 & 1 & 0 & 0 & 3 \end{pmatrix}$. Reducing to a row-echelon form,

$\mathbf{A} \xrightarrow{R_2-R_1, R_3-3R_1, R_3-\frac{5}{2}R_2} \begin{pmatrix} 1 & 2 & 1 & -1 & 0 \\ 0 & -2 & 0 & 0 & 0 \\ 0 & 0 & -3 & 3 & 3 \end{pmatrix}$.

This means that

$\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & -5/2 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ -3 & 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 & 0 \\ -1 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \mathbf{A} = \begin{pmatrix} 1 & 2 & 1 & -1 & 0 \\ 0 & -2 & 0 & 0 & 0 \\ 0 & 0 & -3 & 3 & 3 \end{pmatrix}$,

and thus

$\mathbf{A} = \begin{pmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 3 & 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 5/2 & 1 \end{pmatrix} \begin{pmatrix} 1 & 2 & 1 & -1 & 0 \\ 0 & -2 & 0 & 0 & 0 \\ 0 & 0 & -3 & 3 & 3 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 3 & 5/2 & 1 \end{pmatrix} \begin{pmatrix} 1 & 2 & 1 & -1 & 0 \\ 0 & -2 & 0 & 0 & 0 \\ 0 & 0 & -3 & 3 & 3 \end{pmatrix}$.