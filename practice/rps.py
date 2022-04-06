import random

from psutil import users


def play():
    user = input("r ,p , s")
    comp = random.choice(['r', 'p', 's'])


    if user == comp:
        return 'It\'s a tie'
      
    if is_win(user, comp):
        return (f'You won! your {user} beats comps {comp}')
      
    return (f'You lost! computers {comp} beats your {user}')

def is_win(p, opp):
  # return true if player wins
  # r > s, s>p, p>r
  
  if (p == 'r' and opp == 's') or (p == 's' and opp == 'p') or (p == 'p' and opp == 'r'):
      return True

print(play())
