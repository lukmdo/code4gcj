#!/usr/bin/python3
"""
python Benergy.py < IN-FILE.in > OUT-FILE.out
python -u Benergy.py < IN-FILE.in | tee OUT-FILE.out
"""


def get_max_gain(E, R, importance_values):
    N = len(importance_values)
    if R > E:
        R = E
    total = 0

    # list( [[got_energy, needed_energy], gain], ... )
    activities = [[[E, 0], i] for i in importance_values]
    activities_index = sorted(
        range(N), key=lambda x: importance_values[x], reverse=True)

    for i in activities_index:
        energy_data, gain = activities[i]

        if energy_data[0] is None:
            energy_data[0] = E
        if energy_data[1] is None:
            energy_data[1] = 0

        total += (energy_data[0] - energy_data[1]) * gain

        head_got_energy, head_need_energy = energy_data

        # on left side
        for j, k in enumerate(range(i - 1, -1, -1)):
            [got_energy, need_energy], gain = activities[k]
            regain = R * (j + 1)
            new_need_energy = head_got_energy - regain
            if new_need_energy > need_energy:
                activities[k][0][1] = new_need_energy
            if new_need_energy <= 0:
                break

        # on right side
        for j, k in enumerate(range(i + 1, N)):
            [got_energy, need_energy], gain = activities[k]
            regain = R * (j + 1)
            new_got_energy = head_need_energy + regain
            if new_got_energy < got_energy:
                activities[k][0][0] = new_got_energy
            if new_got_energy >= E:
                break

    return total


def solve(num_cases):
    for i in range(1, num_cases + 1):
        case_info = input().split(' ')
        case_data = input().split(' ')
        E, R, num_importance_values = map(int, case_info)
        importance_values = list(map(int, case_data))
        solved = get_max_gain(E, R, importance_values)
        print('Case #{num}: {solved}'.format(num=i, solved=solved))

if __name__ == '__main__':
    num_cases = int(input())
    solve(num_cases)
