Coordinates Relative to a Basis

### Example

$$ V = \left\{ \begin{pmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{pmatrix} \mid x_1 - 2x_2 + x_3 = 0, x_2 + x_3 - 2x_4 = 0 \right\} \text{, Basis: } S = \left\{ \begin{pmatrix} -3 \\ -1 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 4 \\ 2 \\ 0 \\ 1 \end{pmatrix} \right\} $$

Find the coordinates of $$ \mathbf{v} = \begin{pmatrix} 1 \\ 1 \\ 1 \\ 1 \end{pmatrix} \in V $$ relative to $S$.

$$ \left( \begin{array}{cc|c} -3 & 4 & 1 \\ -1 & 2 & 1 \\ 1 & 0 & 1 \\ 0 & 1 & 1 \end{array} \right) \xrightarrow{RREF} \left( \begin{array}{cc|c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right) \qquad [\mathbf{v}]_S = \begin{pmatrix} 1 \\ 1 \end{pmatrix} $$

---

### Introduction

### Basis for the zero space $\{ \mathbf{0} \}$

Recall that the zero space $\{ \mathbf{0} \}$ is a subspace. Find a basis for $\{ \mathbf{0} \}$.

The basis for the zero space $\{ \mathbf{0} \}$ is the empty set $\{ \}$ or $\emptyset$.
* Firstly, $\text{span}\{\mathbf{0}\} = \{\mathbf{0}\}$ but the set $\{\mathbf{0}\}$ is not linearly independent.
* However, if $S$ is a set that contains any nonzero vector, then $\text{span}(S)$ will be strictly bigger than the zero space, $\{ \mathbf{0} \} \subsetneq \text{span}(S)$.
* The empty set is linearly independent vacuously.
* However, $\text{span}\{\}$ does not make sense.
* The real definition of the span of $S$ is the smallest subspace $V$ such that $S \subseteq V$. That is $V = \text{span}(S)$ if $V \subseteq W$ for all subspaces $W$ containing $S$.

---

### Question

**Definition**

Let $V$ be a subspace of $\mathbb{R}^n$. A set $S = \{ \mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_k \}$ is a **basis** for $V$ if