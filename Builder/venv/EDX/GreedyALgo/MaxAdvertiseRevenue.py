#!/usr/local/bin/python3
import operator


def max_rev(W,value,click):
    count = 0
    for i in range(W):
        count = count + (value[i] * click[i])
    print(count)

if __name__=="__main__":
    weights = []
    values1 =[]
    with open('3_3_dot_product20180216.in') as fin:
        line = fin.readline().strip()
        W = int(line)
        value_per_click = fin.readline().split(" ")
        click_per_day = fin.readline().split(" ")
        value_per_click = list(map(int, value_per_click))
        click_per_day = list(map(int, click_per_day))
        value_per_click.sort()
        click_per_day.sort()
        print(value_per_click)
        print(click_per_day)

    max_rev(W,value_per_click,click_per_day)
