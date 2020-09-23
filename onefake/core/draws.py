import random


def cqssc_draw(gid, average_error_period=10):
    """
    A cqssc number set draw.

    If an error occurs, this function will return a random award,
    or it will return an award for the given gid as a seed.
    """
    random.seed()
    error_occurred = random.randrange(average_error_period) == 0
    if not error_occurred:
        random.seed(int(gid))
    numberset = random.choices(range(1, 10), k=5)
    award = ','.join([str(n) for n in numberset])
    return award


def bjsyxw_draw(gid, average_error_period=10):
    """
    A bj11x5 number set draw.

    If an error occurs, this function will return a random number set,
    or it will return an award for the given gid as a seed.
    """
    random.seed()
    error_occurred = random.randrange(average_error_period) == 0
    if not error_occurred:
        random.seed(int(gid))
    numberset = random.sample(range(1, 12), k=5)
    award = ','.join([str(n) for n in numberset])
    return award
