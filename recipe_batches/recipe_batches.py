#!/usr/bin/python

import math


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged = [0] * elements

    a = 0
    b = 0

    for i in range(elements):
        if a >= len(arrA):
            merged[i] = arrB[b]
            b += 1
        elif b >= len(arrB):
            merged[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:
            merged[i] = arrA[a]
            a += 1
        else:
            merged[i] = arrB[b]
            b += 1
    return merged


def recursive_split(arr):
    if len(arr) < 2:
        return arr
    return merge(recursive_split(arr[:len(arr)//2]), recursive_split(arr[len(arr)//2:]))


def recipe_batches(recipe, ingredients):

    batches = 0
    amounts = []
    less_than = "false"

    for (key, value), (key2, value2) in zip(recipe.items(), ingredients.items()):
        if len(ingredients) >= len(recipe):
            if value > value2:
                print(value)
                less_than = "true"
            else:
                amount = value2 // value
                amounts.append(amount)
                batches = recursive_split(amounts)[0]
        else:
            batches = 0

    if less_than == "true":
        batches = 0
    print(f"{batches} batches can be made from the available ingredients: {ingredients}.")


# if __name__ == '__main__':
#     # Change the entries of these dictionaries to test
#     # your implementation with different inputs
#     recipe = {'milk': 100, 'butter': 50, 'flour': 5}
#     ingredients = {'milk': 132, 'butter': 78, 'flour': 51}
#     print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
#         batches=recipe_batches(recipe, ingredients), ingredients=ingredients))

recipe_batches({'milk': 100, 'butter': 50, 'flour': 5},
               {'milk': 10232, 'butter': 800, 'flour': 96})
