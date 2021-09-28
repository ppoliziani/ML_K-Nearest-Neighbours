# ML_K-Nearest-Neighbours
Implementing the Nearest Neighbours and K Nearest Neighbours algorithm to predict the sign of a pair of coordinates. 

Using matplotlib to graph the training set of coordinates in blue, test coordinate in red and the nearest neighbour in green.

The prediction will be either:
- 1 for coordinates in the positive space
- -1 for coordinates in the negative space

Examples:

![knn1](https://user-images.githubusercontent.com/49439911/135139327-5b1651f2-17a5-4798-beb1-688ad486e950.png)
![knn2](https://user-images.githubusercontent.com/49439911/135139336-946c4a90-7c39-4083-a283-d0d49989e1d2.png)
![knn3](https://user-images.githubusercontent.com/49439911/135139335-f97f524a-a59c-46fd-a82b-c8c96d55a5d9.png)


Current Limitaion:

So far only implemented KNN where k = 1, just Nearest Neighbour, so when a the test sample and the nearest neighbour lie across the axis it will produce the incorrect prediciton. Adding more comparisons and taking a vote or the average should mitigate this.

![knn4](https://user-images.githubusercontent.com/49439911/135139375-cc03acc4-c6ae-4b20-a1fa-22ee84abd35c.png)

