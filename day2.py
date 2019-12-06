import copy
from utils import get_filename_from_arg, get_int_list_from_file


def calc_instruction(opcode, position, codes_list):
    source_1 = codes_list[position+1]
    source_2 = codes_list[position+2]
    dest_pos = codes_list[position+3]
    if opcode == 1:
        codes_list[dest_pos] = \
            codes_list[source_1] + \
            codes_list[source_2]
    if opcode == 2:
        codes_list[dest_pos] = \
            codes_list[source_1] * \
            codes_list[source_2]

    return codes_list


def restore_gravity_assist_program(num1, num2, codes_list):
    codes_list[1] = num1
    codes_list[2] = num2
    for index in range(0, len(codes_list), 4):
        opcode = codes_list[index]
        if opcode == 99:
            break
        codes_list = calc_instruction(opcode, index, codes_list)

    return codes_list[0]

def find_noun_verb(codes_list, value):
    for i in range(100):
        for j in range(100):
            new_list = copy.copy(codes_list)
            if restore_gravity_assist_program(i, j, new_list) == value:
                print(100 * i + j)
                return i, j

    return None, None


if __name__ == '__main__':
    filename = get_filename_from_arg()
    codes_list = get_int_list_from_file(filename=filename, sep=',')
    new_list = copy.deepcopy(codes_list)
    print(restore_gravity_assist_program(12, 2, new_list))
    print(find_noun_verb(codes_list, 19690720))
