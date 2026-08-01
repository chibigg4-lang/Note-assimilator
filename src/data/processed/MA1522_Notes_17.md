# Elementary matrices:

A square matrix $E$ of order $n$ is called an elementary matrix if it can be obtained from the identity matrix $I_n$ by performing a single elementary row operation.
$$I_n \xrightarrow{r} E$$

# Elementary matrices and Elementary Row operations
$A_{nxm}$
$E_{nxn}$
$$A \xrightarrow{r} EA$$

# Row Equivalent matrices
$$A \xrightarrow{r_1} E_1A \xrightarrow{r_2} E_2E_1A \xrightarrow{r_3} \dots \xrightarrow{r_k} B = E_k \dots E_2E_1A$$
$$A = E_1^{-1}E_2^{-1} \dots E_k^{-1}B$$

$$
\begin{pmatrix} 1 & 1 & 1 & 0 \\ 1 & 2 & 3 & -1 \\ 2 & 1 & 4 & 2 \end{pmatrix} \xrightarrow{R_2+2R_1} \xrightarrow{R_2 \leftrightarrow R_3} \begin{pmatrix} 1 & 1 & 1 & 0 \\ 2 & 1 & 4 & 2 \\ 3 & 4 & 5 & -1 \end{pmatrix}
$$
$$
\begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix} \begin{pmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 & 1 & 0 \\ 1 & 2 & 3 & -1 \\ 2 & 1 & 4 & 2 \end{pmatrix} = B
$$

# Inverse of elementary matrices

Consider the following
$$I_3 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \xrightarrow{R_2+3R_1} = \mathbf{B} = E$$
Give a single row operation that reduces $\mathbf{B}$ to the identity matrix $I_3$,
$$\mathbf{E} = \mathbf{B} = \begin{pmatrix} 1 & 0 & 0 \\ 3 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \xrightarrow{R_2-3R_1} \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} = I$$
$$I = E'E$$
$$I = EE'$$
$$I \xrightarrow{R_2-3R_1} E' \xrightarrow{R_2+3R_1} I$$