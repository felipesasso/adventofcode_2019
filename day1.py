from utils import get_filename_from_arg

def get_fuel_requirements(filename):
    with open(filename) as file:
        fuel = sum(map(lambda x: (int(x) // 3) - 2, file.read().split()))

    return fuel

if __name__ == '__main__':
    filename = get_filename_from_arg()
    print(get_fuel_requirements(filename))
