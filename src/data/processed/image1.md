$s$: sample std deviation $$s = \sqrt{s^2} = \sqrt{\sum_{i=1}^{n} (x_i - \bar{x})^2 \frac{1}{n-1}}$$

Chapter 6
2 types of: Estimations $\rightarrow$ the result: point estimate
+ Point estimation: The rule or formula that doubles this cal $\rightarrow$ point estimator
+ Interval estimation: 2 nums are outputd to form an interval within the parameter is expected to be

Definition 1: Estimator: rule, formula to estimate based on sample
Example: wait time: $x_1 = 6, x_2 = 1, x_3 = 4, x_4 = 9$
We can use $\bar{x} = \text{mean}$ to estimate $\mu$
$\rightarrow \bar{x}$ is the estimator for $\mu$
$\bar{x} = 5$ is the estimate

Definition 2: Unbiased estimator: $\hat{\theta}$ be an estimator for $\theta$
If $E(\hat{\theta}) = \theta \rightarrow$ unbiased estimator of $\theta$
Ex: $x_1 \dots x_n$ random sample with mean $\mu$ and variance $\sigma^2$
$$s^2 = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2 \text{ is an unbiased estimator of } \sigma^2$$
since $E(s^2) = \sigma^2$

Definition 3: $z_\alpha$. Recall $n \to \infty$, $\frac{\bar{x} - \mu}{\sigma / \sqrt{n}} \to$ standard norm distribution
$\rightarrow P(Z > z_\alpha) = \alpha$
Also: $$P(-z_{\alpha/2} \le \frac{\bar{x} - \mu}{\sigma / \sqrt{n}} \le z_{\alpha/2}) = 1 - \alpha$$
This means that: with probability $1 - \alpha$, the error $|\bar{x} - \mu|$ is less than
$$E = z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}} \text{ derive from } |\bar{x} - \mu| \le z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}$$

Definition 4: Maximum Error of Estimate
$$E = z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}} \text{ is called the maximum error of estimate}$$

Determination of sample size
We want to know what the min sample should be
with probability $1 - \alpha$, the error is at most at $E_0$
$$\iff z_{\alpha/2} \frac{\sigma}{\sqrt{n}} \le E_0 \iff n \ge \left( \frac{z_{\alpha/2} \cdot \sigma}{E_0} \right)^2$$

| Population | $\sigma$ | $n$ | Statistic | $E$ | $n$ for desired $E_0$ and $\alpha$ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| I Normal | known | any | $Z = \frac{\bar{x}-\mu}{\sigma/\sqrt{n}}$ | $z_{\alpha/2} \frac{\sigma}{\sqrt{n}}$ | $\left( \frac{z_{\alpha/2} \cdot \sigma}{E_0} \right)^2$ |
| II any | known | large | $Z = \frac{\bar{x}-\mu}{\sigma/\sqrt{n}}$ | $z_{\alpha/2} \frac{\sigma}{\sqrt{n}}$ | $\left( \frac{z_{\alpha/2} \cdot \sigma}{E_0} \right)^2$ |
| III Normal | unknown | small | $T = \frac{\bar{x}-\mu}{s/\sqrt{n}}$ | $t_{(n-1; \alpha/2)} \frac{s}{\sqrt{n}}$ | $\left( \frac{t_{(n-1; \alpha/2)} \cdot s}{E_0} \right)^2$ |
| IV any | unknown | large | $Z = \frac{\bar{x}-\mu}{s/\sqrt{n}}$ | $z_{\alpha/2} \frac{s}{\sqrt{n}}$ | $\left( \frac{z_{\alpha/2} \cdot s}{E_0} \right)^2$ |