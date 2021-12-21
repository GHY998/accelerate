# MIT License

# Copyright (c) 2021 Mikhail Tsitsvero

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from ase import Atoms, Atom, io
import re
import os
import matplotlib.pyplot as plt

import pandas as pd

import math
import numpy as np


def as_num(x):
    y='{:.4f}'.format(x)
    return(y)


def _sum(arr, n):
    # 使用内置的 sum 函数计算
    return (sum(arr))


def eq_list_to_xyz(input_file, output_file):
    with open(input_file) as f:
        file_content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    file_content = [x.strip() for x in file_content]
    f.close()

    molecules = []

    line_index = -1
    for line in file_content:
        line_index += 1
        if re.match(r"# Geometry", line):

            m = re.match(r'# Geometry of EQ (?P<ind>.*), SYMMETRY = (?P<symmtype>.*)', line)
            mol = Atoms()
            mol.info['eq_num'] = int(m.group('ind'))
            mol.info['symm_type'] = str(m.group('symmtype'))

            # for i in range(1, num_atoms + 1):
            #     atom,x,y,z = file_content[line_index + i].split()
            #     mol.append(Atom(atom,(x,y,z)))

            i = 1
            while not re.search("Energy", file_content[line_index + i]):
                atom, x, y, z = file_content[line_index + i].split()
                mol.append(Atom(atom, (x, y, z)))
                i = i + 1

            num_atoms = i - 1

            m = re.match(r'Energy    = (?P<energy>.*) \((?P<energy2>.*) :    (?P<someconst>.*)\)',
                         file_content[line_index + num_atoms + 1])
            mol.info['energy'] = float(m.group('energy'))
            mol.info['energy2'] = float(m.group('energy2'))
            mol.info['someconst'] = float(m.group('someconst'))

            m = re.match(r'Spin\(\*\*2\) =    (?P<spin>.*)', file_content[line_index + num_atoms + 2])
            mol.info['spin'] = float(m.group('spin'))

            m = re.match(r'ZPVE      =    (?P<zpve>.*)', file_content[line_index + num_atoms + 3])
            mol.info['zpve'] = float(m.group('zpve'))

            molecules.append(mol)
            io.write(output_file, molecules, 'xyz')

    io.write(output_file, molecules, 'xyz')
    return molecules


import glob

# Get all log-files within directories
all_files = glob.glob("../files/urea_01/*/*.log")
# all_files = glob.glob("urea-01-7e-step2_EQ_list.log")


for file in all_files:
    ary = file.split("\\")
    # molecules = eq_list_to_xyz(file, f'test_{ary[-3]}_{ary[-2]}.xyz')
    molecules = eq_list_to_xyz(all_files[0], 'test.xyz')
    molecules1 = eq_list_to_xyz(all_files[1], 'test.xyz')
    molecules2 = eq_list_to_xyz(all_files[2], 'test.xyz')
    molecules3 = eq_list_to_xyz(all_files[3], 'test.xyz')
    molecules4 = eq_list_to_xyz(all_files[4], 'test.xyz')
    molecules5 = eq_list_to_xyz(all_files[5], 'test.xyz')
    molecules6 = eq_list_to_xyz(all_files[6], 'test.xyz')

    energies = []
    for mol in molecules:
        energies.append(mol.info["energy"])
        # print(molecules[0].info['energy'])
    print(energies)

    x = 0

    for i in energies:
        x += 1

    print("the total number of the first position are " ,x)
    print("the minimum in the first position is " ,min(energies))

    average = sum(energies) / x
    print('累加值', sum(energies), '平均值', average)

    energies1 = []
    for mol in molecules1:
        energies1.append(mol.info["energy"])
    # print(molecules[0].info['energy'])
    print(energies1)

    x1 = 0

    for i in energies1:
        x1 += 1

    print("the total number of the second position are " ,x1)
    print("the minimum in the position is " ,min(energies1))

    average1 = sum(energies1) / x1
    print('1累加值', sum(energies1), '平均值', average1)

    energies2 = []
    for mol in molecules2:
        energies2.append(mol.info["energy"])
        # print(molecules[0].info['energy'])
    print(energies2)

    x2 = 0

    for i in energies2:
        x2 += 1

    print("the total number of the third position are " ,x2)
    print("the minimum in the position is " ,min(energies2))

    average2 = sum(energies2) / x2
    print('累加值', sum(energies2), '平均值', average2)

    energies3 = []
    for mol in molecules3:
        energies3.append(mol.info["energy"])
        # print(molecules[0].info['energy'])
    print(energies3)

    x3 = 0

    for i in energies3:
        x3 += 1

    print("the total number of the fourth position are " ,x3)
    print("the minimum in the position is " ,min(energies3))

    average3 = sum(energies3) / x3
    print('累加值', sum(energies3), '平均值', average3)

    energies4 = []
    for mol in molecules4:
        energies4.append(mol.info["energy"])
        # print(molecules[0].info['energy'])
    print(energies4)

    x4 = 0

    for i in energies4:
        x4 += 1

    print("the total number of the fifth position are " ,x4)
    print("the minimum in the position is " ,min(energies4))

    average4 = sum(energies4) / x4
    print('累加值', sum(energies4), '平均值', average4)

    energies5 = []
    for mol in molecules5:
        energies5.append(mol.info["energy"])
        # print(molecules[0].info['energy'])
    print(energies5)

    x5 = 0

    for i in energies5:
        x5 += 1

    print("the total number of the sixth position are " ,x5)
    print("the minimum in the position is " ,min(energies5))

    average5 = sum(energies5) / x5
    print('累加值', sum(energies5), '平均值', average5)

    energies6 = []
    for mol in molecules6:
        energies6.append(mol.info["energy"])
        # print(molecules[0].info['energy'])
    print(energies6)

    x6 = 0

    for i in energies6:
        x6 += 1

    print("the total number of the seventh position are ",x6)
    print("the minimum in the position is " ,min(energies6))

    average6 = sum(energies6) / x6
    print('累加值', sum(energies6), '平均值', average6)

    min_value = [min(energies), min(energies1), min(energies2), min(energies3), min(energies4), min(energies5),min(energies6)]
    print(min(min_value))

    energies_ = list(map(lambda x: x - min(min_value), energies))
    energies_1 = list(map(lambda x: x - min(min_value), energies1))
    energies_2 = list(map(lambda x: x - min(min_value), energies2))
    energies_3 = list(map(lambda x: x - min(min_value), energies3))
    energies_4 = list(map(lambda x: x - min(min_value), energies4))
    energies_5 = list(map(lambda x: x - min(min_value), energies5))
    energies_6 = list(map(lambda x: x - min(min_value), energies6))

    # energies = [x - min(min_value) for x in energies]
    # energies1 = [x - min(min_value) for x in energies1]
    # energies2 = [x - min(min_value) for x in energies2]
    # energies3 = [x - min(min_value) for x in energies3]
    # energies4 = [x - min(min_value) for x in energies4]
    # energies5 = [x - min(min_value) for x in energies5]
    # energies6 = [x - min(min_value) for x in energies6]

    print("----------------------first position----------------------")
    print(energies_)
    print("----------------------second position----------------------")
    print(energies_1)
    print("----------------------third position----------------------")
    print(energies_2)
    print("----------------------fourth position----------------------")
    print(energies_3)
    print("----------------------fifth position----------------------")
    print(energies_4)
    print("----------------------sixth position----------------------")
    print(energies_5)
    print("----------------------seventh position----------------------")
    print(energies_6)

    total_number_first = x
    total_number_second = x1
    total_number_third = x2
    total_number_fourth = x3
    total_number_fifth = x4
    total_number_sixth = x5
    total_number_seventh = x6

    k_B = 3.166811563 * 10 ** (-6)
    T = 298.15

    first = energies[:]
    second = energies1[:] 
    third = energies2[:]
    fourth = energies3[:]
    fifth = energies4[:]
    sixth = energies5[:]
    seventh = energies6[:]

    a = [math.exp(-(energyvalue / (k_B * T))) for energyvalue in first]
    b = [math.exp(-(energyvalue / (k_B * T))) for energyvalue in second]
    c = [math.exp(-(energyvalue / (k_B * T))) for energyvalue in third]
    d = [math.exp(-(energyvalue / (k_B * T))) for energyvalue in fourth]
    e = [math.exp(-(energyvalue / (k_B * T))) for energyvalue in fifth]
    f = [math.exp(-(energyvalue / (k_B * T))) for energyvalue in sixth]
    j = [math.exp(-(energyvalue / (k_B * T))) for energyvalue in seventh]

    a_1 = [np.sum(arr) for arr in [np.array(a)]]
    b_1 = [np.sum(arr) for arr in [np.array(b)]]
    c_1 = [np.sum(arr) for arr in [np.array(c)]]
    d_1 = [np.sum(arr) for arr in [np.array(d)]]
    e_1 = [np.sum(arr) for arr in [np.array(e)]]
    f_1 = [np.sum(arr) for arr in [np.array(f)]]
    j_1 = [np.sum(arr) for arr in [np.array(j)]]

    value1 = float("".join(map(str, a_1))) / total_number_first
    value2 = float("".join(map(str, b_1))) / total_number_second
    value3 = float("".join(map(str, c_1))) / total_number_third
    value4 = float("".join(map(str, d_1))) / total_number_fourth
    value5 = float("".join(map(str, e_1))) / total_number_fifth
    value6 = float("".join(map(str, f_1))) / total_number_sixth
    value7 = float("".join(map(str, j_1))) / total_number_seventh

    # a_value = float("".join(map(str, a_1)))/total_number_first
    # b_value = float("".join(map(str, b_1)))/total_number_second)
    # c_value = as_num(float("".join(map(str, c_1)))/total_number_third)
    # d_value = as_num(float("".join(map(str, d_1)))/total_number_fourth)
    # e_value = as_num(float("".join(map(str, e_1)))/total_number_fifth)
    # f_value = as_num(float("".join(map(str, f_1)))/total_number_sixth)
    # j_value = as_num(float("".join(map(str, j_1)))/total_number_seventh)

    print("first:", value1)
    print("second:", value2)
    print("third:", value3)
    print("fourth:", value4)
    print("fifth:", value5)
    print("sixth:", value6)
    print("seventh:", value7)

    arr = [value1, value2, value3, value4, value5, value6, value7]
    n = len(arr)
    ans = _sum(arr, n)
    print("the sum value is ", ans)

    p1_ = value1 / ans
    p2_ = value2 / ans
    p3_ = value3 / ans
    p4_ = value4 / ans
    p5_ = value5 / ans
    p6_ = value6 / ans
    p7_ = value7 / ans

    p1 = as_num((value1 / ans))
    p2 = as_num((value2 / ans))
    p3 = as_num((value3 / ans))
    p4 = as_num((value4 / ans))
    p5 = as_num((value5 / ans))
    p6 = as_num((value6 / ans))
    p7 = as_num((value7 / ans))

    untreated=[p1_,p2_,p3_,p4_,p5_,p5_,p6_,p7_]
    print("未处理",untreated)
    treated =[p1, p2, p3, p4, p5, p6, p7]
    print("处理后",treated)
    total=[x,x1,x2,x3,x4,x5,x6]
    print("each total",total)
    print("minimum value ",min(min_value))

    average_arr1= sum(average_arr)/len(average_arr)
    average_arr2 = [average - average_arr1, average1 - average_arr1, average2 - average_arr1, average3 - average_arr1,
                  average4 - average_arr1, average5 - average_arr1, average6 - average_arr1]

    print(np.abs(average_arr2))

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    positions = ('α', 'Β', 'γ', 'δ', 'ε', "ζ", "η")
    p_value = untreated

    plt.bar(positions, treated)
    plt.title('Every probability value')

    plt.show()

    average_arr = [average, average1, average2, average3, average4, average5, average6]
    print(average_arr)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    positions = ('α', 'Β', 'γ', 'δ', 'ε', "ζ", "η")

    plt.bar(positions, np.abs(average_arr2))
    plt.title('average value')

    plt.show()

    # plt.hist(spacer)
    # plt.title(file)
    # plt.show()
    break