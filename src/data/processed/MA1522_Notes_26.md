$$
\begin{pmatrix}
1 & 2 & 1 \\
-1 & 1 & 3 \\
3 & 2 & 1
\end{pmatrix}
$$

$$
\begin{aligned}
A_{11} &= \begin{vmatrix} 1 & 3 \\ 2 & 1 \end{vmatrix} & A_{12} &= -\begin{vmatrix} -1 & 3 \\ 3 & 1 \end{vmatrix} & A_{13} &= \begin{vmatrix} -1 & 1 \\ 3 & 2 \end{vmatrix} \\
&= (1)(1) - (2)(3) & &= -(-1)(1) + (3)(3) & &= (-1)(2) - (1)(3) \\
&= -5 & &= 10 & &= -5
\end{aligned}
$$

$$
\begin{aligned}
A_{21} &= -\begin{vmatrix} 2 & -1 \\ 2 & 1 \end{vmatrix} & A_{22} &= \begin{vmatrix} 1 & -1 \\ 3 & 1 \end{vmatrix} & A_{23} &= -\begin{vmatrix} 1 & 2 \\ 3 & 2 \end{vmatrix} \\
&= -(2)(1) + (-1)(2) & &= (1)(1) - (-1)(3) & &= -(1)(2) + (2)(3) \\
&= -4 & &= 4 & &= 4
\end{aligned}
$$

$$
\begin{aligned}
A_{31} &= \begin{vmatrix} 2 & -1 \\ 1 & 3 \end{vmatrix} & A_{32} &= -\begin{vmatrix} 1 & -1 \\ -1 & 3 \end{vmatrix} & A_{33} &= \begin{vmatrix} 1 & 2 \\ -1 & 1 \end{vmatrix} \\
&= (2)(3) - (-1)(1) & &= -(1)(3) + (-1)(-1) & &= (1)(1) - (2)(-1) \\
&= 7 & &= -2 & &= 3
\end{aligned}
$$

The determinant of **A** is defined to be

$$
\det(\mathbf{A}) = a_{i1}A_{i1} + a_{i2}A_{i2} + \dots + a_{in}A_{in} = \sum_{k=1}^n a_{ik}A_{ik} \tag{1}
$$

$$
= a_{1j}A_{1j} + a_{2j}A_{2j} + \dots + a_{nj}A_{nj} = \sum_{k=1}^n a_{kj}A_{kj} \tag{2}
$$

This is called the cofactor expansion along $\begin{cases} \text{row} & i \quad (3) \\ \text{column} & j \quad (4) \end{cases}$.

$$
\begin{vmatrix} a & b & c \\ d & e & f \\ g & h & i \end{vmatrix} = a \begin{vmatrix} e & f \\ h & i \end{vmatrix} - b \begin{vmatrix} d & f \\ g & i \end{vmatrix} + c \begin{vmatrix} d & e \\ g & h \end{vmatrix} = aei - afh - bdi + bfg + cdh - ceg.
$$

$$
\begin{vmatrix} a & b & c \\ d & e & f \\ g & h & i \end{vmatrix} \begin{matrix} a & b \\ d & e \\ g & h \end{matrix}
$$
$$-ceg - afh - bdi + aei + bfg + cdh$$

### Determinant of Triangular Matrices
Theorem (Determinant of a triangular matrix is the product of diagonal entries)
If **A** = $(a_{ij})_n$ is a triangular matrix, then

$$
\det(\mathbf{A}) = a_{11}a_{22} = \dots a_{nn} = \prod_{k=1}^n a_{ii}.
$$

Sketch of proof.
Upper triangular matrix, continuously cofactor expand along first column,
$$
\begin{vmatrix} a_{11} & a_{12} & a_{13} & a_{14} \\ 0 & a_{22} & a_{23} & a_{2n} \\ 0 & 0 & a_{33} & a_{34} \\ 0 & 0 & 0 & a_{44} \end{vmatrix} = a_{11} \begin{vmatrix} a_{22} & a_{23} & a_{2n} \\ 0 & a_{33} & a_{34} \\ 0 & 0 & a_{44} \end{vmatrix} = a_{11}a_{22} \begin{vmatrix} a_{33} & a_{34} \\ 0 & a_{44} \end{vmatrix} = a_{11}a_{22}a_{33}a_{44}.
$$