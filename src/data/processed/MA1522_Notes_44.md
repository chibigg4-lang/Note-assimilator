### Algorithm to find Transition Matrix
Let $S = \{\mathbf{u}_1, ..., \mathbf{u}_k\}$ and $T = \{\mathbf{v}_1, ..., \mathbf{v}_k\}$ be basis for a subspace $V$ in $\mathbb{R}^n$.

* To find $\mathbf{P}$, the transition matrix from $T$ to $S$, we need to find $[\mathbf{v}_i]_S$ for $i = 1, 2, ..., k$.
* This is equivalent to solving $( \mathbf{u}_1 \quad \mathbf{u}_2 \quad \dots \quad \mathbf{u}_k \mid \mathbf{v}_i )$ for $i = 1, 2, ..., k$.
* Since these linear systems have the same coefficient matrix, we can solve them simultaneously,
$$( \mathbf{u}_1 \quad \mathbf{u}_2 \quad \dots \quad \mathbf{u}_k \mid \mathbf{v}_1 \quad \mathbf{v}_2 \quad \dots \quad \mathbf{v}_k ).$$
* Now since $S$ is a basis, the system must have a unique solution, and the reduced row-echelon form of the augmented matrix above will be of the form
$$ \left( \begin{array}{c|c} \mathbf{I}_k & [\mathbf{v}_1]_S \quad [\mathbf{v}_2]_S \quad \dots \quad [\mathbf{v}_k]_S \\ \mathbf{0}_{(n-k) \times k} & \mathbf{0} \quad \quad \quad \mathbf{0} \quad \quad \dots \quad \quad \mathbf{0} \end{array} \right) = \left( \begin{array}{c|c} \mathbf{I}_k & \mathbf{P} \\ \mathbf{0}_{(n-k) \times k} & \mathbf{0}_{(n-k) \times k} \end{array} \right) $$
where $\mathbf{P}$ is the transition matrix from $T$ to $S$.
In summary,
$$( \text{"}S\text{"} \mid \text{"}T\text{"} ) = ( \mathbf{u}_1 \quad \mathbf{u}_2 \quad \dots \quad \mathbf{u}_k \mid \mathbf{v}_1 \quad \mathbf{v}_2 \quad \dots \quad \mathbf{v}_k ) \xrightarrow{\text{rref}} \left( \begin{array}{c|c} \mathbf{I}_k & \mathbf{P} \\ \mathbf{0}_{(n-k) \times k} & \mathbf{0}_{(n-k) \times k} \end{array} \right),$$

---

### Example
Suppose $S = \left\{ \mathbf{u}_1 = \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}, \mathbf{u}_2 = \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix}, \mathbf{u}_3 = \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} \right\}$, $T = \left\{ \mathbf{v}_1 = \begin{pmatrix} 1 \\ 1 \\ -1 \end{pmatrix}, \mathbf{v}_2 = \begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix}, \mathbf{v}_3 = \begin{pmatrix} -1 \\ 1 \\ 1 \end{pmatrix} \right\}$.

The transition matrix from $T$ to $S$ is
$$ \left( \begin{array}{ccc|ccc} 1 & 0 & 1 & 1 & 1 & -1 \\ 0 & 1 & 1 & 1 & -1 & 1 \\ 1 & 1 & 0 & -1 & 1 & 1 \end{array} \right) \xrightarrow{\text{rref}} \left( \begin{array}{ccc|ccc} 1 & 0 & 0 & -1/2 & 3/2 & -1/2 \\ 0 & 1 & 0 & -1/2 & -1/2 & 3/2 \\ 0 & 0 & 1 & 3/2 & -1/2 & -1/2 \end{array} \right) \Rightarrow \mathbf{P} = \begin{pmatrix} -1/2 & 3/2 & -1/2 \\ -1/2 & -1/2 & 3/2 \\ 3/2 & -1/2 & -1/2 \end{pmatrix}. $$
Let $\mathbf{w} = \begin{pmatrix} 1 \\ 2 \\ 2 \end{pmatrix}, \left( \begin{array}{ccc|c} 1 & 1 & -1 & 1 \\ 1 & -1 & 1 & 2 \\ -1 & 1 & 1 & 2 \end{array} \right) \xrightarrow{\text{rref}} \left( \begin{array}{ccc|c} 1 & 0 & 0 & 3/2 \\ 0 & 1 & 0 & 3/2 \\ 0 & 0 & 1 & 2 \end{array} \right) \Rightarrow [\mathbf{w}]_T = \begin{pmatrix} 3/2 \\ 3/2 \\ 2 \end{pmatrix}$.
$$ \begin{pmatrix} 1/2 \\ 3/2 \\ 1/2 \end{pmatrix} = [\mathbf{w}]_S = \mathbf{P}[\mathbf{w}]_T = \begin{pmatrix} -1/2 & 3/2 & -1/2 \\ -1/2 & -1/2 & 3/2 \\ 3/2 & -1/2 & -1/2 \end{pmatrix} \begin{pmatrix} 3/2 \\ 3/2 \\ 2 \end{pmatrix} $$