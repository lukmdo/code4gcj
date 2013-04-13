#!/usr/bin/python3
"""
python Btrains.py < IN-FILE.in > OUT-FILE.out
python Btrains.py < IN-FILE.in | tee OUT-FILE.out
"""
import itertools

def add_n_mins(str_time, n_minutes):
    """
    Returns: new_str_time =  str_time + n_minutes

    would invite datetime to party when needed
    """
    if not n_minutes:
        return str_time
    time_hours, time_minutes = int(str_time[:2]), int(str_time[-2:])
    add_n_hours, n_minutes = divmod(time_minutes + n_minutes, 60)
    return '{:02d}:{:02d}'.format(time_hours + add_n_hours, n_minutes)

def gen_num_trains(departures, arrivals, turnarround):
    t = 0
    if not departures:
        return 0

    ARRIVAL_TYPE = 10
    DEPARTURE_TYPE = 20
    departures = zip(departures, itertools.repeat(DEPARTURE_TYPE))
    arrivals = zip(arrivals, itertools.repeat(ARRIVAL_TYPE))
    all_events = itertools.chain(arrivals, departures)

    on_side = []
    for item in sorted(all_events):
        str_time, event_type = item
        if event_type == DEPARTURE_TYPE:
            if not on_side:
                t += 1
                continue
            if on_side[0] <= str_time:
                on_side.pop(0)
                continue
            else:
                t += 1
        elif event_type == ARRIVAL_TYPE:
            ready_to_go_at = add_n_mins(str_time, turnarround)
            on_side.append(ready_to_go_at)

    return t


def solve(num_cases):
    for i in range(1, num_cases+1):
        turnarround = int(input())
        num_from_a, num_from_b = input().split(' ')
        departure_from_a, arrive_at_a = [], []
        departure_from_b, arrive_at_b = [], []
        for _ in range(int(num_from_a)):
            d, a = input().split(' ')
            departure_from_a.append(d)
            arrive_at_b.append(a)
        for _ in range(int(num_from_b)):
            d, a = input().split(' ')
            departure_from_b.append(d)
            arrive_at_a.append(a)

        num_a = gen_num_trains(departure_from_a, arrive_at_a, turnarround)
        num_b = gen_num_trains(departure_from_b, arrive_at_b, turnarround)
        print('Case #{num}: {num_a} {num_b}'.format(
            num=i, num_a=num_a, num_b=num_b))

if __name__ == '__main__':
    num_cases = int(input())
    solve(num_cases)
