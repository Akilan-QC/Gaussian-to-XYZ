import pandas as pd


def atomic_name(nb_list):
    """
    Return the atomic symbol as a list using a list of atomic number
    """
    table_path = "PT.csv"
    df = pd.read_csv(table_path)
    atm_list = []
    for atom in range(len(nb_list)):
        line = df[df["AtomicNumber"] == int(nb_list[atom])]
        atm_list.append(str(line['Symbol'].values[0]))
    return atm_list




file_open = open(input(), 'r')
a = file_open.readlines()
file_open.close()



d = []
e = []
coord = []
atomic_Number = []
No_Atoms = []
for lines in a:
    if "NAtoms" in lines:
        No_Atoms.append(lines.split())
total_line = int(No_Atoms[0][1])


def standard_orientation():
    line_start = 0
    line_end = 0
    copy = False
    for lines in a:
        line_start += 1
        if "Standard orientation:" in lines != []:
            d.append(line_start)

        line_end += 1

    global count
    count = 0

    for b in a:
        if "Standard orientation:" in b != []:
            count += b.count("Standard orientation:")

    start = 0

    for line_1 in a:

        start += 1

        if "Standard orientation:" in line_1 and start == d[count-1]:
            copy = True
        if start == d[count-1] + total_line+5:
            copy = False
        elif copy:
            new_line = line_1.split()[3:]
            atomic_Number.append(int(line_1.split()[1]))
            coord.append(new_line)


def input_orientation():
    line_start = 0
    line_end = 0
    copy = False
    for lines in a:
        line_start += 1
        if "Input orientation:" in lines != []:
            d.append(line_start)

        line_end += 1


    global count

    count = 0

    for b in a:
        if "Input orientation:" in b != []:
            count += b.count("Input orientation:")

    start = 0

    for line_1 in a:

        start += 1

        if "Input orientation:" in line_1 and start == d[count-1]:
            copy = True
        if start == d[count-1] + total_line+5:
            copy = False
        elif copy:
            new_line = line_1.split()[3:]
            coord.append(new_line)
            try:
                atomic_Number.append(int(line_1.split()[1]))
            except:
                pass


counter_1 = 0
counter_value = []
for counter_lines in a:
    if "Standard orientation:" in counter_lines:
        counter_1 +=1
        counter_value.append(int(counter_1))

if counter_value == []:
    input_orientation()
else:
    standard_orientation()


final_coord = coord[5:]

coord_number = 0


output_list = atomic_name(atomic_Number)
print(total_line)
print("")
for fc in final_coord:

    (print("{0:>2} {1:>11} {2:>11} {3:>11}".format(
        output_list[coord_number], fc[0], fc[1], fc[2])))
    coord_number += 1
