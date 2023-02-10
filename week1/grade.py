"""grade"""
def main(point):
    if point >= 50:
        return print("Congrats!! You passed.")
    print("Sorry!! You failed.")
main(float(input()))