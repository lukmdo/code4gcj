def _open_combinations(chests_opened, chests, keys):
    keys_set = set(keys)
    chests_opened_set = set(chests_opened)
    combinations = []

    for chest in chests:
        chest_num, open_key, *found_keys = chest
        if chest_num in chests_opened_set:
            continue
        if open_key in keys_set:
            new_chests_opened = list(chests_opened)
            new_chests_opened.append(chest_num)

            new_keys = list(keys)
            new_keys.remove(open_key)  # any key of type open_key
            new_keys.extend(found_keys)

            combination = (tuple(new_chests_opened), tuple(new_keys))
            combinations.append(combination)

    return combinations


def get_open_combination(init_keys, chests):
    combinations = [_open_combinations([], chests, init_keys)]
    # import pdb; pdb.set_trace()

    for step in range(1, len(chests)):
        if len(combinations) < step:
            break  # no combinations from prev step
        last_combinations = combinations[-1]
        print(len(combinations))
        print(len(last_combinations))

        for combination in last_combinations:
            new_combinations = _open_combinations(combination[0], chests, combination[1])
            if len(combinations) <= step:
                combinations.append([])
            combinations[step].extend(new_combinations)

        last_combinations.clear()  # free some memory

    if len(combinations) < len(chests):
        return None
    options = [c[0] for c in combinations[-1]]
    if not options:
        return None
    best_combination = sorted(options)[0]

    return tuple(best_combination)


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

        solved = get_open_combination(init_keys, chests) or 'IMPOSSIBLE'
        print('Case #{case_num}: {solved}'.format(
            case_num=case_num, solved=solved))

if __name__ == '__main__':
    import sys
    with open(sys.argv[-1], 'r') as f:
        input = f.readline
        num_cases = int(input())
        solve(num_cases)
