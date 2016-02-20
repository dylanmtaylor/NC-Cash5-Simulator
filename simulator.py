from __future__ import unicode_literals
from prompt_toolkit import prompt
import random

def random_balls(max):
    return random.sample(range(1, max), 5)

print("North Carolina Cash 5 Lottery Game Simulator")

high_num = 39
qp = True
qp_in = prompt('Use quick pick numbers [Y/n]? ', default='Y')
picked = random_balls(high_num)
prizes = [1,4,200,50000] #2,3,4,5 wins respectively
game = 1
tickets = 1
spent = 0
won = 0
lost = 0
net = 0
winnings = 0

if qp_in.upper()[0] == 'Y':
    print('Okay, each ticket will be picked randomly.')
else:
    for i in range(0,5):
	picked[i] = prompt('Enter number %d of 5: ' % int(i+1))
    qp = False

games = int(prompt('How many games would you like to simulate? ', default='1'))
if qp:
    tickets = int(prompt('How many tickets will be bought per game? ', default='1'))

cost = float(prompt('How much does each ticket cost? $', default='1.00'))

print 'Default prizes are set to: ',
for i, p in enumerate(prizes):
    print '$%.2f' % p + (',' if i+1 < len(prizes) else '\n'),
override = prompt('Would you like to override these values [Y/n]? ', default='n')

while game <= games:
    print('Simulating game %s / %s ... (%s%%)') % (game, games, (game*100/games))
    # have to pay to play
    g_spent = (cost * tickets)
    spent += g_spent
    winners = random_balls(high_num)
    g_winnings = 0
    max_matched = 0
    print('\tWinning numbers: '),
    for w in winners:
	print w,
    print
    for t in range(0,tickets):
        matched = 0
        print('Checking ticket %d of %d...' % (t+1, tickets))
        if qp:
    	   picked = random_balls(high_num)
        print('\tPicked numbers: '),
        for p in picked:
    	    if p in winners:  # highlight the winning numbers and count matches
                matched += 1
    	        print '\033[1m',
            else:
                print '\033[0m',
    	    print p,
        print '\033[0m', # remove bold attribute from text
        print('(%d' % matched) + (' matches' if (matched != 1) else ' match'),
        if (matched < 2):
            print '; $0.00)'
        else:
            g_winnings += prizes[matched-2]
	    print '; $%.02f)' % prizes[matched-2]
            if max_matched < matched:
                max_matched = matched
    winnings += g_winnings
    # Unless a game is at least break-even, we do not consider it to be a win
    if (g_winnings < (cost * tickets)):
        lost += 1
        print('\tYou lost this game (-$%.2f net earnings).' % (g_spent - g_winnings))
    else:
        won += 1
        print('\tYou won this game ($%.2f net earnings)' % (g_winnings - g_spent))
    net += g_winnings - (cost * tickets)
    print('\tTotal spent: $%.2f' % spent)
    print('\tTotal winnings: $%.2f' % winnings)
    print('\tNet return on gambling: $%.2f' % net)
    print('\tWon: %d; Lost: %d; Win Percentage: %.03f%%') % (won, lost, (won*100/(won+lost)))

    game += 1
    # A winning game is defined as having 2 or more matches
