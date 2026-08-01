Let $S = \{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_k\}$ be a linearly independent set. Let
$$
\begin{aligned}
\mathbf{v}_1 &= \mathbf{u}_1 \\
\mathbf{v}_2 &= \mathbf{u}_2 - \left( \frac{\mathbf{v}_1 \cdot \mathbf{u}_2}{\|\mathbf{v}_1\|^2} \right) \mathbf{v}_1 \\
\mathbf{v}_3 &= \mathbf{u}_3 - \left( \frac{\mathbf{v}_1 \cdot \mathbf{u}_3}{\|\mathbf{v}_1\|^2} \right) \mathbf{v}_1 - \left( \frac{\mathbf{v}_2 \cdot \mathbf{u}_3}{\|\mathbf{v}_2\|^2} \right) \mathbf{v}_2 \\
&\vdots \\
\mathbf{v}_k &= \mathbf{u}_k - \left( \frac{\mathbf{v}_1 \cdot \mathbf{u}_k}{\|\mathbf{v}_1\|^2} \right) \mathbf{v}_1 - \left( \frac{\mathbf{v}_2 \cdot \mathbf{u}_k}{\|\mathbf{v}_2\|^2} \right) \mathbf{v}_2 - \dots - \left( \frac{\mathbf{v}_{k-1} \cdot \mathbf{u}_k}{\|\mathbf{v}_{k-1}\|^2} \right) \mathbf{v}_{k-1}.
\end{aligned}
$$
Then $\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_k\}$ is an orthogonal set (of nonzero vectors), and hence,
$$
\left\{ \frac{\mathbf{v}_1}{\|\mathbf{v}_1\|}, \frac{\mathbf{v}_2}{\|\mathbf{v}_2\|}, \dots, \frac{\mathbf{v}_k}{\|\mathbf{v}_k\|} \right\}
$$
is an orthonormal set such that $\text{span}\{\mathbf{v}_1, \dots, \mathbf{v}_k\} = \text{span}\{\mathbf{u}_1, \dots, \mathbf{u}_k\}$.

---

# Best Approximation Theorem

**Theorem (Best approximation theorem)**
Let $V$ be a subspace of $\mathbb{R}^n$ and $\mathbf{w}$ a vector in $\mathbb{R}^n$. Let $\mathbf{w}_p$ be the projection of $\mathbf{w}$ onto $V$. Then $\mathbf{w}_p$ is vector in $V$ closest to $\mathbf{w}$; that is,
$$\|\mathbf{w} - \mathbf{w}_p\| \le \|\mathbf{w} - \mathbf{v}\|$$
for all $\mathbf{v}$ in $V$.

**Proof.**
$\mathbf{v} \in V, \quad \mathbf{v}-\mathbf{w}_p \in V. \quad \mathbf{w}_n = \mathbf{w}-\mathbf{w}_p \perp V. \Rightarrow \mathbf{w}-\mathbf{w}_p \perp \mathbf{v}-\mathbf{w}.$
By pythagorean theorem,
$$\|\mathbf{w} - \mathbf{v}\|^2 = \|\mathbf{w} - \mathbf{w}_p\|^2 + \underbrace{\|\mathbf{v} - \mathbf{w}_p\|^2}_{\ge 0.}.$$
$$\|\mathbf{w} - \mathbf{w}_p\|^2 \le \|\mathbf{w} - \mathbf{v}\|^2 \Rightarrow \|\mathbf{w}-\mathbf{w}_p\| \le \|\mathbf{w}-\mathbf{v}\|.$$