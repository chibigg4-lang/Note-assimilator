# Dot product, norm, distance.

dot product:
$$u \cdot v = u^T \cdot v = (u_1 \ u_2 \ \dots \ u_n) \begin{pmatrix} v_1 \\ \dots \\ \dots \\ v_n \end{pmatrix}$$

$$= u_1v_1 + u_2v_2 + \dots + u_nv_n$$
$$= \sum_{i=1}^n u_iv_i$$

The **inner product** (or **dot product**) of vectors $\mathbf{u} = (u_i)$ and $\mathbf{v} = (v_i)$ in $\mathbb{R}^n$ is defined to be
$$\mathbf{u} \cdot \mathbf{v} = u_1v_1 + u_2v_2 + \dots + u_nv_n.$$

Define the **norm** of a vector $\mathbf{u} \in \mathbb{R}^n$, $\mathbf{u} = (u_i)$, to be the square root of the inner product of $\mathbf{u}$ with itself, and is denoted as $\|\mathbf{u}\|$,
$$\|\mathbf{u}\| = \sqrt{\mathbf{u} \cdot \mathbf{u}} = \sqrt{u_1^2 + u_2^2 + \dots + u_n^2}.$$

This is also known as the **length** or **magnitude** of the vector.

**Theorem** (Properties of inner product and norm)
Let $\mathbf{u}, \mathbf{v} \in \mathbb{R}^n$ be vectors and $a, b, c \in \mathbb{R}$ be real numbers.
(i) Inner product is symmetric,
$$\mathbf{u} \cdot \mathbf{v} = \mathbf{v} \cdot \mathbf{u}.$$
(ii) Inner product commutes with scalar multiple,
$$c\mathbf{u} \cdot \mathbf{v} = (c\mathbf{u}) \cdot \mathbf{v} = \mathbf{u} \cdot (c\mathbf{v}).$$
(iii) Inner product is distributive,
$$\mathbf{u} \cdot (a\mathbf{v} + b\mathbf{w}) = a\mathbf{u} \cdot \mathbf{v} + b\mathbf{u} \cdot \mathbf{w}.$$
(iv) Inner product is positive definite, $\mathbf{u} \cdot \mathbf{u} \ge 0$ with equality if and only if $\mathbf{u} = \mathbf{0}$.
(v) $\|c\mathbf{u}\| = |c|\|\mathbf{u}\|$.

**Definition**
A vector $\mathbf{u}$ in $\mathbb{R}^n$ is a **unit vector** if its norm is 1,
$$\|\mathbf{u}\| = 1$$

**Normalizing a vector**
Let $\mathbf{u}$ be a nonzero vector $\mathbf{u} \neq \mathbf{0}$. By multiplying by the reciprocal of the norm, we get a unit vector,
$$\mathbf{u} \to \frac{\mathbf{u}}{\|\mathbf{u}\|}.$$
This is called **normalizing** $\mathbf{u}$.

**Definition**
The **distance** between two vectors $\mathbf{u}$ and $\mathbf{v}$, denoted as $d(\mathbf{u}, \mathbf{v})$, is defined to be
$$d(\mathbf{u}, \mathbf{v}) = \|\mathbf{u} - \mathbf{v}\|.$$
Define the **angle** $\theta$ between two nonzero vectors, $\mathbf{u}, \mathbf{v} \neq \mathbf{0}$ to be such that
$$\cos(\theta) = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\|\|\mathbf{v}\|}.$$