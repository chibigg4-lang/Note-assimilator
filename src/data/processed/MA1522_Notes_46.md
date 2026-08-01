# Ranks

Let $\mathbf{A}$ be a $m \times n$ matrix and $\mathbf{R}$ its reduced row-echelon form.
$$\dim(\text{Col}(\mathbf{A})) = \# \text{ of pivot columns in RREF of } \mathbf{A},$$
$$= \# \text{ of leading entries in RREF of } \mathbf{A},$$
$$= \# \text{ of nonzero rows in RREF of } \mathbf{A} = \dim(\text{Row}(\mathbf{A}))$$

**Definition**
Define the rank of $\mathbf{A}$ to be the dimension of its column space or row space
$$rank(\mathbf{A}) = \dim(\text{Col}(\mathbf{A})) = \dim(\text{Row}(\mathbf{A})).$$

**Exercise**
Prove that the rank is invariant under transpose,
$$rank(\mathbf{A}) = rank(\mathbf{A}^T).$$

**Challenge**
Prove the following theorem.

**Theorem**
The linear system $\mathbf{A}\mathbf{x} = \mathbf{b}$ is consistent if and only if
the rank of $\mathbf{A}$ is equal to the rank of the augmented matrix $(\mathbf{A} \mid \mathbf{b})$.
$$rank(\mathbf{A}) = rank((\mathbf{A} \mid \mathbf{b})).$$

**Lemma**
Let $\mathbf{A}$ be a $m \times n$ matrix and $\mathbf{B}$ a $n \times p$ matrix. The column space of the product $\mathbf{AB}$ is a subspace of the column space of $\mathbf{A}$.
$$\text{Col}(\mathbf{AB}) \subseteq \text{Col}(\mathbf{A}).$$

**Theorem**
Let $\mathbf{A}$ be a $m \times n$ matrix and $\mathbf{B}$ a $n \times p$ matrix. Then
$$rank(\mathbf{AB}) \leq \min\{rank(\mathbf{A}), rank(\mathbf{B})\}.$$

**Question**
Show that if $\mathbf{A}$ and $\mathbf{B}$ are row equivalent matrices, then $rank(\mathbf{A}) = rank(\mathbf{B})$.

**Theorem** (Rank-Nullity Theorem)
Let $\mathbf{A}$ be a $m \times n$ matrix. The sum of its rank and nullity is equal to the number of columns,
$$rank(\mathbf{A}) + nullity(\mathbf{A}) = n.$$

**Summary**
Let $\mathbf{A}$ be a $m \times n$ matrix.

| Subspace | Subspace of | Basis | Dimension |
| :--- | :--- | :--- | :--- |
| $\text{Col}(\mathbf{A})$ | $\mathbb{R}^m$ | Columns of $\mathbf{A}$ corresponding to pivot columns in RREF. | $rank(\mathbf{A}) = \text{number of pivot columns in RREF.}$ |
| $\text{Row}(\mathbf{A})$ | $\mathbb{R}^n$ | Nonzero rows of RREF. | $rank(\mathbf{A}) = \text{number of nonzero rows of RREF.}$ |
| $\text{Null}(\mathbf{A})$ | $\mathbb{R}^n$ | Vectors in general solution to $\mathbf{A}\mathbf{x} = \mathbf{0}.$ | $nullity(\mathbf{A}) = \text{number of non-pivot columns in RREF.}$ |