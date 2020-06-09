import pandas as pd


def grade(values):
    if 70 <= values["score"] < 80:
        values["score"] = "C"
    elif 80 <= values["score"] < 90:
        values["score"] = "B"
    elif 90 <= values["score"]:
        values["score"] = "A"
    else:
        values["score"] = "F"
    return values


scores = pd.DataFrame({"score": [89, 70, 71, 65, 30, 93, 100, 75]})
scores.apply(grade, axis=1)
