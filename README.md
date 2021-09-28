# ML_K-Nearest-Neighbours
Implementing the Nearest Neighbours and K Nearest Neighbours algorithm to predict the sign of a pair of coordinates. 

Using matplotlib to graph the training set of coordinates in blue, test coordinate in red and the nearest neighbour in green.

Examples:
![knn1](https://user-images.githubusercontent.com/49439911/135135731-f72d7a23-f361-44b1-a1ad-9b4b77e00164.png)
![knn2](https://user-images.githubusercontent.com/49439911/135135787-7095c849-6c7f-48f8-93e3-d04b117647ef.png)
![knn3](https://user-images.githubusercontent.com/49439911/135135793-eb48e7f7-c052-453e-9055-0cf577b99713.png)

Current Limitaion:

So far only implemented KNN where k = 1, just Nearest Neighbour, so when a the test sample and the nearest neighbour lie across the axis it will produce the incorrect prediciton. Adding more comparisons and taking a vote or the average should mitigate this.

![image](https://user-images.githubusercontent.com/49439911/135136060-eddad1c1-f89d-4d0f-8ccf-424b69be2ee3.png)

