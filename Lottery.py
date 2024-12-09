import random

def main():
    numbers = '0123456789'
    numbers_letters = list(numbers)
    my_ticket = list(input('What is your ticket: '))

    winning_ticket = []
    winning_tickets = 0

    while my_ticket != winning_ticket:
        winning_ticket = []
        for _ in range(len(my_ticket)):
            thing = random.choice(numbers)
            winning_ticket.append(thing)
                
        winning = ''.join(winning_ticket)
        print(f'The winning ticket is: {winning}.')
        winning_tickets += 1
        
    print('Congratulations, you won!')
    print(f'It took you {winning_tickets} times!')

if __name__ == '__main__':
    main()