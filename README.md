# ML_K-Nearest-Neighbours
Implementing the K Nearest Neighbours algorithm to predict the sign of a pair of coordinates. 

Using matplotlib to graph the training set of coordinates in blue, test coordinate in red and the nearest neighbour in green.

The prediction will be either:
- 1 for coordinates in the positive space
- -1 for coordinates in the negative space

Final implementation examples (k = 3):

![knn5](https://user-images.githubusercontent.com/49439911/135255465-d457a668-e70c-49c5-8a9b-c14a4d5c7b00.png)
![knn6](https://user-images.githubusercontent.com/49439911/135255471-e11608cd-8bc7-4624-863b-427266a588c8.png)
![knn7](https://user-images.githubusercontent.com/49439911/135255479-d6b338d9-9106-4459-bf5f-db83bf909d46.png)

Examples (k = 1):

![knn1](https://user-images.githubusercontent.com/49439911/135139327-5b1651f2-17a5-4798-beb1-688ad486e950.png)
![knn2](https://user-images.githubusercontent.com/49439911/135139336-946c4a90-7c39-4083-a283-d0d49989e1d2.png)
![knn3](https://user-images.githubusercontent.com/49439911/135139335-f97f524a-a59c-46fd-a82b-c8c96d55a5d9.png)

When k = 1, a situation where the test sample and the nearest neighbour lie across the axis it will produce the incorrect prediciton. Adding more comparisons and taking a vote or the average should solve this.

![knn4](https://user-images.githubusercontent.com/49439911/135139375-cc03acc4-c6ae-4b20-a1fa-22ee84abd35c.png)

Current Limitaions:

Although adding more points to compare to should fix the cross axis wrong sign issue, it still is not fully solved as seen below. Even though the test sample (red dot) is in the negative 2 of the 3 nearest points are in the positive and so knn gave it a positive sign.

![knn8](https://user-images.githubusercontent.com/49439911/135255547-646214bb-0e76-4bfa-a04c-8a904b652067.png)

Increasing the training set shold help reduce errors like these. 

![knn9](https://user-images.githubusercontent.com/49439911/135256503-c0846c39-48e9-4f80-8213-783fa132df16.png)


