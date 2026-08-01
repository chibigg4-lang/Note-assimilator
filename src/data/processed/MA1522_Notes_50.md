# Orthogonal matrices

## Discussion

Let $S = \{ \mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_k \}$ be a set of vectors in $\mathbb{R}^n$. Construct the $n \times k$ matrix $\mathbf{Q} = (\mathbf{u}_1 \quad \mathbf{u}_2 \quad \dots \quad \mathbf{u}_k)$ whose columns are the vectors in $S$. Consider the product

$$
\mathbf{Q}^T \mathbf{Q} = 
\begin{pmatrix} 
\mathbf{u}_1^T \\ \mathbf{u}_2^T \\ \vdots \\ \mathbf{u}_k^T 
\end{pmatrix} 
(\mathbf{u}_1 \quad \mathbf{u}_2 \quad \dots \quad \mathbf{u}_k) = 
\begin{pmatrix} 
\mathbf{u}_1^T \mathbf{u}_1 & \mathbf{u}_1^T \mathbf{u}_2 & \dots & \mathbf{u}_1^T \mathbf{u}_k \\ 
\mathbf{u}_2^T \mathbf{u}_1 & \mathbf{u}_2^T \mathbf{u}_2 & \dots & \mathbf{u}_2^T \mathbf{u}_k \\ 
\vdots & \vdots & \ddots & \vdots \\ 
\mathbf{u}_k^T \mathbf{u}_1 & \mathbf{u}_k^T \mathbf{u}_2 & \dots & \mathbf{u}_k^T \mathbf{u}_k 
\end{pmatrix} = 
\begin{pmatrix} 
\mathbf{u}_1 \cdot \mathbf{u}_1 & \mathbf{u}_1 \cdot \mathbf{u}_2 & \dots & \mathbf{u}_1 \cdot \mathbf{u}_k \\ 
\mathbf{u}_2 \cdot \mathbf{u}_1 & \mathbf{u}_2 \cdot \mathbf{u}_2 & \dots & \mathbf{u}_2 \cdot \mathbf{u}_k \\ 
\vdots & \vdots & \ddots & \vdots \\ 
\mathbf{u}_k \cdot \mathbf{u}_1 & \mathbf{u}_k \cdot \mathbf{u}_2 & \dots & \mathbf{u}_k \cdot \mathbf{u}_k 
\end{pmatrix}
$$

that is, the $(i, j)$-entry of the product $\mathbf{Q}^T \mathbf{Q}$ is the inner product $\mathbf{u}_i \cdot \mathbf{u}_j$. Hence,

$$
S \text{ is } 
\begin{cases} 
\text{orthogonal} \\ 
\text{orthonormal} 
\end{cases} 
\iff \mathbf{Q}^T \mathbf{Q} \text{ is } 
\begin{cases} 
\text{a diagonal matrix} \\ 
\text{the identity matrix} 
\end{cases}
$$

* In particular, if $k=n$, then $\mathbf{Q}$ is a square matrix and $\mathbf{Q}^T \mathbf{Q} = \mathbf{I}_n$ implies that $\mathbf{Q}^T = \mathbf{Q}^{-1}$.
* That is, $S$ is orthonormal if and only if $\mathbf{Q}^T = \mathbf{Q}^{-1}$.

---

### Definition
An $n \times n$ square matrix $\mathbf{A}$ is orthogonal if $\mathbf{A}^T = \mathbf{A}^{-1}$, equivalently, $\mathbf{A}^T \mathbf{A} = \mathbf{I} = \mathbf{A} \mathbf{A}^T$.

### Theorem
Let $\mathbf{A}$ be a square matrix of order $n$. The following statements are equivalent:
(i) $\mathbf{A}$ is an orthogonal matrix.
(ii) The columns of $\mathbf{A}$ form an orthonormal basis for $\mathbb{R}^n$.
(iii) The rows of $\mathbf{A}$ form an orthonormal basis for $\mathbb{R}^n$.

# Orthogonal Projection

Let $S = \{ \mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_k \}$ be a linearly independent set. Let

$$
\begin{aligned}
\mathbf{v}_1 &= \mathbf{u}_1 \\
\mathbf{v}_2 &= \mathbf{u}_2 - \left( \frac{\mathbf{v}_1 \cdot \mathbf{u}_2}{\|\mathbf{v}_1\|^2} \right) \mathbf{v}_1 \\
\mathbf{v}_3 &= \mathbf{u}_3 - \left( \frac{\mathbf{v}_1 \cdot \mathbf{u}_3}{\|\mathbf{v}_1\|^2} \right) \mathbf{v}_1 - \left( \frac{\mathbf{v}_2 \cdot \mathbf{u}_3}{\|\mathbf{v}_2\|^2} \right) \mathbf{v}_2 \\
&\vdots \\
\mathbf{v}_k &= \mathbf{u}_k - \left( \frac{\mathbf{v}_1 \cdot \mathbf{u}_k}{\|\mathbf{v}_1\|^2} \right) \mathbf{v}_1 - \left( \frac{\mathbf{v}_2 \cdot \mathbf{u}_k}{\|\mathbf{v}_2\|^2} \right) \mathbf{v}_2 - \dots - \left( \frac{\mathbf{v}_{k-1} \cdot \mathbf{u}_k}{\|\mathbf{v}_{k-1}\|^2} \right) \mathbf{v}_{k-1}
\end{aligned}
$$

Then $\{ \mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_k \}$ is an orthogonal set (of nonzero vectors), and hence,

$$
\left\{ \frac{\mathbf{v}_1}{\|\mathbf{v}_1\|}, \frac{\mathbf{v}_2}{\|\mathbf{v}_2\|}, \dots, \frac{\mathbf{v}_k}{\|\mathbf{v}_k\|} \right\}
$$

is an orthonormal set such that $\text{span}\{ \mathbf{v}_1, \dots, \mathbf{v}_k \} = \text{span}\{ \mathbf{u}_k, \dots, \mathbf{u}_k \}$.