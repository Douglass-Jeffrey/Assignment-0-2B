#!/usr/bin/env python3

# Created by: Douglass Jeffrey
# Created on: Oct 2019
# This program calculates area of triangles


def main():
    # this function calculates the area of the triangles

    # input
    num1 = int(input("Input the base length of the triangle: "))
    num2 = int(input("Input the height of the triangle: "))

    # process
    answer = (num1*num2)/2

    # output
    print("")
    print("The area of the triangle is {} units^2".format(answer))


if __name__ == "__main__":

    main()
