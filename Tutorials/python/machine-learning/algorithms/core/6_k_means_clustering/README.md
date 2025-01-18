# K-Means Clustering:

K-Means Clustering is an Unsupervised Machine Learning algorithm which groups the unlabeled dataset into different clusters. It is an iterative algorithm that divides the unlabeled dataset into k different clusters in such a way that each dataset belongs only one group that has similar properties.

K-means clustering is a technique used to organize data into groups based on their similarity. 

For example online store uses K-Means to group customers based on purchase frequency and spending creating segments like Budget Shoppers, Frequent Buyers and Big Spenders for personalised marketing.

# How K Means clustering works:

The algorithm takes the unlabeled dataset as input, divides the dataset into k-number of clusters, and repeats the process until it does not find the best clusters. The value of k should be predetermined in this algorithm.

The k-means clustering algorithm mainly performs two tasks:

* Determines the best value for K center points or centroids by an iterative process.
* Assigns each data point to its closest k-center. Those data points which are near to the particular k-center, create a cluster.
* Hence each cluster has datapoints with some commonalities, and it is away from other clusters.

The below diagram explains the working of the K-means Clustering Algorithm:

[K-Means Clustering](./images/k-means-clustering.jpg)

# How to choose the k value?
The end result of the algorithm depends on the number of сlusters (k) that’s selected before running the algorithm. However, choosing the right k can be hard, with options varying based on the dataset and the user’s desired clustering resolution.

The smaller the clusters, the more homogeneous data there is in each cluster. Increasing the k value leads to a reduced error rate in the resulting clustering. However, a big k can also lead to more calculation and model complexity. So we need to strike a balance between too many clusters and too few.

The most popular heuristic for this is the elbow method.

Below you can see a graphical representation of the elbow method. We calculate the variance explained by different k values while looking for an “elbow” – a value after which higher k values do not influence the results significantly. This will be the best k value to use.

[Elbow method](./images/elbow_method.jpg)

Most commonly, Within Cluster Sum of Squares (WCSS) is used as the metric for explained variance in the elbow method. It calculates the sum of squares of distance from each centroid to each point in that centroid’s cluster.

We calculate this metric for the range of k values we want to test and look at the results. At the point where WCSS stops dropping significantly with each new cluster added, adding another cluster to the model won’t really increase its explanatory power by a lot. This is the “elbow,” and we can safely pick this number as the k value for the algorithm.