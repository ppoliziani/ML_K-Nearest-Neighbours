# ML_K-Nearest-Neighbours
Implementing the Nearest Neighbours and K Nearest Neighbours algorithm to predict the sign of a pair of coordinates. 

Using matplotlib to graph the training set of coordinates in blue, test coordinate in red and the nearest neighbour in green.

Examples:

![knn1](https://user-images.githubusercontent.com/49439911/135137278-fbc1040f-5d2a-4918-b60e-d5cdc1b64fd3.png)
![knn2](https://user-images.githubusercontent.com/49439911/135137287-6f30e850-a30b-4b2f-ae83-9d1ed4088b4e.png)
![knn3](https://user-images.githubusercontent.com/49439911/135137294-eec15b32-89a3-4f1b-a81f-bc9d672cde6b.png)


Current Limitaion:

So far only implemented KNN where k = 1, just Nearest Neighbour, so when a the test sample and the nearest neighbour lie across the axis it will produce the incorrect prediciton. Adding more comparisons and taking a vote or the average should mitigate this.

![knn4](https://user-images.githubusercontent.com/49439911/135137307-46027ad1-5e3c-4237-b1c1-fbec3d47ee34.png)


