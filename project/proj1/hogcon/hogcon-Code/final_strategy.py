"""
    This file contains your final_strategy that will be submitted to the contest.

    You can only depend on "general-purpose" libraries - do not import or open any
    contest-specific files, like other Python or text files. All contest logic must
    be in this file.

    Remember to supply a unique PLAYER_NAME or your submission will not succeed.
"""

PLAYER_NAME = '若雨茗秋'  # Change this line!

def swine_swap(player_score, opponent_score):
    
    exitment=3**(player_score+opponent_score)
    tail=exitment%10
    sum0=0
    while exitment>0:
        tail0=exitment%10
        sum0=sum0*10+tail0
        exitment//=10
    tail1=sum0%10
    return tail1==tail

def picky_piggy(score):
    
    if score==0:
        
        return 1
    else:
        return int((1/21*10**(score%6+6))%10)   
def picky_piggy_strategy(score, opponent_score, cutoff=8, num_rolls=6):
   
    if picky_piggy(opponent_score)>=cutoff:
        return 0
    else:
        return num_rolls
    
    
def swine_swap_strategy(score, opponent_score, cutoff=8, num_rolls=6):
    
    if swine_swap(score+picky_piggy(opponent_score),opponent_score) and opponent_score-score>=cutoff:
        return 0
    else:
        return num_rolls
    
    

def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.

    *** YOUR DESCRIPTION HERE ***
    """
    # BEGIN PROBLEM 12
    if picky_piggy_strategy(score,opponent_score)==0:
        return 0
    elif swine_swap_strategy(score,opponent_score)==0:
        return 0
    else:
        return 6