import csv
import pandas as pd
import statistics

df=pd.read_csv('height-weight.csv')
height_list=df["Height(Inches)"].tolist()
weight_list=df["Weight(Pounds)"].tolist()

#mean for height and weight
height_mean=statistics.mean(height_list)
weight_mean=statistics.mean(weight_list)

#median for height and weight
height_median=statistics.median(height_list)
weight_median=statistics.median(weight_list)

#mode for height and weight
height_mode=statistics.mode(height_list)
weight_mode=statistics.mode(weight_list)

#printing mean,median and mode to validate
print("Mean,Median and Mode of the height is {},{} and{} respectively".format(height_mean,height_median,height_mode))
print("Mean,Median and Mode for the Weight is {},{} and {} respectively".format(weight_mean,weight_median,weight_mode))

#standard deviation for height and weight
height_std=statistics.stdev(height_list)
weight_std=statistics.stdev(weight_list)
print("Standard Deviation for Height is ->" +str(height_std))
print("Standard Deviation for Weight is -> "+str(weight_std))

#1,2 and 3 standard deviation for height
height_first_stdev_start,height_first_stdev_end=height_mean-height_std,height_mean+height_std

height_second_stdev_start,height_second_stdev_end=height_mean-(2*height_std),height_mean+(2*height_std)

height_third_stdev_start,height_third_stdev_end=height_mean-(3*height_std),height_mean+(3*height_std)

#1,2 and 3 standard deviation for weight
weight_first_stdev_start,weight_first_stdev_end=weight_mean-weight_std,weight_mean+weight_std

weight_second_stdev_start,weight_second_stdev_end=weight_mean-(2*weight_std),weight_mean+(2*weight_std)

weight_third_stdev_start,weight_third_stdev_end=weight_mean-(3*weight_std),weight_mean+(3*weight_std)

#percentage of data with 1,2 and 3 of standard deviation of data
height_within_first_standarddeviation=[result for result in height_list if result>height_first_stdev_start and height_first_stdev_end]
height_within_second_standarddeviation=[result for result in height_list if result>height_second_stdev_start and height_second_stdev_end]
height_within_third_standarddeviation=[result for result in height_list if result>height_third_stdev_start and height_third_stdev_end]

#percentage of data with 1,2 and 3 of standard deviation of data
weight_within_first_standarddeviation=[result for result in weight_list if result>weight_first_stdev_start and weight_first_stdev_end]
weight_within_second_standarddeviation=[result for result in weight_list if result>weight_second_stdev_start and weight_second_stdev_end]
weight_within_third_standarddeviation=[result for result in weight_list if result>weight_third_stdev_start and weight_third_stdev_end]

#printing data for height (standard deviation)
print("{}% of data for height lies within first standard deviation ".format(len(height_within_first_standarddeviation)*100.0/len(height_list)))
print("{}% of data for height lies within second standard deviation ".format(len(height_within_second_standarddeviation)*100.0/len(height_list)))
print("{}% of data for height lies within first third deviation ".format(len(height_within_third_standarddeviation)*100.0/len(height_list)))

#printing data for weight (standard deviation)
print("{}% of data for weight lies within first standard deviation ".format(len(weight_within_first_standarddeviation)*100.0/len(weight_list)))
print("{}% of data for weight lies within second standard deviation ".format(len(weight_within_second_standarddeviation)*100.0/len(weight_list)))
print("{}% of data for weight lies within first third deviation ".format(len(weight_within_third_standarddeviation)*100.0/len(weight_list)))
