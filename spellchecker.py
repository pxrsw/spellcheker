import numpy as np
import json
import sys


def levenshtein(word1, word2):
    rows, cols = (len(word1) + 1, len(word2) + 1)
    arr = [[0 for i in range(cols)] for j in range(rows)]

    for i in range(0, rows):
        arr[i][0] = i

    for j in range(0, cols):
        arr[0][j] = j

    for i in range(1, rows):
        for j in range(1, cols):

            cost = 1
            if word1[i - 1] == word2[j - 1]:
                cost = 0

            arr[i][j] = (
                min(arr[i - 1][j], arr[i][j - 1], arr[i - 1][j - 1]) + cost
            )

    return arr[rows - 1][cols - 1]


def get_input():
    input_word = input()
    return input_word


def read_dic():
    with open("en.json", "r") as json_dic:
        dic = json.loads(json_dic.read())
    return dic


def swap_values_and_keys(dic):
    dic = dict(zip(dic.values(), dic.keys()))
    return dic


def check_word_exist_in_dic(dic, input_word):
    try:
        if type(dic[input_word]) != None:
            print("THIS WORD IS CORRECT")
            return 1
    except:
        pass


def check_spelling(input_word, dic, exist_in_dic):
    number_of_output = 0
    if exist_in_dic != 1:
        for item in sorted(dic.keys(), reverse=True):
            if (
                int(levenshtein(input_word, dic[item]) <= 1)
                and number_of_output < 4
            ):
                print(dic[item])
                number_of_output += 1


if __name__ == "__main__":
    input_word = get_input()
    dic = read_dic()
    exist_in_dic = check_word_exist_in_dic(dic, input_word)
    dic = swap_values_and_keys(dic)
    check_spelling(input_word, dic, exist_in_dic)
