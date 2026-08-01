Algorithm to computing inverse:

Suppose $A_{n \times n}$. $AX = I \to$ must have unique solution.

$$(A|I) \xrightarrow{\text{RREF}} (I | A^{-1})$$

Inverse $\begin{pmatrix} 2 & 7 & 1 \\ 1 & 4 & -1 \\ 1 & 3 & 0 \end{pmatrix}$

$$\left( \begin{array}{ccc|ccc} 2 & 7 & 1 & 1 & 0 & 0 \\ 1 & 4 & -1 & 0 & 1 & 0 \\ 1 & 3 & 0 & 0 & 0 & 1 \end{array} \right) \xrightarrow{\text{RREF}} \left( \begin{array}{ccc|ccc} 1 & 0 & 0 & -3/2 & -3/2 & 11/2 \\ 0 & 1 & 0 & 1/2 & 1/2 & -3/2 \\ 0 & 0 & 1 & 1/2 & -1/2 & -1/2 \end{array} \right)$$

$$= \frac{1}{2} \begin{pmatrix} -3 & -3 & 11 \\ 1 & 1 & -3 \\ 1 & -1 & -1 \end{pmatrix}$$

Properties of inverse:

(i) $(A^{-1})^{-1} = A$

(ii) For any non-zero real number $a \in \mathbb{R}$
$(aA)$ is invertible with inverse $(aA)^{-1} = \frac{1}{a} A^{-1}$

(iii) $A^T$ is invertible with inverse $(A^T)^{-1} = (A^{-1})^T$

(iv) if $B$ is an invertible matrix of order $n$
Then $(AB)$ is invertible with inverse $(AB)^{-1} = B^{-1} \cdot A^{-1}$