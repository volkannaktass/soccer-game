import random as r

s1 = {"x1": 55, "y1": 10, "length": 50, "height": 50}
s2 = {"x1": 5, "y1": 20, "length": 35, "height": 50}

c1 = {"x1": 5, "y1": 10, "diameter": 50}
c2 = {"x1": 5, "y1": 10, "diameter": 25}


class Collusion():
    def __init__(self, s1, s2, c1, c2):
        self.s1 = s1
        self.s2 = s2
        self.c1 = c1
        self.c2 = c2

    @staticmethod
    def rect2rect(s1, s2):
        s1["x2"] = s1["x1"] + s1["length"]
        s2["x2"] = s2["x1"] + s2["length"]

        if ((s1["x1"] < s2["x1"] and s2["x1"] < s1["x2"]) or (s1["x1"] < s2["x2"] and s2["x2"] < s1["x2"])):
            print("Collision!")

        elif ((s2["x1"] < s1["x1"] and s1["x1"] < s2["x2"]) or (s2["x1"] < s1["x2"] and s1["x2"] < s2["x2"])):
            print("Collision!")
        elif (s1["x1"] == s2["x1"] or s2["x1"] == s1["x2"] or s1["x1"] == s2["x2"] or s2["x2"] == s1["x2"]):
            print("Collision!")
        else:
            print("No Collision!!!")

    @staticmethod
    def circle2circle(c1, c2):

        c1["x2"] = c1["diameter"] + c1["x1"]
        c2["x2"] = c2["diameter"] + c2["x1"]
        c1["x3"] = (c1["diameter"] / 2) + c1["x1"]
        c2["x3"] = c2["diameter"] / 2 + c2["x1"]

        if (c2["x1"] < c1["x2"] and c2["x1"] > c1["x1"]) or (c2["x2"] < c1["x2"] and c2["x2"] > c1["x1"]):
            print("Collision!")
        elif (c1["x1"] < c2["x3"] and c2["x3"] < c1["x2"]) or (c2["x1"] < c1["x3"] and c1["x3"] < c2["x2"]):
            print("Collision!")
        elif c2["x1"] == c1["x2"] or c2["x1"] == c1["x1"] or c2["x3"] == c1["x3"] or c2["x2"] == c1["x1"]:
            print("Collision!")
        else:
            print("No Collision!!!")

    @staticmethod
    def rect2circle(s1, c1):

        s1["x2"] = s1["x1"] + s1["length"]
        c1["x2"] = c1["diameter"] + c1["x1"]
        c1["x3"] = (c1["diameter"] / 2) + c1["x1"]

        if (s1["x1"] < c1["x1"] and c1["x1"] < s1["x1"]) or (s1["x1"] < c1["x2"] and c1["x2"] < s1["x2"]) or (
                s1["x1"] < c1["x1"] and c1["x3"] < s1["x2"]):
            print("Collision!")
        elif s1["x1"] == c1["x1"] or s1["x1"] == c1["x2"] or s1["x1"] == c1["x2"] or s1["x2"] == c1["x1"]:
            print("Collision!")
        else:
            print("No Collision!!!")


collusion = Collusion(s1, s2, c1, c2)

collusion.rect2rect(s1, s2)
collusion.circle2circle(c1, c2)
collusion.rect2circle(s1, c1)

# generate1 = input("Which shape would you like to generate?")
# generate2 = input("Which shape would you like to generate?")


# if generate1 == "square" and generate2 == "square":
#    rect2rect()

# elif generate1 == "circle" and generate2 == "circle":
#     circle_circle()
# elif (generate1 == "circle" and generate2 == "square") or (generate1 == "square" and generate2 == "circle"):
#     squarecircle()
# else:
#     print("Invalid Input..!!!")






