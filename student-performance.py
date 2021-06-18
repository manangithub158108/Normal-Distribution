# importing all the modules
import csv, statistics;
import plotly.figure_factory as ff;
import plotly.graph_objects as go;
import pandas as pd;

# opening the file and storing the writing score in score array.
with open('data.csv') as doc:
    reader = csv.reader(doc);
    file_data = list(reader);

file_data.pop(0);

score = [];

for i in range(0, len(file_data)):
    writing_score = int(file_data[i][7]);
    score.append(writing_score);


# finding mean, median, mode, stddev of the data
mean = statistics.mean(score);
median = statistics.median(score);
mode = statistics.mode(score);
stddev = statistics.stdev(score);

print('Mean of the data => ' + str(mean));
print('Median of the data => ' + str(median));
print('Mode of the data => ' + str(mode));
print('Standard deviation of the data => ' + str(stddev));

# creating the first standard deviation
first_stddev_start, first_stddev_end = mean - stddev, mean + stddev

# creating the second standard deviation
second_stddev_start, second_stddev_end = mean - 2*stddev, mean + 2*stddev

# creating the third standard deviation
third_stddev_start, third_stddev_end = mean - 3*stddev, mean + 3*stddev

# getting all the data information of first deviation
list_of_data_of_first_deviation = [
    result
    for result in score
        if result > first_stddev_start and result < first_stddev_end
]

# getting all the data information of second deviation
list_of_data_of_second_deviation = [
    result
    for result in score
        if result > second_stddev_start and result < second_stddev_end
]

# getting all the data information of third deviation
list_of_data_of_third_deviation = [
    result
    for result in score
        if result > third_stddev_start and result < third_stddev_end
]

# finding the percentages 
print('{}% Off the first standard deviation'.format(len(list_of_data_of_first_deviation) * 100 / len(score)));
print('{}% Off the second standard deviation'.format(len(list_of_data_of_second_deviation) * 100 / len(score)));
print('{}% Off the third standard deviation'.format(len(list_of_data_of_third_deviation) * 100 / len(score)));

# plotting histograph 
fig = ff.create_distplot([score], ['Score'], show_hist = False);
fig.add_trace(go.Scatter(
    x = [mean, mean],
    y = [0, 0.17],
    mode = 'lines',
    name = 'mean'
));

# 1st
fig.add_trace(go.Scatter(
    x = [first_stddev_start, first_stddev_start],
    y = [0, 0.17],
    name = 'First Standard deviation',
    mode = 'lines'
));
fig.add_trace(go.Scatter(
    x = [first_stddev_end, first_stddev_end],
    y = [0, 0.17],
    name = 'First Standard deviation',
    mode = 'lines'
));

# 2nd
fig.add_trace(go.Scatter(
    x = [second_stddev_start, second_stddev_start],
    y = [0, 0.17],
    name = 'Second Standard deviation',
    mode = 'lines'
));
fig.add_trace(go.Scatter(
    x = [second_stddev_end, second_stddev_end],
    y = [0, 0.17],
    name = 'Second Standard deviation',
    mode = 'lines'
));

# 3rd 
fig.add_trace(go.Scatter(
    x = [third_stddev_start, third_stddev_start],
    y = [0, 0.17],
    name = 'Third Standard deviation',
    mode = 'lines'
));
fig.add_trace(go.Scatter(
    x = [third_stddev_end, third_stddev_end],
    y = [0, 0.17],
    name = 'Third Standard deviation',
    mode = 'lines'
));

fig.show();
