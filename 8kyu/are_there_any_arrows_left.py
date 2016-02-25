# http://www.codewars.com/kata/559f860f8c0d6c7784000119/

def any_arrows(arrows):
    return any(not i.get("damaged", False) for i in arrows)
