### Discussion

Recall that the general solution of a homogeneous system $\mathbf{A}\mathbf{x} = \mathbf{0}$ has the form
$$s_1\mathbf{v}_1 + s_2\mathbf{v}_2 + \dots + s_k\mathbf{v}_k, \quad s_1, s_2, \dots, s_k \in \mathbb{R}.$$
Explicitly, the solution set is
$$V = \{ \ s_1\mathbf{v}_1 + s_2\mathbf{v}_2 + \dots + s_k\mathbf{v}_k \mid s_1, s_2, \dots, s_k \in \mathbb{R} \}.$$
Observe however that this is just $\text{span}\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_k\}$,
$$V = \{ \ s_1\mathbf{v}_1 + s_2\mathbf{v}_2 + \dots + s_k\mathbf{v}_k \mid s_1, s_2, \dots, s_k \in \mathbb{R} \} = \text{span}\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_k\}.$$
By the properties of a linear span, this would mean that the solution set to a homogeneous system is a vector space that is a subset of the Euclidean vector space. We call a vector space nested inside another vector space a subspace.

***

**Definition**
A subset $V$ of $\mathbb{R}^n$ is a subspace if it satisfies the following properties.
I. $V$ contains the zero vector $\mathbf{0} \in V$.
II. $V$ is closed under scalar multiplication. For any vector $\mathbf{v}$ in $V$ and scalar $\alpha$, the vector $\alpha\mathbf{v}$ is in $V$.
III. $V$ is closed under addition. For any vectors $\mathbf{u}, \mathbf{v}$ in $V$, the sum $\mathbf{u} + \mathbf{v}$ is in $V$.

Property (i) can be replaced with property (i'): $V$ is nonempty.
Properties (ii) and (iii) is equivalent to property (ii'):
$V$ is closed under linear combination. For any $\mathbf{u}, \mathbf{v}$ in $V$, and scalars $\alpha, \beta$, the linear combination $\alpha\mathbf{u} + \beta\mathbf{v}$ is in $V$.

**Theorem** (Solution set of a homogeneous system is a subspace)
The solution set $V = \{ \ \mathbf{u} \mid \mathbf{A}\mathbf{u} = \mathbf{b} \ \}$ to a linear system $\mathbf{A}\mathbf{x} = \mathbf{b}$ is a subspace if and only if $\mathbf{b} = \mathbf{0}$, that is, the system is homogeneous.

**Definition**
The solution set to a homogeneous system is call a solution space.

# Equivalent definition for subspace:

**Check if a set is a subspace**
To show that a set $V$ is a subspace, we can either
* find a spanning set, that is find a set $S$ such that $V = \text{span}(S)$, or
* show that $V$ satisfies the 3 conditions of being a subspace.

To show that a subset $V$ is not a subspace, we can either
* show that it does not contain the zero vector, $\mathbf{0} \notin V$,
* find a vector $\mathbf{v} \in V$ and a scalar $\alpha \in \mathbb{R}$ such that $\alpha\mathbf{v} \notin V$, or
* find vectors $\mathbf{u}, \mathbf{v} \in V$ such that the sum is not in $V$, $\mathbf{u} + \mathbf{v} \notin V$.