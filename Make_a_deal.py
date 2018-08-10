#!/usr/bin/env python

'''  application of Make a deal statistics
     for reference:
     https://math.stackexchange.com/questions/608957/monty-hall-problem-extended
'''
import pdb  # noqa F401
import random
from Utils.plogger import set_logger, timed, func_args

logfile = 'make_a_deal.log'
logformat = '%(asctime)s:%(levelname)s:%(message)s'
logger = set_logger(logfile, logformat, 'DEBUG')


class Make_A_DealObject:

    def __init__(self):
        pass

    def pick(self, doors, doors_to_open):
        self.doors = doors
        self.doors_to_open = doors_to_open
        win_1, win_2 = False, False
        open_doors = []

        price = random.randint(1, self.doors)
        open_door = price
        i = 0
        while i < doors_to_open:
            while open_door == price or open_door in open_doors:
                open_door = random.randint(2, self.doors)
            open_doors.append(open_door)
            i += 1

        select_door = open_doors[0]
        while select_door in open_doors:
            select_door = random.randint(2, self.doors)

        win_1 = (1 == price)
        win_2 = (select_door == price)
        # pdb.set_trace()

        return win_1, win_2

    def pick1(self, doors, doors_to_open):
        global dbg_open, dbg_select, dbg_price
        self.doors = doors
        self.doors_to_open = doors_to_open
        win_1, win_2 = False, False
        open_doors = []

        price = random.randint(1, self.doors)
        open_door = price
        i = 0
        while i < doors_to_open:
            open_door = random.randint(2, self.doors)
            while open_door == price or open_door in open_doors:
                open_door += 1
                if open_door == self.doors + 1:
                    open_door = 2

            open_doors.append(open_door)
            i += 1

        select_door = open_doors[0]
        while select_door in open_doors:
            select_door = random.randint(2, self.doors)

        win_1 = (1 == price)
        win_2 = (select_door == price)
#       pdb.set_trace()

        return win_1, win_2

    def pickset(self, doors, doors_to_open):
        self.doors = doors
        self.doors_to_open = doors_to_open
        win_1, win_2 = False, False

        doors_set = set(range(1, self.doors+1))
        price_set = set(random.sample(doors_set, 1))
        choice1_set = set(random.sample(doors_set, 1))
        open_set = set(random.sample(doors_set.difference(price_set).
                       difference(choice1_set), doors_to_open))
        choice2_set = set(random.sample(doors_set.difference(open_set).
                          difference(choice1_set), 1))
        win_1 = choice1_set.issubset(price_set)
        win_2 = choice2_set.issubset(price_set)

        return win_1, win_2

@func_args(logger)
def screen_input(question, input_range):
    '''  Function to deal and check screen input
         input_range is a tuple with lowest and highest value included
         question is string what number to input
         functin output is the response value, if 'q' was answered value is -1
    '''
    #  pdb.set_trace()
    key_input = True
    while key_input:
        try:
            reply = input('How many {} (between {} and {})(q is quit): '.
                          format(question, input_range[0], input_range[1]))
            if reply == 'q':
                reply = -1
                break
            else:
                reply = int(reply)

            if reply in range(input_range[0], input_range[1]+1):
                key_input = False

        except Exception as e:
            print('Exception: ', e)
            logger.exception('Exception: {}'.format(e))

    return reply

@func_args(logger)
def test_result(doors, doors_to_open):
    '''  Calculates the theoratical results as given in the reference
    '''
    logger.info('Name option: Theoretical results')
    win_1 = 1/doors
    win_2 = (doors - 1)/doors*(1/(doors-doors_to_open-1))

    print('number of wins option 1 is {:.2f}%: '.
          format(100*win_1))
    print('number of wins option 2 is {:.2f}%: '.
          format(100*win_2))

    logger.info('number of wins option 1 is {:.2f}%: '.
                format(100*win_1))
    logger.info('number of wins option 2 is {:.2f}%: '.
                format(100*win_2))

@timed(logger)
@func_args(logger)
def make_a_deal_func(throws, doors, doors_to_open, func):
    '''  this function runs a make_a_deal_function defined in func
         which has input arguments doors and doors_to_open
    '''
    logger.info('Name option: {}'.format(func.__name__))
    number_of_wins_1, number_of_wins_2, counter = 0, 0, 0

    while counter < throws:
        win_1, win_2 = func(doors, doors_to_open)

        if win_1:
            number_of_wins_1 += 1

        if win_2:
            number_of_wins_2 += 1

        counter += 1
        print('completion is {:.2f}%'.
              format(100*counter/throws), end='\r')

    print('number of wins option 1 is {:.2f}%: '.
          format(100*number_of_wins_1/counter))
    print('number of wins option 2 is {:.2f}%: '.
          format(100*number_of_wins_2/counter))

    logger.info('number of wins option 1 is {:.2f}%: '.
                       format(100*number_of_wins_1/counter))
    logger.info('number of wins option 2 is {:.2f}%: '.
                       format(100*number_of_wins_2/counter))

@timed(logger)
def main():
    '''  main program of Make_a_deal. Enter number of throws function is called
         and then goes in an infinate loop to repeat the experiment
         loop is ended by entering 'q'
    '''
    throws = screen_input('throws', (1, 1000000))
    if throws == -1:
        return
    logger.info("-"*40)
    logger.info('number of throws: {}'.format(throws))

    while True:
        doors = screen_input('doors', (2, 100))
        if doors == -1:
            return

        doors_to_open = screen_input('doors to open', (1, doors-2))
        if doors_to_open == -1:
            return

        logger.info('Number of doors is {}, number of doors to open is {}'.
                           format(doors, doors_to_open))

        price = Make_A_DealObject()
        make_a_deal_func(throws, doors, doors_to_open, price.pick)
        make_a_deal_func(throws, doors, doors_to_open, price.pick1)
        make_a_deal_func(throws, doors, doors_to_open, price.pickset)
        test_result(doors, doors_to_open)


if __name__ == '__main__':
    main()
