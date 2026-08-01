Seven NO: Hypothesis Tests

5 steps to hypothesis testing.
Step 1: Set your competing hypothesis: null and alternative.
Step 2: Set the level of significance.
Step 3: Identify the test statistic, its distribution, and the rejection criteria.
Step 4: Compute the observed test statistic value, based on your data.
Step 5: Conclusion.

Definition 1: Type I vs Type II errors
The rejection of $H_0$ when $H_0$ is true is called a Type I error.
The not rejection of $H_0$ when $H_0$ is false is called a Type II error.

Definition 2: Significance vs Power
The probability of making a Type I error is called level of significance, denoted by $\alpha$.
$$\alpha = P(\text{Type I error}) = P(\text{reject } H_0 | H_0 \text{ is true})$$
Let
$$\beta = P(\text{Type II error}) = P(\text{not reject } H_0 | H_0 \text{ is false})$$
Define $1-\beta = P(\text{Reject } H_0 | H_0 \text{ is false})$ to be the power of the test.

Typically set the $\alpha$ level to $\alpha = 0.05$ or $\alpha = 0.01$.

As step 3: To test the hypothesis, we first select a suitable test statistic for the parameter under the hypothesis. The test statistic serves to quantify just how unlikely it is to observe the sample, assuming the null hypothesis is true.

As $\alpha$ is given, a decision rule such that it divides the set of all possible values of the test statistic into two regions, one being the rejection region (critical region), and the other, the acceptance region.

Step 4 & 5: Calculation and Conclusion
+ The value of the test statistic is obtained.
+ Check if it is within our rejection region
    - If it is $\rightarrow$ Reject $H_0$
    - If not $\rightarrow$ fail to Reject $H_0$

Case: known variance (testing a population mean)
* population variance $\sigma^2$ is known and
* where $n \geq 30$ or
* normal distribution
Step 1: $H_0: \mu = \mu_0$ vs $H_1: \mu \neq \mu_0$
Step 2: Set level of significance: $\alpha$ typically be $0.05$
With $\sigma^2$ known and population normal (or $n > 30$)
$$Z = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}} \sim N(0,1)$$