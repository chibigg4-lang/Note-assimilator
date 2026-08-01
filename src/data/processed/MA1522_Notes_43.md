# Transaction matrices

Let $V$ be a subspace of $\mathbb{R}^n$. Suppose $S = \{\mathbf{u}_1, \dots, \mathbf{u}_k\}$ and $T = \{\mathbf{v}_1, \dots, \mathbf{v}_k\}$ are bases for the subspace $V$. Define the transition matrix from $T$ to $S$ to be
$$ \mathbf{P} = \left( [\mathbf{v}_1]_S \quad [\mathbf{v}_2]_S \quad \dots \quad [\mathbf{v}_k]_S \right), $$
the matrix whose columns are the coordinates of the vectors in $T$ relative to the basis $S$.

**Theorem** (Transition matrix)
Let $V$ be a subspace of $\mathbb{R}^n$. Suppose $S = \{\mathbf{u}_1, \dots, \mathbf{u}_k\}$ and $T = \{\mathbf{v}_1, \dots, \mathbf{v}_k\}$ are bases for the subspace $V$. Let $\mathbf{P}$ be the transition matrix from $T$ to $S$. Then for any vector $\mathbf{w}$ in $V$,
$$ [\mathbf{w}]_S = \mathbf{P} [\mathbf{w}]_T. $$

**Algorithm to find Transition Matrix**
Let $S = \{\mathbf{u}_1, \dots, \mathbf{u}_k\}$ and $T = \{\mathbf{v}_1, \dots, \mathbf{v}_k\}$ be basis for a subspace $V$ in $\mathbb{R}^n$. To find $\mathbf{P}$, the transition matrix from $T$ to $S$
$$ ( \text{ " } S \text{ " } | \text{ " } T \text{ " } ) = \left( \begin{array}{ccc|ccc} \mathbf{u}_1 & \mathbf{u}_2 & \dots & \mathbf{u}_k & \mathbf{v}_1 & \mathbf{v}_2 & \dots & \mathbf{v}_k \end{array} \right) \xrightarrow{rref} \left( \begin{array}{c|c} \mathbf{I}_k & \mathbf{P} \\ \mathbf{0}_{(n-k) \times k} & \mathbf{0}_{(n-k) \times k} \end{array} \right), $$

---

### Example
Suppose $S = \{\mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3\}$ is a basis for a subspace $V$ of $\mathbb{R}^n$. Let $T = \{\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3\}$ be such that
$$ \mathbf{v}_1 = \mathbf{u}_1, $$
$$ \mathbf{v}_2 = \mathbf{u}_1 + \mathbf{u}_2, $$
$$ \mathbf{v}_3 = \mathbf{u}_1 + \mathbf{u}_2 + \mathbf{u}_3. $$

Further, let us write the coordinates of the vectors in $T$ relative to the basis $S$,
$$ [\mathbf{v}_1]_S = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \quad [\mathbf{v}_2]_S = \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}, \quad [\mathbf{v}_3]_S = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}. $$

$$ [\mathbf{v}]_S = \underbrace{\begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{pmatrix}}_{\mathbf{P}} [\mathbf{v}]_T. $$
*(Note: arrows indicate $[\mathbf{v}_1]_S, [\mathbf{v}_2]_S, [\mathbf{v}_3]_S$ as columns of $\mathbf{P}$)*

$$ [\mathbf{v}]_S = \left( \begin{array}{ccc} [\mathbf{v}_1]_S & [\mathbf{v}_2]_S & [\mathbf{v}_3]_S \end{array} \right) [\mathbf{v}]_T. $$