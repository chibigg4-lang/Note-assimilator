Determinant and elementary row operations:

$A \xrightarrow{R_i + aR_j} B \to \det(B) = \det(A)$
$A \xrightarrow{cR_i} B \to \det(B) = c \det(A)$
$A \xrightarrow{R_i \leftrightarrow R_j} B \to \det(B) = -\det(A)$

Note: single elementary row operation.
if a square matrix A has 2 equal columns or rows $\to \det(A) = 0$

$R_{n \times n} = E_k \dots E_2 E_1 A$.
$\det(R) = \det(E_k) \dots \det(E_2) \det(E_1) \det(A)$

**Corollary**
The determinant of an elementary matrix **E** is given as such.
(i) If **E** corresponds to $R_i + aR_j$, then $\det(\mathbf{E}) = 1$.
(ii) If **E** corresponds to $cR_j$, then $\det(\mathbf{E}) = c$.
(iii) If **E** corresponds to $R_i \leftrightarrow R_j$, then $\det(\mathbf{E}) = -1$.

**Determinant of Row Equivalent Matrices**
Corollary
Let **A** be an $n \times n$ square matrix. Suppose $A \xrightarrow{r_1} \xrightarrow{r_2} \dots \xrightarrow{r_k} R = \begin{pmatrix} d_1 & * & \dots & * \\ 0 & d_2 & \dots & * \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & d_n \end{pmatrix}$, where **R** is the reduced row-echelon form of **A**. Let $E_i$ be the elementary matrix corresponding to the elementary row operation $r_i$, for $i = 1, \dots, k$. Then
$$\det(A) = \frac{d_1 d_2 \dots d_n}{\det(E_k) \dots \det(E_2) \det(E_1)}$$

$$A = \begin{pmatrix} 2 & 1 & 3 & 1 \\ 1 & 0 & 1 & 1 \\ 0 & 2 & 1 & 0 \\ 0 & 1 & 2 & 3 \end{pmatrix} \xrightarrow{E_1: R_1-2R_2} \xrightarrow{E_2: R_3-2R_4} \begin{pmatrix} 0 & 1 & 1 & -1 \\ 1 & 0 & 1 & 1 \\ 0 & 0 & -3 & -6 \\ 0 & 1 & 2 & 3 \end{pmatrix} \xrightarrow{E_3: R_4-R_1} \xrightarrow{E_4: -\frac{1}{3}R_3} \begin{pmatrix} 0 & 1 & 1 & -1 \\ 1 & 0 & 1 & 1 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 1 & 4 \end{pmatrix} \xrightarrow{E_5: R_4-R_3} \begin{pmatrix} 0 & 1 & 1 & -1 \\ 1 & 0 & 1 & 1 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & 2 \end{pmatrix} \xrightarrow{E_6: R_1 \leftrightarrow R_2} \begin{pmatrix} 1 & 0 & 1 & 1 \\ 0 & 1 & 1 & -1 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & 2 \end{pmatrix}$$

$$2 = (-1)(1)(-3)(1)(1)(1) \det(A)$$
$$\det(A) = 2(-1)(-3) = 6.$$