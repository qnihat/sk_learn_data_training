import csv
import os
from numpy import loadtxt


def run_once():
    if not os.path.exists('angles.csv'):
        print('csv file created')
        #num_coords = len(results.pose_landmarks.landmark)
        landmarks = []
        for val in range(1, 9):
            landmarks += ['input{}'.format(val)]
        landmarks+=['class']
        with open('angles.csv', mode='w', newline='') as f:
            csv_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(landmarks)

run_once()

def add_angles(row):
    with open('angles.csv', mode='a', newline='') as f:
        csv_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(row)

dataset = loadtxt('pima-indians-diabetes.csv', delimiter=',')
X = dataset[:,0:8]
y = dataset[:,8]

for i in range(len(X)):
    row=[]
    #row=X[i]
    for ele in X[i]:
        row.append(ele)
    row.append(y[i])
    add_angles(row)