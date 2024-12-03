import pandas as pd
import numpy as np

# Star 1
with open("day_2_input.txt") as file:
    data = [np.array(line.strip().split(' '), dtype=float) for line in file]

safe_report_1_count = 0

for reports in data:
    level_check = []

    for i in range(len(reports) - 1):
        current = reports[i]
        next = reports[i + 1]
        diff = next - current
        level_check.append(diff)
    level_check = np.array(level_check)

    if np.all(level_check <= 3.0) and np.all(level_check >= 1.0):
        safe_report_1_count = safe_report_1_count + 1
    if np.all(level_check <= -1.0) and np.all(level_check >= -3.0):
        safe_report_1_count = safe_report_1_count + 1

print("Answer 1: " + str(safe_report_1_count))

# Star 2
safe_report_2_count = 0

for reports in data:
    level_check = []
    local_count = 0

    for i in range(len(reports) - 1):
        current = reports[i]
        next = reports[i + 1]
        diff = next - current
        level_check.append(diff)
    level_check = np.array(level_check)

    if np.all(level_check <= 3.0) and np.all(level_check >= 1.0):
        local_count = 1
    if np.all(level_check <= -1.0) and np.all(level_check >= -3.0):
        local_count = 1

    for i in range(len(reports)):
        cleaned_level = np.delete(reports, i)
        level_check = []

        for i in range(len(cleaned_level) - 1):
            current = cleaned_level[i]
            next = cleaned_level[i + 1]
            diff = next - current
            level_check.append(diff)
            
        level_check = np.array(level_check)

        if np.all(level_check <= 3.0) and np.all(level_check >= 1.0):
            local_count = 1
        if np.all(level_check <= -1.0) and np.all(level_check >= -3.0):
            local_count = 1            
    safe_report_2_count = safe_report_2_count + local_count

print("Answer 2: " + str(safe_report_2_count))





