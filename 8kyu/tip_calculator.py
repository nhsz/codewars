# http://www.codewars.com/kata/56598d8076ee7a0759000087/

import math


def calculate_tip(amount, rating):
    tip_percentage = {"terrible": 0, "poor": 0.05, "good": 0.1, "great": 0.15, "excellent": 0.2}
    
    if rating.lower() in tip_percentage.keys():
        return math.ceil(amount * tip_percentage[rating.lower()])
    else:
        return "Rating not recognised"
