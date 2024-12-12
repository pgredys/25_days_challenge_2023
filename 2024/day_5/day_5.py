
def import_data(file: str) -> tuple[list[tuple[int, ...]], list[tuple[int, ...]]]:
    with open(file) as f:
        lines = f.read().splitlines()

    split_index = lines.index('')
    rules, records = lines[:split_index],lines[split_index+1:]

    rules = [tuple(map(int, i.split('|'))) for i in rules]
    records = [tuple(map(int,i.split(','))) for i in records]

    return rules, records

def is_correct(rules: list, record: tuple) -> bool:
    for rule in rules:
        if rule[0] in record and rule[1] in record:
            if record.index(rule[0]) < record.index(rule[1]):
                pass
            else:
                return False
    return True

def middle(record: tuple) -> int:
    ind = int(len(record) / 2)
    return record[ind]

def task_0(file: str) -> int:
    ord_rules, updates = import_data(file)
    answer = 0
    for update in updates:
        if is_correct(ord_rules, update):
            answer += middle(update)

    return answer

def task_1(file: str):
    ord_rules, updates = import_data(file)
    answer = 0
    for update in updates:
        update = list(update)
        if not is_correct(ord_rules, update):
            while not is_correct(ord_rules, update):
                for rule in ord_rules:
                    if rule[0] in update and rule[1] in update:
                        if update.index(rule[0]) > update.index(rule[1]):
                            a,b = update.index(rule[0]), update.index(rule[1])
                            update[b], update[a] = update[a], update[b]

            answer += middle(update)
            # print(update)
    return answer


if __name__ == '__main__':
    # task 0:
    print('First task')
    print(f'Test answer: {task_0("test.txt")}')  # expected: 143
    print(f'Final answer: {task_0("input.txt")} '  # expected: 5091
          f'\n-------------------\n')

    # task 1:
    print('Second task')
    print(f'Test answer: {task_1("test.txt")}')  # expected: 123
    print(f'Test answer: {task_1("input.txt")}')  # expected: 4681