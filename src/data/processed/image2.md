Definition 5 Confidence Interval $\overline{X} \pm E$
Interval estimator: rule/formula for calculating an interval $(a,b)$ which you are fairly certain the parameter of interest lies in.
Degree of confidence / confidence level $(1-\alpha)$
$$P(a < \mu < b) = 1-\alpha$$
$(a,b)$ is called the $(1-\alpha)$ confidence interval

| Population | $\sigma$ | $n$ | Confidence interval |
| :--- | :--- | :--- | :--- |
| Normal | known | any | $\overline{x} \pm Z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}$ |
| any | known | large | $\overline{x} \pm Z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}$ |
| Normal | unknown | small | $\overline{x} \pm t_{(n-1; \alpha/2)} \cdot \frac{s}{\sqrt{n}}$ |
| any | unknown | large | $\overline{x} \pm Z_{\alpha/2} \cdot \frac{s}{\sqrt{n}}$ |

Consider $X_1, ..., X_{n_1}$ and $Y_1, ..., Y_{n_2}$, $\overline{X}, \overline{Y}$ independent, $\sigma_1, \sigma_2$ are known
$\sigma_1^2 \neq \sigma_2^2$
$E(\overline{X})=\mu_1$, $E(\overline{Y})=\mu_2$, $V(\overline{X})=\frac{\sigma_1^2}{n_1}$, $V(\overline{Y})=\frac{\sigma_2^2}{n_2}$
$\rightarrow E(\overline{X}-\overline{Y})=\mu_1-\mu_2$, $V(\overline{X}-\overline{Y})=\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}$
and if populations are normal / $n_1, n_2 \ge 30$
we have:
$$Z = \frac{(\overline{X}-\overline{Y})-(\mu_1-\mu_2)}{\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}} \approx N(0,1) (\text{开})$$
Confidence intervals for $\mu_1-\mu_2$ & $\delta = \mu_1 - \mu_2$ with confidence $100(1-\alpha)\%$
If $\sigma_1^2$ and $\sigma_2^2$ are known, by $(\text{开})$
$$P(|Z| < Z_{\alpha/2}) = 1-\alpha$$
$$\iff P\left((\overline{X}-\overline{Y}) - Z_{\alpha/2}\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}} < \mu_1-\mu_2 < (\overline{X}-\overline{Y}) + Z_{\alpha/2}\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}\right) = 1-\alpha$$
$$(a,b) = (\overline{X}-\overline{Y}) \pm Z_{\alpha/2} \sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}$$
Practical: Same conditions:
$100(1-\alpha)\%$ confidence interval for $\mu_1-\mu_2$ is
$$(\overline{X}-\overline{Y}) \pm Z_{\alpha/2} \sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}$$