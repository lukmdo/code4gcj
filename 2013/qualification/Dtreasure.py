#!/usr/bin/python3
"""
python Dtreasure.py < IN-FILE.in > OUT-FILE.out
python -u Dtreasure.py < IN-FILE.in | tee OUT-FILE.out
"""
from collections import Counter


def _can_open_all(chests, keys):
    if not chests:
        return True
    # eulerian path: code.google.com/codejam/contest/2270488/dashboard#s=a&a=3

    # enough_keys_by_type
    all_keys = list(keys)
    chest_open_keys = []
    for chest in chests:
        chest_num, open_key, *found_keys = chest
        all_keys.extend(found_keys)
        chest_open_keys.append(open_key)
    all_keys_count = Counter(all_keys)
    chest_open_keys_count = Counter(chest_open_keys)
    enough_keys_by_type = all(
        v <= all_keys_count.get(k, 0) for k, v in chest_open_keys_count.items())
    if not enough_keys_by_type:
        return False

    # each chest_open_key type can be reached
    chest_open_keys_set = set(chest_open_keys)
    seen_keys_set = set(keys)
    if chest_open_keys_set.issubset(seen_keys_set):
        return True
    can_open_and_non_empty = lambda c: c[2:] and c[1] in seen_keys_set
    other_chests = set(chests)

    bfs_queue = set(filter(can_open_and_non_empty, chests))
    while bfs_queue:
        other_chests -= bfs_queue
        chest = bfs_queue.pop()
        seen_keys_set |= set(chest[2:])
        if chest_open_keys_set.issubset(seen_keys_set):
            return True
        child_chests = filter(can_open_and_non_empty, other_chests)
        bfs_queue |= set(child_chests)

    return False


def get_open_combination(init_keys, chests):
    if not _can_open_all(chests, init_keys):
        return None

    keys = list(init_keys)

    combination = tuple()
    for _ in range(len(chests)):
        temp_keys = list(keys)
        temp_chests = list(chests)
        for i, chest in enumerate(chests):
            chest_num, open_key, *found_keys = chest
            if open_key not in temp_keys:
                continue
            new_chests = list(temp_chests)
            new_chests.pop(i)
            new_keys = list(temp_keys)
            new_keys.remove(open_key)
            new_keys.extend(found_keys)
            if _can_open_all(new_chests, new_keys):
                keys = new_keys
                chests = new_chests
                combination += (chest_num,)
                break

    return combination


def solve(num_cases):
    for case_num in range(1, num_cases + 1):
        case_info = input().split(' ')
        num_init_keys, num_chests = int(case_info[0]), int(case_info[1])

        init_keys = [int(key_type) for key_type in input().split(' ')]
        chests = []
        for chest_num in range(1, num_chests + 1):
            chest_info = [int(item) for item in input().split(' ')]
            open_key = chest_info[0]
            keys_in_chest = chest_info[2:]

            chest = [chest_num, open_key] + keys_in_chest
            chests.append(tuple(chest))

        solved = get_open_combination(init_keys, chests)
        solved = ' '.join(str(n) for n in solved) if solved else 'IMPOSSIBLE'
        print('Case #{case_num}: {solved}'.format(
            case_num=case_num, solved=solved))

if __name__ == '__main__':
    num_cases = int(input())
    solve(num_cases)
