
from ial3p3.tomograph import Tomograph
from ial3p3.controller import read_from_csv, leastSquare, evolutiveAlgorithm, descentGradient

def main():
    path = "slice_localization_data.csv"
    #path = "test"
    #read_from_csv(path)
    leastSquare(path)
    #evolutiveAlgorithm(path)
    #descentGradient(path)
if __name__ == '__main__':
    main()