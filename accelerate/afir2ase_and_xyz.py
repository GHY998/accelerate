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
            
            i=1
            while not re.search("Energy", file_content[line_index + i]):
                atom,x,y,z = file_content[line_index + i].split()
                mol.append(Atom(atom,(x,y,z)))
                i=i+1
               
            num_atoms = i-1

            m = re.match(r'Energy    = (?P<energy>.*) \((?P<energy2>.*) :    (?P<someconst>.*)\)', file_content[line_index + num_atoms + 1])
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
#all_files = glob.glob("../files/*/*/*.log")
all_files = glob.glob("../files/*/*/*.log")

molecules = eq_list_to_xyz(all_files[0], 'test.xyz')

print(molecules[0].info['energy'])
