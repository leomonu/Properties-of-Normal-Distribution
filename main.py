import random
import plotly.figure_factory as ff
import statistics

diceSum = []

for i in range(0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    sum = dice1 + dice2
    diceSum.append(sum)
    
mean = statistics.mean(diceSum)
std_deviation = statistics.stdev(diceSum)
print("This is mean",mean)
median = statistics.median(diceSum)
mode = statistics.mode(diceSum)
print("This is median",median)
print("This is mode :",mode)
print("This is stdDeviation ",std_deviation)

fig = ff.create_distplot([diceSum],["Result"],show_hist=False)
fig.show()