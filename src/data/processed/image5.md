DATE: .......................................

# 3. Linear Regression
## 3.1 Simple linear regression
$$y \approx \beta_0 + \beta_1 X \quad \text{intercept and slope}$$
predict future sales:
$$\hat{y} = \hat{\beta}_0 + \hat{\beta}_1 X$$

## 3.1.1
Most common approach is minimizing the least squares criterion.
Let $\hat{y}_i = \hat{\beta}_0 + \hat{\beta}_1 x_i$ be the prediction for $Y$ based on the ith value of $X$.
$e_i = y_i - \hat{y}_i$ (difference between ith observe response val and ith response val predicted by our model)
$$RSS = \sum_{i=1}^{n} e_i^2 \quad \text{(residual sum of squares)}$$
By calculus:
$$\hat{\beta}_1 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^{n} (x_i - \bar{x})^2}, \hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x}$$

## 3.1.2: Assessing the Accuracy of the Coefficients Estimates
Recall that true relationship is: $Y = f(X) + \epsilon$
Linear regression assumption: $Y = \beta_0 + \beta_1 X + \epsilon$
The error term is a catch-all for what we miss with this simple model:
the true relationship is probably not linear, there may be other variables that
cause variation in $Y$, and there may be measurement error. Usually assume that
error term is independent of $X$.

Natural question: how accurate is sample mean $\hat{\mu}$ as an estimate of $\mu$
$\to$ Compute standard error of $\hat{\mu}$
$$Var(\hat{\mu}) = SE(\hat{\mu})^2 = \frac{\sigma^2}{n}$$
$$SE(\hat{\beta}_0)^2 = \sigma^2 \left[ \frac{1}{n} + \frac{\bar{x}^2}{\sum_{i=1}^{n} (x_i - \bar{x})^2} \right], SE(\hat{\beta}_1)^2 = \frac{\sigma^2}{\sum_{i=1}^{n} (x_i - \bar{x})^2}$$
$\sigma^2 = Var(\epsilon)$
In general, $\sigma^2$ is not known, but can be estimated from the data.
Estimate of $\sigma$ is known as residual standard error
$$RSE = \sqrt{\frac{RSS}{n-2}}$$
When $\sigma^2$ is estimated from the data, we should write $\widehat{SE}(\hat{\beta}_1)$ to indicate an
estimation has been made, but we drop $\wedge$ for simplicity of notation.

## Confidence Intervals (ST2334)
for $\beta_1$: $\hat{\beta}_1 \pm z_{0.025} SE(\hat{\beta}_1) \quad (z_{0.025} = 1.96)$
for $\beta_0$: $\hat{\beta}_0 \pm z_{0.025} SE(\hat{\beta}_0)$