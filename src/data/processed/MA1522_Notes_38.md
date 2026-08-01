Special cases.

### Special Cases

1. $\{0\}$, where $0 \in \mathbb{R}^n$ is the zero vector is always linearly dependent.
   $c_10=0$
2. If $\mathbf{v} \neq 0$, then $\{\mathbf{v}\} \in \mathbb{R}^n$ is linearly independent.
   $c_1 \mathbf{v} = 0 \Rightarrow c_1 = 0$
   ($c_1 \neq 0$ is implied under $\mathbf{v} \neq 0$)
3. $\{\mathbf{v}_1, \mathbf{v}_2\}$ is linearly dependent if and only if one is a scalar multiple of the other, $\alpha\mathbf{v}_1 = \mathbf{v}_2$ or $\mathbf{v}_1 = \beta\mathbf{v}_2$.
   $c_1\mathbf{v}_1 + c_2\mathbf{v}_2 = 0 \quad \mathbf{v}_1 = \frac{c_2}{-c_1} \mathbf{v}_2 \quad \alpha\mathbf{v}_1 = \mathbf{v}_2 \quad \alpha\mathbf{v}_1 - \mathbf{v}_2 = 0$
4. The empty set $\{\} = \varnothing$ is linearly independent.

Basis and Coordinates:

**Definition**
Let $V$ be a subspace of $\mathbb{R}^n$. A set $S = \{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_k\}$ is a **basis** for $V$ if
(i) $span(S) = V$ and
(ii) $S$ is linearly independent.

**Theorem**
Suppose $S\{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_k\}$ is a basis for $V$. Then every vector $\mathbf{v}$ in the subspace $V$ can be written as a linear combination of vectors in $S$ uniquely.

### Basis for Solution Set of Homogeneous System

**Theorem**
Let $V = \{\mathbf{u} | A\mathbf{u} = \mathbf{0}\}$ be the solution space to some homogeneous system. Suppose
$$s_1\mathbf{u}_1 + s_2\mathbf{u}_2 \dots + s_k\mathbf{u}_k, s_1, s_2, \dots s_k \in \mathbb{R}$$
is a general solution to the homogeneous system $A\mathbf{x} = \mathbf{0}$.
Then $\{\mathbf{u}_1 \mathbf{u}_2 \dots \mathbf{u}_k\}$ is a basis for the subspace $V = \{\mathbf{u} | A\mathbf{u} = \mathbf{0}\}$.

**Theorem**
Basis for the zero space $\{0\}$ of $\mathbb{R}^n$ is the empty set $\{\}$ or $\varnothing$.