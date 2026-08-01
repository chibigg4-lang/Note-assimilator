Definition
Let $\mathbf{A}$ be an $n \times n$ square matrix. The adjoint of $\mathbf{A}$, denoted as $\mathbf{adj}(\mathbf{A})$, is the $n \times n$ square matrix whose $(i, j)$ entry is the $(j, i)$-cofactor of $\mathbf{A}$,

$$\mathbf{adj}(\mathbf{A}) = \begin{pmatrix} A_{11} & A_{12} & \cdots & A_{1n} \\ A_{21} & A_{22} & \cdots & A_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ A_{n1} & A_{n2} & \cdots & A_{nn} \end{pmatrix}^T = \begin{pmatrix} A_{11} & A_{21} & \cdots & A_{n1} \\ A_{12} & A_{22} & \cdots & A_{n2} \\ \vdots & \vdots & \ddots & \vdots \\ A_{1n} & A_{2n} & \cdots & A_{nn} \end{pmatrix}.$$

Theorem (Adjoint formula)
Let $\mathbf{A}$ be a square matrix and $\mathbf{adj}(\mathbf{A})$ it adjoint. Then

$$\mathbf{A}(\mathbf{adj}(\mathbf{A})) = \det(\mathbf{A})\mathbf{I},$$

where $\mathbf{I}$ is the identity matrix.
Corollary (Adjoint formula for inverse)
Let $\mathbf{A}$ be an invertible matrix. Then the inverse of $\mathbf{A}$ is given by

$$\mathbf{A}^{-1} = \frac{1}{\det(\mathbf{A})}\mathbf{adj}(\mathbf{A}).$$

# Euclidean Vector spaces:

$$v = \begin{pmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{pmatrix} \bigg| v_i \in \mathbb{R} \text{ for } i = 1, 2, \dots, n$$

### Vectors addition and Scalar Multiplication
Since vectors are matrices (column vectors are $n \times 1$ matrices and row vectors are $1 \times n$ matrices), the properties of matrix addition and scalar multiplication holds for vectors.
However, there are geometrical interpretations for these properties. For any vectors $\mathbf{u}, \mathbf{v}, \mathbf{w}$ and scalars $a, b \in \mathbb{R}$,
(i) The sum $\mathbf{u} + \mathbf{v}$ is a vector in $\mathbb{R}^n$.
(ii) (Commutative) $\mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u}$.
(iii) (Associative) $\mathbf{u} + (\mathbf{v} + \mathbf{w}) = (\mathbf{u} + \mathbf{v}) + \mathbf{w}$.
(iv) (Zero vector) $\mathbf{0} + \mathbf{v} = \mathbf{v}$.
(v) The negative $-\mathbf{v}$ is a vector in $\mathbb{R}^n$ such that $\mathbf{v} - \mathbf{v} = \mathbf{0}$.
(vi) (Scalar multiple) $a\mathbf{v}$ is a vector in $\mathbb{R}^n$.
(vii) (Distribution) $a(\mathbf{u} + \mathbf{v}) = a\mathbf{u} + a\mathbf{v}$.
(viii) (Distribution) $(a + b)\mathbf{u} = a\mathbf{u} + b\mathbf{u}$.
(ix) (Associativity of scalar multiplication) $(ab)\mathbf{u} = a(b\mathbf{u})$.
(x) If $a\mathbf{u} = \mathbf{0}$, then either $a = 0$ or $\mathbf{u} = \mathbf{0}$.

A linear combination of $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_k \in \mathbb{R}^n$ is
$$c_1\mathbf{u}_1 + c_2\mathbf{u}_2 + \dots + c_k\mathbf{u}_k, \text{ for some } c_1, c_2, \dots, c_k \in \mathbb{R}.$$

### Abstract Vector Spaces
Definition
A set $V$ equipped with addition and scalar multiplication is said to be a vector space over $\mathbb{R}$ if it satisfies the following axioms.
1. For any vectors $\mathbf{u}, \mathbf{v}$ in $V$, the sum $\mathbf{u} + \mathbf{v}$ is in $V$.
2. (Commutative) For any vectors $\mathbf{u}, \mathbf{v}$ in $V, \mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u}$.
3. (Associative) For any vectors $\mathbf{u}, \mathbf{v}, \mathbf{w}$ in $V, \mathbf{u} + (\mathbf{v} + \mathbf{w}) = (\mathbf{u} + \mathbf{v}) + \mathbf{w}$.
4. (Zero vector) There is a vector $\mathbf{0}$ in $V$ such that $\mathbf{0} + \mathbf{v} = \mathbf{v}$ for all vectors $\mathbf{v}$ in $V$.
5. (Negative) For any vector $\mathbf{u}$ in $V$, there exists a vector $-\mathbf{u}$ in $V$ such that $\mathbf{u} + (-\mathbf{u}) = \mathbf{0}$.
6. For any scalar $a$ in $\mathbb{R}$ and vector $\mathbf{v}$ in $V, a\mathbf{v}$ is a vector in $V$.
7. (Distribution) For any scalar $a$ in $\mathbb{R}$ and vectors $\mathbf{u}, \mathbf{v}$ in $V, a(\mathbf{u} + \mathbf{v}) = a\mathbf{u} + a\mathbf{v}$.
8. (Distribution) For any scalars $a, b$ in $\mathbb{R}$ and vector $\mathbf{u}$ in $V, (a + b)\mathbf{u} = a\mathbf{u} + b\mathbf{u}$.
9. (Associativity of scalar multiplication) For any scalars $a, b$ in $\mathbb{R}$ and vector $\mathbf{u}$ in $V, a(b\mathbf{u}) = (ab)\mathbf{u}$.
10. For any vector $\mathbf{u}$ in $V, 1\mathbf{u} = \mathbf{u}$.