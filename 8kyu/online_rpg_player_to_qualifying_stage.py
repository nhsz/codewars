# http://www.codewars.com/kata/55849d76acd73f6cc4000087/

def player_rank_up(pts):
    message = """Well done! You have advanced to the qualifying stage.
                 Win 2 out of your next 3 games to rank up."""
    return message if pts >= 100 else False
