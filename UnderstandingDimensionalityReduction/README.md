## Linear Dimensionality Reduction Methods

### Principal Component Analysis

Steps:

1. Standardize the data
2. Take mean and center it around origin
3. Find the best fit line (eigenvector) that explains the most variance
4. Analyze the variance explained by each eigenvector (scree plot)
5. Choose the number of eigenvectors to keep
6. Project the data onto the new subspace

Watch this video for a better understanding: [Stack Quest's Video On PCA](https://www.youtube.com/watch?v=FgakZw6K1QQ)

### Linear Discriminant Analysis
Steps:
1. Standardize the data
2. Similar to PCA, we aren't going to center the data around the origin. 
3. We are trying to maximize the distance between the means of the classes and minimize the variance within the classes (spread).

Watch this video for a better understanding: [Stack Quest's Video On LDA](https://www.youtube.com/watch?v=azXCzI57Yfc)