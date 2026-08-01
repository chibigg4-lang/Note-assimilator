The $n \times n$ identity matrix $\mathbf{I}_n$ is in reduced row-echelon form and does not have any zero rows. Hence, its columns span $\mathbb{R}^n$.

Indeed, let $\mathbf{e}_i$ denote the $i$-th column of $\mathbf{I}_n$ for $i=1, \dots, n$. Then for any vector $\mathbf{w}$,

$$ \mathbf{w} = \begin{pmatrix} w_1 \\ w_2 \\ \vdots \\ w_n \end{pmatrix} = w_1 \begin{pmatrix} 1 \\ 0 \\ \vdots \\ 0 \end{pmatrix} + w_2 \begin{pmatrix} 0 \\ 1 \\ \vdots \\ 0 \end{pmatrix} + \dots + w_n \begin{pmatrix} 0 \\ 0 \\ \vdots \\ 1 \end{pmatrix} $$

Hence, $\text{span}\{\mathbf{e}_1, \mathbf{e}_2, \dots, \mathbf{e}_n\} = \mathbb{R}^n$. This set is called the *standard basis* of $\mathbb{R}^n$.

# Properties of Linear Spans:

**Theorem** (Properties of linear span)
Let $S = \{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_k\}$ be a finite set of vector. The span of $S$, $span(S)$ has the following properties.

(i) The span of $S$ contains the origin,
$$ \mathbf{0} \in span(S). $$

(ii) The span of $S$ is closed under vector addition, for any $\mathbf{u}, \mathbf{v} \in span(S)$,
$$ \mathbf{u} + \mathbf{v} \in span(S). $$

(iii) The span $S$ is closed under scalar multiplication, for any $\mathbf{u} \in span(S)$ and real number $\alpha \in \mathbb{R}$,
$$ \alpha \mathbf{u} \in span(S). $$

Properties (ii) and (iii) can be combined together into one property (ii'):
The span is closed under linear combinations, that is, if $\mathbf{u}, \mathbf{v}$ are vectors in $span(S)$ and $\alpha, \beta$ are any scalars, then the linear combination $\alpha\mathbf{u} + \beta\mathbf{v}$ is a vector in $span(S)$.

**Theorem** (Linear span is closed under linear combinations)
Let $S = \{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_k\}$ be a set of vectors in $\mathbb{R}^n$. For any vectors $\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_m$ in $span(S)$, the span of $\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_m$ is a subset of $span(S)$,
$$ span\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_m\} \subseteq span(S). $$

**Algorithm to check for Set Relations between Spans**
Now suppose we are given 2 sets of vectors $T = \{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_m\}$ and $S = \{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_k\}$.

I. By the corollary, if $\mathbf{v}_i \in span(S)$ for $i = 1, \dots, m$, we can conclude that $span(T) \subseteq span(S)$.
II. Recall that to check if $\mathbf{v}_i \in span(S)$, we check that the system $(\mathbf{u}_1 \quad \mathbf{u}_2 \quad \dots \quad \mathbf{u}_k \mid \mathbf{v}_i)$ is consistent for all $i = 1, \dots, m$.
III. There are in total $m$ such linear systems to check. However, since they have the same coefficient matrix, we may combine and check them together, that is, check that
$$ \left( \begin{array}{ccc|c|ccc} \mathbf{u}_1 & \mathbf{u}_2 & \dots & \mathbf{u}_k & \mathbf{v}_1 & \mathbf{v}_2 & \dots & \mathbf{v}_m \end{array} \right) $$
is consistent.

**Theorem** (Algorithm to check for set relations between spans)
Let $S = \{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_k\}$ and $T = \{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_m\}$ be sets of vectors in $\mathbb{R}^n$. Then $span(T) \subseteq span(S)$ if and only if $\left( \begin{array}{ccc|c|ccc} \mathbf{u}_1 & \mathbf{u}_2 & \dots & \mathbf{u}_k & \mathbf{v}_1 & \mathbf{v}_2 & \dots & \mathbf{v}_m \end{array} \right)$ is consistent.