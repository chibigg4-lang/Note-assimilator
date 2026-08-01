Example

Let $\mathbf{A} = \begin{pmatrix} 5 & -1 & -1 \\ -1 & 5 & -1 \\ -1 & -1 & 5 \end{pmatrix}$. We have found a basis for the eigenspaces.

$$E_3 = \text{span} \left\{ \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} \right\}, \quad E_6 = \text{span} \left\{ \begin{pmatrix} -1 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} -1 \\ 0 \\ 1 \end{pmatrix} \right\}$$

Perform Gram-Schmidt process to the vectors in the basis of $E_6$.

$$\mathbf{v}_1 = \begin{pmatrix} -1 \\ 1 \\ 0 \end{pmatrix}, \quad \mathbf{v}_2 = \begin{pmatrix} -1 \\ 0 \\ 1 \end{pmatrix} - \frac{1}{2} \begin{pmatrix} -1 \\ 1 \\ 0 \end{pmatrix} = \frac{1}{2} \begin{pmatrix} -1 \\ -1 \\ 2 \end{pmatrix}$$

After normalizing the vectors, put them as columns of the matrix $\mathbf{P}$.

$$\mathbf{A} = \begin{pmatrix} 1/\sqrt{3} & -1/\sqrt{2} & -1/\sqrt{6} \\ 1/\sqrt{3} & 1/\sqrt{2} & -1/\sqrt{6} \\ 1/\sqrt{3} & 0 & 2/\sqrt{6} \end{pmatrix} \begin{pmatrix} 3 & 0 & 0 \\ 0 & 6 & 0 \\ 0 & 0 & 6 \end{pmatrix} \begin{pmatrix} 1/\sqrt{3} & 1/\sqrt{3} & 1/\sqrt{3} \\ -1/\sqrt{2} & 1/\sqrt{2} & 0 \\ -1/\sqrt{6} & -1/\sqrt{6} & 2/\sqrt{6} \end{pmatrix}$$

# Markov Chain.

### Markov Chain

Definition
(i) A vector $\mathbf{v} = (v_i)_n$ with nonnegative coordinates that add up to 1, $\sum_{i=1}^n v_i = 1$, is called a *probability vector*.

(ii) A *stochastic* matrix is a square matrix whose columns are probability vectors.

(iii) A *Markov chain* is a sequence of probability vectors $\mathbf{x}_0, \mathbf{x}_1, ..., \mathbf{x}_k, ...$, together with a stochastic matrix $\mathbf{P}$ such that
$$\mathbf{x}_1 = \mathbf{P}\mathbf{x}_0, \quad \mathbf{x}_2 = \mathbf{P}\mathbf{x}_1, \quad ... \quad, \mathbf{x}_k = \mathbf{P}\mathbf{x}_{k-1}, ...$$

When a Markov chain of vectors in $\mathbb{R}^n$ describes a system or a sequence of experiments, the entries in $\mathbf{x}_k$ list, respectively, the probabilities that the system is in each of $n$ possible states, or the probabilities that the outcome of the experiment is one of $n$ possible outcomes. For this reason, $\mathbf{x}_k$ is often called a *state vector*.