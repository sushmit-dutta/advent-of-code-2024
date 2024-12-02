import pandas as pd
import numpy as np


# Star 1
data = pd.read_csv('data/day_1.txt', sep='\s+', header=None)
data.columns = ['Team1', 'Team2']

team_1 = data['Team1'].to_numpy()
team_2 = data['Team2'].to_numpy()

team_1_sorted = np.sort(team_1)
team_2_sorted = np.sort(team_2)

diff = abs(team_2_sorted - team_1_sorted)
print("Star 1 Answer: " + str(sum(diff)))

# Star 2

arr = []

for check_1 in team_1:
    count = 0
    for check_2 in team_2:
        if check_1 == check_2:
            count = count + 1
    arr.append(check_1 * count)
print(sum(arr))
    




