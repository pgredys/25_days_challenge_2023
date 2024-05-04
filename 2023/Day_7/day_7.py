from functools import cmp_to_key

cards_order = ('A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J')


def load_input(path: str) -> list:
    with open(path, 'r') as file:
        return file.read().splitlines()


def card_strength(card: str) -> int:
    return len(cards_order) - cards_order.index(card)


def get_hand(line: str) -> str:
    return line.split()[0]


def get_bid(line: str) -> str:
    return int(line.split()[1])


def read_hands(path: str) -> list[str, int]:
    hands_list = []
    hands_line = load_input(input_path)
    for line in hands_line:
        hands_list.append([get_hand(line), get_bid(line)])
    return hands_list


def contains_joker(card_set: str):
    if card_set.find('J') >= 0:
        reference_rank = get_rank(card_set)
        letter_reference = ''
        for letter in cards_order:
            if get_rank(card_set.replace('J', letter)) > reference_rank:
                letter_reference = letter
                reference_rank = get_rank(card_set.replace('J', letter))

        if get_rank(card_set) < reference_rank:
            return card_set.replace('J', letter_reference)
        else:
            return card_set

    else:
        return card_set


def get_rank(card_set: str):
    counter = dict((k, card_set.count(k)) for k in cards_order if card_set.count(k) != 0)

    counter_list = list(counter.values())
    counter_list.sort(reverse=True)

    if counter_list[0] == 5:
        return 6
    if counter_list[0] == 4:
        return 5
    if counter_list[0] == 3 and counter_list[1] == 2:
        return 4
    if counter_list[0] == 3:
        return 3
    if counter_list[0] == 2 and counter_list[1] == 2:
        return 2
    if counter_list[0] == 2:
        return 1
    else:
        return 0


def compare_by_numbers(item1: str, item2: str):
    assert len(item1) == len(item2)

    if item1 == item2:
        return 0

    for letter_index, _ in enumerate(item1):

        if card_strength(item1[letter_index]) > card_strength(item2[letter_index]):
            return 1
        if card_strength(item1[letter_index]) < card_strength(item2[letter_index]):
            return -1


def compare(item1, item2):
    Item1 = contains_joker(item1)
    Item2 = contains_joker(item2)

    if get_rank(Item1) < get_rank(Item2):
        return -1
    elif get_rank(Item1) > get_rank(Item2):
        return 1
    else:
        return compare_by_numbers(item1, item2)


def first_answer(path: str) -> int:
    hands = read_hands(input_path)

    hands_list = [i[0] for i in hands]
    hands_reference = [i[0] for i in hands]
    hands_bid = [i[1] for i in hands]

    hands_list.sort(key=cmp_to_key(compare))

    result = 0
    for i, item in enumerate(hands_list):
        index = hands_reference.index(item)
        result += (i + 1) * hands_bid[index]

    return result


if __name__ == '__main__':
    input_path = 'camel_hands.txt'
    print(first_answer(input_path))
