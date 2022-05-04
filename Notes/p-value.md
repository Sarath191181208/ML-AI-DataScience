## P-value

The probability that a particular statistical measure, such as the mean or the standard deviation, of an assumed probability distribution will be greater than of equal to (or less than or equal to in some instances) observed results.

Types of p-value tests:

| Test Name                                            | Kind of data                                                         |
| ---------------------------------------------------- | -------------------------------------------------------------------- |
| [One sample proportion](#one-sample-proportion-test) | Single Categorical Variable                                          |
| [ $chi^2$ ](#chi2-test)                              | Two Categorical features                                             |
| [T test](#t-test)                                    | Single Continious Value with or without a binary categorical feature |
| [Corelation](#corelation)                            | Two continuous features                                              |
| [Anova Test](#anova-test)                            | Categorical Feature, Continuous feature                              |

| Var 1                        | Var 2                | Test Name                  |
| ---------------------------- | -------------------- | -------------------------- |
| Numerical                    | Numerical            | Pearson's corelation       |
| Categorical(ordianal)        | Numerical            | Spearman's rank corelation |
| Categorical(nominal)         | Categorical(nominal) | $Chi^2$                    |
| Categorical(nominal/ordinal) | Numerical            | Anova                      |

### One sample proportion test:

- Single Categorical Variable
- **When would you use a proportion test?**
  - Use the One Proportion Test to test whether the probability of occurrence of an event is different from a standard or historical value. This test is based on the binomial distribution with parameters n (number of trials) and p (probability of the event).

### $chi^2$ test:

- Two categorical variables
- **When would you use $chi^2$ test?**
  - To distinguish between the two features are actually realted or just due to chance alone.

### T test:

- Single continious value with or without a binary categorical feature
- **When would you use T test?**
  - When mean value for data is intended to be compared to a fixed and defined number.

### Corelation:

- Two continious features
- **When would you use Corelation?**
  - Use correlation for a quick and simple summary of the direction and strength of the relationship between two or more numeric variables.

### Anova Test:

- Categorical Feature, Continuous feature
- **When ?**
  1. Statistical differences among the means of two or more groups.
  1. Statistical differences among the means of two or more interventions.
  1. Statistical differences among the means of two or more change scores.
