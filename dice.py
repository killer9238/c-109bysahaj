import random
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import statistics

dice_result=[]
count=[]
for i in range (0,100):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice_result.append(dice1+dice2)
mean=sum(dice_result)/len(dice_result)
standarddeviation=statistics.stdev(dice_result)
print("Mean is ->"+str(mean))
print("Standard Deviation ->"+str(standarddeviation))

median=statistics.median(dice_result)
mode=statistics.mode(dice_result)
print("Median is ->"+str(median))
print("Mode is -> "+str(mode))

fig=ff.create_distplot([dice_result],["Result"],show_hist=False)
fig.show()