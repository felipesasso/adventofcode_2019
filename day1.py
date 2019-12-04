from utils import get_filename_from_arg, get_int_list_from_file

def get_total_fuel_fuel_requirements(mass_list):
    return sum(map(get_fuel_fuel_requirements, mass_list))

def get_fuel_fuel_requirements(mass):

    requirements = 0
    if mass <= 0:
        raise ValueError('Mass must be a positive number')

    while True:
        mass = get_rocket_fuel_requirements(mass)
        if mass <= 0:
            return requirements
        requirements += mass

def get_rocket_fuel_requirements(mass):
    if type(mass) != int:
        if not mass.is_digit():
            raise ValueError('Mass must be a digit!')
            mass = int(mass)
    if mass <= 0:
        raise ValueError('Mass must be a positive number')
    return (mass // 3) - 2

def get_total_fuel_requirements(mass_list):
    return sum(map(get_rocket_fuel_requirements, mass_list))

def get_total_fuel_requirements_from_file(filename):
    list_ = get_int_list_from_file(filename)
    return get_total_fuel_requirements(list_)

def get_total_fuel_fuel_requirements_from_file(filename):
    list_ = get_int_list_from_file(filename)
    return get_total_fuel_fuel_requirements(list_)

if __name__ == '__main__':
    filename = get_filename_from_arg()
    print('Part 1: {}'.format(get_total_fuel_requirements_from_file(filename)))
    print('Part 2: {}'.format(get_total_fuel_fuel_requirements_from_file(filename)))
