# blackjack-bot
Bot that apply the martingale model on [tibiablackjack roulette](https://tibiablackjack.com/roulette) for cryptocoins
### Using the martingale system
The most effective way of using the Martingale is to only bet on one color (this bot only bet on Red). They have the maximum odds of winning (almost 50%), but the lowest payout of all – 1:1. This means you win the same amount of money you bet for the spin. Overall, those are the safest bets you could possibly place in a game of roulette. If you want to try out these types of bets, you can check out these best online casino USA sites which offer roulette games.

For even-money bets, the bet progression that you will use goes like this:

	1 – 2 – 4 – 8 – 16 – 32 – 64 – 128 – 256 – 512 – 1024 – 2048 – 4096 – 8192
	
So, if yout bet $1 on red and you lose, next round you will bet $2 on red. If you lose again, bet $4 on red next round.
If you win, next round you should bet $1

### How to bet with this bot

Execute the dist/bot.exe or run bot.py
To run bot.py, you must have selenium lib installed (pip install selenium)

The software will expect your inputs:
- the first one is your username on tibiablackjack.com, to confirm your login

- the second one is the minimum bet

- and third is the maximum number of consecutive losses until restart with minimum bet (this step was requested by my client - and to full utilize it, just type '999')

If you get stucked in captcha at login, you have 45 seconds to pass it manually
