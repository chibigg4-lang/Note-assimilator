### Example

Sheldon only patronizes three stalls in the school canteen, the mixed rice, noodle, and mala hotpot stall for lunch everyday. He never buys from same stall two days in a row. If he buys from the mixed rice stall on a certain day, there is a 40% chance he will patronize the noodles stall the next day. If he buys from the noodle stall on a certain day, there is a 50% chance he will eat mala hotpot the next day. If he eats mala hotpot on a certain day, there is a 60% chance he will patronize the mixed rice the next day.

$a_n, b_n, c_n$ probability that Sheldon patronizes the mixed rice, noodles, mala hotpot for lunch after $n$ days.
$x_n = \begin{pmatrix} a_n \\ b_n \\ c_n \end{pmatrix}$, $x_0, x_1 = Px_0, \dots, x_k = Px_{k-1} = P^k x_0$.

$$\begin{pmatrix} 0.6 \\ 0.4 \\ 0 \end{pmatrix} = P \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} \implies P = \begin{pmatrix} 0 & 0.5 & 0.6 \\ 0.4 & 0 & 0.4 \\ 0.6 & 0.5 & 0 \end{pmatrix}$$

***

### Example

By construction, $\mathbf{P} = \begin{pmatrix} 0 & 0.5 & 0.6 \\ 0.4 & 0 & 0.4 \\ 0.6 & 0.5 & 0 \end{pmatrix}$ is a stochastic matrix. The state vector after $n$ days will be $\mathbf{x}_n = \mathbf{P}^n \mathbf{x}_0$.

To compute the powers of $\mathbf{P}$, we may diagonalize $\mathbf{P}$. Performing the algorithm to diagonalization, we obtain
$$\mathbf{P}^k = \begin{pmatrix} 1 & -1 & 1 \\ 0.8 & 0 & -2 \\ 1 & 1 & 1 \end{pmatrix} \begin{pmatrix} 1^k & 0 & 0 \\ 0 & (-0.6)^k & 0 \\ 0 & 0 & (-0.4)^k \end{pmatrix} \begin{pmatrix} 1 & -1 & 1 \\ 0.8 & 0 & -2 \\ 1 & 1 & 1 \end{pmatrix}^{-1}$$

Suppose Sheldon had noodles today. The probability that he patronizes each of the stalls 3 days later is
$$\mathbf{x}_3 = \mathbf{P}^3 \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 1 & -1 & 1 \\ 0.8 & 0 & -2 \\ 1 & 1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 & 0 \\ 0 & (-0.6)^3 & 0 \\ 0 & 0 & (-0.4)^3 \end{pmatrix} \begin{pmatrix} 1 & -1 & 1 \\ 0.8 & 0 & -2 \\ 1 & 1 & 1 \end{pmatrix}^{-1} \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 0.38 \\ 0.24 \\ 0.38 \end{pmatrix}$$

***

### Example

Recall that if $-1 < r < 1$, then $r^k \to 0$ as $k \to \infty$; that is for very big $k$, $r^k$ is approximately 0. Hence, in the long run, Sheldon's state vector is
$$\mathbf{P}^k \mathbf{x}_0 = \mathbf{P}^k \begin{pmatrix} a \\ b \\ c \end{pmatrix} \xrightarrow{k \to \infty} \mathbf{x}_\infty = \begin{pmatrix} 1 & -1 & 1 \\ 0.8 & 0 & -2 \\ 1 & 1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} \begin{pmatrix} 1 & -1 & 1 \\ 0.8 & 0 & -2 \\ 1 & 1 & 1 \end{pmatrix}^{-1} \begin{pmatrix} a \\ b \\ c \end{pmatrix}$$
$$= \frac{1}{14} \begin{pmatrix} 5 & 5 & 5 \\ 4 & 4 & 4 \\ 5 & 5 & 5 \end{pmatrix} \begin{pmatrix} a \\ b \\ c \end{pmatrix} = \frac{1}{14} \begin{pmatrix} 5(a+b+c) \\ 4(a+b+c) \\ 5(a+b+c) \end{pmatrix} = \frac{1}{14} \begin{pmatrix} 5 \\ 4 \\ 5 \end{pmatrix},$$

where the last equality follows from the fact that $\mathbf{x}_0$ is a probability vector. That is, he will most probably patronize the mixed rice or mala hotpot stall with equal probability $\frac{5}{14}$ in the long run.

Observe that $\frac{1}{14} \begin{pmatrix} 5 \\ 4 \\ 5 \end{pmatrix}$ is an probability state vector and an eigenvector associated to eigenvalue 1. Meaning, 

regardless of the choice to the starting state vector $\begin{pmatrix} a \\ b \\ c \end{pmatrix}$, in the long run, the resultant state vector is the same!