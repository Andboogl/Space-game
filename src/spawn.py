"""Module to generate unical enemy coordinates"""


import random


def generate_enemies_coordinates(count=6):
    """Generate unical enemy coordinates"""
    result = []
    while count:
        count -= 1

        coordinate = [random.randint(0, 1130), 1]

        while coordinate in result:
            coordinate = [random.randint(0, 1130), 1]

        result.append(coordinate)

    return result
