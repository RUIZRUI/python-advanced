# -*- coding: utf-8 -*-

import csv

students = [
    ['name', 'gender', 'age'],
    ['qixqi', 'female', 19],
    ['zx', 'male', 20]]

handle = open('csv_w.csv', 'w', newline='')     # 解决不同平台下换行不一致
writer = csv.writer(handle)
writer.writerows(students)
handle.close()

handle = open('csv_r.csv', 'r')
reader = csv.reader(handle)
for row in reader:
    print(row)

handle.close()
