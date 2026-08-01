# Orthogonal and orthonormal bases

### Theorem
Suppose $S = \{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_k\}$ is an orthogonal set of nonzero vectors. Then $S$ is linearly independent.

### Theorem
Every orthonormal set is linearly independent.

### Definition
Let $V$ be a subspace of $\mathbb{R}^n$. A set $S \subseteq V$ is an orthogonal basis (resp. orthonormal basis) of $V$ if $S$ is a basis of $V$ and $S$ is an orthogonal (resp. orthonormal) set.

***

## Coordinates Relative to an Orthogonal Basis

### Theorem
Let $S = \{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_k\}$ be an orthogonal basis for a subspace $V$ of $\mathbb{R}^n$. Then for any $\mathbf{v} \in V$,
$$\mathbf{v} = \left( \frac{\mathbf{v} \cdot \mathbf{u}_1}{\|\mathbf{u}_1\|^2} \right) \mathbf{u}_1 + \left( \frac{\mathbf{v} \cdot \mathbf{u}_2}{\|\mathbf{u}_2\|^2} \right) \mathbf{u}_2 + \dots + \left( \frac{\mathbf{v} \cdot \mathbf{u}_k}{\|\mathbf{u}_k\|^2} \right) \mathbf{u}_k$$

If further $S$ is an orthonormal basis, then
$$\mathbf{v} = (\mathbf{v} \cdot \mathbf{u}_1) \mathbf{u}_1 + (\mathbf{v} \cdot \mathbf{u}_2) \mathbf{u}_2 + \dots + (\mathbf{v} \cdot \mathbf{u}_k) \mathbf{u}_k$$

that is $S$ orthogonal, $[\mathbf{v}]_S = \begin{pmatrix} \frac{\mathbf{v} \cdot \mathbf{u}_1}{\|\mathbf{u}_1\|^2} \\ \frac{\mathbf{v} \cdot \mathbf{u}_2}{\|\mathbf{u}_2\|^2} \\ \vdots \\ \frac{\mathbf{v} \cdot \mathbf{u}_k}{\|\mathbf{u}_k\|^2} \end{pmatrix}$, $S$ orthonormal, $[\mathbf{v}]_S = \begin{pmatrix} \mathbf{v} \cdot \mathbf{u}_1 \\ \mathbf{v} \cdot \mathbf{u}_2 \\ \vdots \\ \mathbf{v} \cdot \mathbf{u}_k \end{pmatrix}$.

***

### Example
$S = \left\{ \frac{1}{\sqrt{3}} \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}, \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix} \right\}$ and $V = \text{span}(S)$. $S$ is an orthonormal basis for $V$. Let $\mathbf{v} = \begin{pmatrix} 2 \\ 1 \\ 0 \end{pmatrix} \in V$. Then

$$\mathbf{v} = \left( \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} \cdot \begin{pmatrix} 2 \\ 1 \\ 0 \end{pmatrix} \right) \frac{1}{\sqrt{3}} \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} + \left( \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix} \cdot \begin{pmatrix} 2 \\ 1 \\ 0 \end{pmatrix} \right) \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix}$$
$$= \underbrace{\left( \frac{3}{\sqrt{3}} \right)}_{c_1} \frac{1}{\sqrt{3}} \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} + \left( \frac{2}{\sqrt{2}} \right) \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix}$$

That is,
$$[\mathbf{v}]_S = \begin{pmatrix} \sqrt{3} \\ \sqrt{2} \end{pmatrix}.$$