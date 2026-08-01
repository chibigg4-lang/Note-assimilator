The classification setting
The most common approach for quantifying the accuracy of our estimate $\hat{f}$ is the training error rate, the proportion of mistakes that are made if we apply our estimate $\hat{f}$ to our training observations:
$$\frac{1}{n} \sum_{i=1}^{n} I(y_i \neq \hat{y}_i) \rightarrow \text{Training error rate } (2.8)$$
$\hat{y}_i$ is the predicted class label for the $i$th observation using $\hat{f}$.
dicator variable $\begin{cases} I(y_i \neq \hat{y}_i) = 1 \text{ if } y_i \neq \hat{y}_i \\ I(y_i \neq \hat{y}_i) = 0 \text{ if } y_i = \hat{y}_i \text{ (means } i\text{th observation was classified correctly)} \end{cases}$
$\hookrightarrow$ we counting wrong prediction by indicator

The test error rate associated with a set of test observations of the form $(x_0, y_0)$ is given by $\text{Ave}(I(y_0 \neq \hat{y}_0)) \text{ } (2.9)$
$+$ $\hat{y}_0$ is the predicted class label result from applying the classifier to the test observation with predictor $x_0$.
$+$ good classifier is one for which test error rate is smallest.

The Bayes Classifier
test error rate is minimized, on average, by classifier that assigns each obs to the most likely class, given its predictor values (assign test obs with predictor vector $x_0$ to class $j$ that):
$$P(Y=j | X=x_0) \text{ is largest } (2.10)$$
The Bayes classifier produces the lowest possible test error rate, called the Bayes error rate
$$\frac{1}{n} \sum_{i=1}^{n} 1 - \max_{j} P(Y=j | X=x_i) = 1 - E(\max_{j} P(Y=j | X)) \text{ } (2.11)$$
$\hookrightarrow$ Over all possible values of $X$

K-Nearest neighbors
Given $K \in \mathbb{N}^{+}$ and test observation $x_0$, the KNN classifier first identifies the $K$ points in the training data that are closest to $x_0$, represented by $\mathcal{N}_0$. It then estimates the conditional probability for class $j$ as the fraction of points in $\mathcal{N}_0$ whose response values equal $j$:
$$P(Y=j | X=x_0) = \frac{1}{K} \sum_{i \in \mathcal{N}_0} I(y_i = j) \text{ } (2.12)$$
Finally, KNN assign the test observation $x_0$ to the class with largest $P$ from (2.12)

Conceptual Exercises (2.4)
1) a) A flexible method since $n$ large we can learn $\hat{f}$ well without overfitting. Also, the degree of freedom is small input space is low-dimension so easier to estimate.
b) inflexible method since $p \gg$ and $n \ll$, therefore can be easily overfitted and may capture noise.
c) flexible method as inflexible method such as linear regression is too restricted + high bias $\rightarrow$ (cannot capture the curve)
d) inflexible method. since $Var(\epsilon)$ is high $\rightarrow$ lots of random noises, too flexible method may follow that noise.