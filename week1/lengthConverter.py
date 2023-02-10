"""LengthConverter"""
def main():
    foot = float(input("Foot : "))
    inch = float(input("Inch : "))
    centimeter = 0
    centimeter = centimeter + foot*30
    centimeter = centimeter + inch*2.5
    meter = centimeter//100
    centimeter = centimeter%100
    print("%d m. %d centimeter" %(meter, centimeter))
main()