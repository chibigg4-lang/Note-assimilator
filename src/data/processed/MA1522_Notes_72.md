A mapping (function) $T : \mathbb{R}^n \to \mathbb{R}^m$, is a **linear transformation** if for all vectors $\mathbf{u}, \mathbf{v}$ in $\mathbb{R}^n$, and scalars $\alpha, \beta$,
$$T(\alpha \mathbf{u} + \beta \mathbf{v}) = \alpha T(\mathbf{u}) + \beta T(\mathbf{v}).$$

The Euclidean space $\mathbb{R}^n$ is called the **domain** of the mapping, and the Euclidean space $\mathbb{R}^m$ is called the **codomain** of the mapping.

Equivalently, a mapping $T : \mathbb{R}^n \to \mathbb{R}^m$, is a **linear transformation** if it satisfies the following properties.
I. For any vector $\mathbf{u}$ in $\mathbb{R}^n$ and scalar $\alpha$,
$$T(\alpha \mathbf{u}) = \alpha T(\mathbf{u}).$$
II. For any vectors $\mathbf{u}, \mathbf{v}$ in $\mathbb{R}^n$,
$$T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v}).$$
By induction, we have that for any vectors $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_k$ in $\mathbb{R}^n$ and scalars $c_1, c_2, \dots, c_k$,
$$T(c_1 \mathbf{u}_1 + c_2 \mathbf{u}_2 + \dots + c_k \mathbf{u}_k) = c_1 T(\mathbf{u}_1) + c_2 T(\mathbf{u}_2) + \dots + c_k T(\mathbf{u}_k).$$

Any $m \times n$ matrix $\mathbf{A}$ defines a linear transformation $T_A : \mathbb{R}^n \to \mathbb{R}^m$ by multiplication,
$$T_A(\mathbf{u}) = \mathbf{A}\mathbf{u} \quad \text{for any } \mathbf{u} \in \mathbb{R}^n.$$

A mapping $\mathbf{T} : \mathbb{R}^n \to \mathbb{R}^m$ is **not a linear transformation** if any of the following statements hold.
I. $\mathbf{T}$ does not map the zero vector to the zero vector, $\mathbf{T}(\mathbf{0}) \neq \mathbf{0}$.
II. There is a scalar $\alpha$ and a vector $\mathbf{u}$ in $\mathbb{R}^n$ such that $\mathbf{T}(\alpha \mathbf{u}) \neq \alpha \mathbf{T}(\mathbf{u})$.
III. There are vectors $\mathbf{u}, \mathbf{v}$ in $\mathbb{R}^n$ such that $\mathbf{T}(\mathbf{u} + \mathbf{v}) \neq \mathbf{T}(\mathbf{u}) + \mathbf{T}(\mathbf{v})$.

***

Let $\mathbf{A} = \begin{pmatrix} 1 & 0 & 1 & -1 \\ 2 & 1 & -1 & -1 \\ 1 & -1 & 0 & 2 \end{pmatrix}$. Then $\mathbf{A}$ defines a linear transformation defined $T$ by matrix multiplication.
1. What are the domain and codomain of $T$?
   $A_{3 \times 4} v_{4 \times 1} = u_{3 \times 1}$.  $T : \mathbb{R}^4 \to \mathbb{R}^3$.
2. Write down the formula of $T$.
   $T \begin{pmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 1 & -1 \\ 2 & 1 & -1 & -1 \\ 1 & -1 & 0 & 2 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{pmatrix} = \begin{pmatrix} x_1 + x_3 - x_4 \\ 2x_1 + x_2 - x_3 - x_4 \\ x_1 - x_2 + 2x_4 \end{pmatrix}$.