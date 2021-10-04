import random
import numpy as np
from matplotlib import pyplot as plt
import math
from scipy import stats


def knn_plot(graph_coords, coordinates, indexes, test_sample, prediction, k, nn_prediciton):

    # plotting training coordinates in blue
    # test coordinate in red
    # nearest neighbour coordinate in green

    fig, ax = plt.subplots()
    x, y = graph_coords.T
    plt.scatter(x, y, color="blue")
    test_x = test_sample[0]
    test_y = test_sample[1]
    plt.scatter(test_x, test_y, color="red")
    plt.annotate("KNN: " + "(k = " + str(k) + ") " + str(prediction) + "\n", (test_x, test_y), fontsize="20")
    plt.annotate("NN: " + str(nn_prediciton), (test_x, test_y), fontsize="20")

    # adds and labels the axis
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    plt.xlabel("x")
    plt.ylabel("y")

    # gets the nearest neighbour and highlights the point in green
    for index in indexes:
        nearest_x = coordinates[int(index)][0]
        nearest_y = coordinates[int(index)][1]
        plt.scatter(nearest_x, nearest_y, color="green")

        # drawing line between the nearest neighbours and the test sample
        x_values = [nearest_x, test_x]
        y_values = [nearest_y, test_y]
        plt.plot(x_values, y_values)

    # adding bounds to the axis
    plt.xticks(np.arange(-15, 51, 2.0))
    plt.yticks(np.arange(-15, 51, 3.0))

    plt.show()


# using p-values ranks the "strangeness" of the sample to the dataset to inform its prediction
# 1.) using nearest neighbours calculate distance between same and difference class and divide them = conformity scores
# 2.) then rank the conformity scores using "1334" rank, if 2 values of same rank assign the higher rank to both
# (Modified Competition Ranking - https://en.wikipedia.org/wiki/Ranking) take the higher rank as pessimistic

def conformal_prediction(coordinates, test_sample, sample_size):
    pass


# k nearest neighbour prediction method
def k_nearest_neighbours(coordinates, test_sample, sample_size):

    k = int(input("Enter a value for k: "))

    distances = np.zeros([sample_size])

    graph_coords = np.delete(coordinates, -1, 1)

    # calculate distance from test_sample to all coordinates
    for x in range(0, sample_size):
        distance = math.sqrt((graph_coords[x][0] - test_sample[0])**2 + (graph_coords[x][1] - test_sample[1])**2)
        distances[x] = distance

    sorted_distances = np.sort(distances)

    # returns k smallest distances, k nearest neighbours distances, need to get the index and the label
    smallest_k = sorted_distances[:k]
    # print(smallest_k)

    indexes = np.zeros([k])

    x = 0
    for val in smallest_k:
        index = np.where(distances == val)
        indexes[x] = index[0][0]
        x += 1

    # if 2 points are the same distance away it will not recognise them as different points and just select one
    i = 0
    nearest_labels = np.zeros(k)
    for index in indexes:
        if i == k:
            break
        # print(coordinates[int(index)][2])
        nearest_labels[i] = coordinates[int(index)][2]
        i += 1

    # gets the label of the single nearest neighbour which is the NN algorithm
    nn_prediction = nearest_labels[0]

    prediction = int(stats.mode(nearest_labels)[0][0])

    knn_plot(graph_coords, coordinates, indexes, test_sample, prediction, k, nn_prediction)


# generate random coordinate training pairs and single coordinate test pair
def generate_samples():

    # initialises a numpy array with 10 coordinate paris full of 0s
    # last column is used to store the label saying whether it is positive (1) or negative (-1) (below or equal to 0)
    # e.g. coordinates [6, -2] in the array would be [6, -2, -1], where the -1 indicates it is negative
    sample_size = 100
    coordinates = np.zeros([sample_size, 3])

    # creates 10 random coordinates and fills in the numpy array, labelling them if they are negative or positive
    lower_bound = -15
    upper_bound = 50
    for x in range(sample_size):
        x_val = random.randint(lower_bound, upper_bound)
        y_val = random.randint(lower_bound, upper_bound)

        if x_val <= 0 or y_val <= 0:
            label = -1
        else:
            label = 1

        coordinate = [x_val, y_val, label]
        coordinates[x] = coordinate

    # print(coordinates)

    test_sample = [random.randint(lower_bound, upper_bound), random.randint(lower_bound, upper_bound), 0]
    # print("Test: " + str(test_sample))

    # nearest_neighbours(coordinates, test_sample)
    k_nearest_neighbours(coordinates, test_sample, sample_size)
    conformal_prediction(coordinates, test_sample, sample_size)


def main():
    print("\n= ML Batch supervised learning (binary classification) using KNN algorithm =\n")
    generate_samples()

main()