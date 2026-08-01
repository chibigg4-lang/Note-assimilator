Linear combination :

linear combination $c_1u_1 + c_2u_2 + \dots + c_k u_k$.
$c_1, c_2, \dots, c_k \in \mathbb{R}$
span: $\text{span}\{u_1, u_2, \dots, u_k\} = \{c_1u_1 + c_2u_2 + \dots + c_k u_k\}$

***

### Algorithm to Check for Linear Combination

Let $S = \{u_1, u_2, \dots, u_k\}$ be a set of vectors in $\mathbb{R}^n$.
* Form the $n \times k$ matrix $\mathbf{A} = (u_1 \quad u_2 \quad \dots \quad u_k)$ whose columns are the vectors in $S$.
* Then a vector $\mathbf{v}$ in $\mathbb{R}^n$ is in $\text{span}\{u_1, u_2, \dots, u_k\}$ if and only if the system $\mathbf{Ax} = \mathbf{v}$ is consistent.
* If the system is consistent, then the solutions to the system are the possible coefficients of the linear combination. That is, if $\mathbf{u} = \begin{pmatrix} c_1 \\ c_2 \\ \vdots \\ c_k \end{pmatrix}$ is a solution to $\mathbf{Ax} = \mathbf{v}$, then 
$$\mathbf{v} = c_1u_1 + c_2u_2 + \dots + c_k u_k.$$

***

When will $\text{span}(S) = \mathbb{R}^n$

### Algorithm to check if $\text{span}(S) = \mathbb{R}^n$.

Let $S = \{u_1, u_2, \dots, u_k\}$ be a set of vectors in $\mathbb{R}^n$.
* Form the $n \times k$ matrix $\mathbf{A} = (u_1 \quad u_2 \quad \dots \quad u_k)$ whose columns are the vectors in $S$.
* Then $\text{span}(S) = \mathbb{R}^n$ if and only if the system $\mathbf{Ax} = \mathbf{v}$ is consistent for all $\mathbf{v}$.
* This is equivalent to the reduced row-echelon form of $\mathbf{A}$ having no zero rows.

Explicitly, $\text{span}\{u_1, u_2, \dots, u_k\} = \mathbb{R}^n$ if and only if the reduced row-echelon form of $( u_1 \quad u_2 \quad \dots \quad u_k )$ has no zero rows.