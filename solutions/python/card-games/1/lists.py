"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    rounds_list = [number]
    rounds_list.append(number + 1)
    rounds_list.append(number + 2)
    return rounds_list


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    if number in rounds:
        return True
    else:
        return False


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    value = 0
    for number in hand:
        value += number

    return value / len(hand)


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    first_last_card = (hand[0] + hand[-1]) / 2

    if len(hand) % 2 == 0:
        middle_card = hand[len(hand) / 2 -1]
    else:
        middle_card = hand[len(hand) // 2]

    avarage = card_average(hand)

    if first_last_card == avarage or middle_card == avarage:
        return True
    else:
        return False

    
def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    even_hand = hand[::2]
    odd_hand = hand[1::2]
    if card_average(even_hand) == card_average(odd_hand):
        return True
    else:
        return False


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    if hand[-1] == 11:
        new_hand = hand[:]
        new_hand[-1] = 22
        return new_hand
    else:
        return hand
