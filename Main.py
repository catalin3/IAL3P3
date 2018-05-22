
from ial3p3.tomograph import Tomograph
from ial3p3.controller import read_from_csv, leastSquare

def main():
    tm = Tomograph(1, 1, 1, 1)
    path = "slice_localization_data.csv"
    #read_from_csv(path)
    leastSquare(path)

if __name__ == '__main__':
    main()