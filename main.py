import random
import numpy as np
from matplotlib import pyplot as plt
import math


def plot(graph_coords, coordinates, index, test_sample):
    # plotting training coordinates in blue
    # test coordinate in red
    # predicted closest coordinate in green

    # need to show axis
    x, y = graph_coords.T
    plt.scatter(x, y, color="blue")
    plt.scatter(test_sample[0], test_sample[1], color="red")
    plt.xlabel("x")
    plt.ylabel("y")
    closest_x = coordinates[index][0]
    closest_y = coordinates[index][1]
    plt.scatter(closest_x, closest_y, color="green")
    plt.show()


# k nearest neighbour prediction method
def k_nearest_neighbours():
    pass

# single nearest neighbour prediction method
def nearest_neighbours(coordinates, test_sample):

    # calculate distance from test_data to all coordinates
    print("\n= Using NN algorithm =\n")

    distances = np.zeros([10, 1])
    print(distances)

    graph_coords = np.delete(coordinates, -1, 1)

    for x in range(0, 10):
        distance = math.sqrt((graph_coords[x][0] - test_sample[0])**2 + (graph_coords[x][1] - test_sample[1])**2)
        distances[x] = distance
        print(distance)

    # find index of shortest distance in distances then return label of same index in coordinates.
    # some sort of search
    print("MIN: " + str(np.amin(distances)))
    index = np.where(distances == np.amin(distances))
    index = index[0][0]

    prediction = coordinates[index][2]
    print(coordinates[index])
    print("\n= NN PREDICTION =\n")
    print(prediction)

    plot(graph_coords, coordinates, index, test_sample)

# generate random coordinate training pairs and single coordinate test pair
# coordinates values in range (-3, 10)
def generate_samples():

    coordinates = np.zeros([10, 3])

    for x in range(10):
        x_val = random.randint(-3, 10)
        y_val = random.randint(-3, 10)

        if x_val <= 0 or y_val <= 0:
            label = -1
        else:
            label = 1

        coordinate = [x_val, y_val, label]

        coordinates[x] = coordinate

    print(coordinates)

    test_sample = [random.randint(-3, 10), random.randint(-3, 10), 0]
    print("Test: " + str(test_sample))

    nearest_neighbours(coordinates, test_sample)


def main():
    print("\n= ML Batch supervised learning using nn algorithm via transduction =\n")
    generate_samples()

main()