### Discussion

Let $S = \{\mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3, \mathbf{u}_4\}$ be a set in $\mathbb{R}^4$. After performing the Gram-Schmidt process on $S$, $\mathbf{v}_4 = \mathbf{0}$, but $\mathbf{v}_3 \neq \mathbf{0}$. What can you conclude?

$$ \mathbf{0} = \mathbf{v}_4 = \mathbf{u}_4 - \text{proj } \mathbf{u}_4 \text{ onto } \underbrace{\text{span}\{\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3\}}_{=\text{span}\{\mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3\}} $$

$$ \Rightarrow \mathbf{u}_4 = \text{proj } \mathbf{u}_4 \text{ onto } \text{span}\{\mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3\} \Rightarrow \mathbf{u}_4 \in \text{span}\{\mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3\} \Rightarrow S \text{ linearly dependent.} $$

# QR factorization

Suppose now $\mathbf{A}$ is a $m \times n$ matrix with linearly independent columns, i.e. $\text{rank}(\mathbf{A}) = n$. Write
$$ \mathbf{A} = (\mathbf{a}_1 \quad \mathbf{a}_2 \quad \dots \quad \mathbf{a}_n). $$

Since the set $S = \{\mathbf{a}_1, \mathbf{a}_2, \dots, \mathbf{a}_n\}$ is linearly independent we may apply the Gram-Schmidt process on $S$ to obtain an orthonormal set $\{\mathbf{q}_1, \mathbf{q}_2, \dots, \mathbf{q}_n\}$. Set
$$ \mathbf{Q} = (\mathbf{q}_1 \quad \mathbf{q}_2 \quad \dots \quad \mathbf{q}_n). $$

Recall that for any $j = 1, 2, \dots, n, \text{span}\{\mathbf{a}_1, \mathbf{a}_2, \dots, \mathbf{a}_j\} = \text{span}\{\mathbf{q}_1, \mathbf{q}_2, \dots, \mathbf{q}_j\}$. In particular, $\mathbf{a}_j$ is in $\text{span}\{\mathbf{q}_1, \mathbf{q}_2, \dots, \mathbf{q}_j\}$. Thus we may write

$$ \mathbf{a}_j = r_{1j}\mathbf{q}_1 + r_{2j}\mathbf{q}_2 + \dots + r_{jj}\mathbf{q}_j + 0\mathbf{q}_{j+1} + \dots + 0\mathbf{q}_n = (\mathbf{q}_1 \quad \dots \quad \mathbf{q}_j \quad \dots \quad \mathbf{q}_n) \begin{pmatrix} r_{1j} \\ \vdots \\ r_{jj} \\ 0 \\ \vdots \\ 0 \end{pmatrix} $$