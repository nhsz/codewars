# http://www.codewars.com/kata/55cbd4ba903825f7970000f5/

def get_grade(s1, s2, s3):
    mean_of_scores = (s1 + s2 + s3) / 3.0

    if 90 <= mean_of_scores <= 100:
        return "A"
    elif 80 <= mean_of_scores < 90:
        return "B"
    elif 70 <= mean_of_scores < 80:
        return "C"
    elif 60 <= mean_of_scores < 70:
        return "D"
    else:
        return "F"
