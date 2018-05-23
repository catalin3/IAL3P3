from ial3p3.inverse import Inverse

class LSE:
    def __init__(self, tomographList):
        self.__tomographList = tomographList
        w = len(tomographList)
        h = 385
        self.__x = [[0 for x in range(h)] for y in range(w)]
        self.__y = [0 for x in range(w)]

        for i in range(w):
            boneStructures = tomographList[i].getBoneStructures()
            airInclusions = tomographList[i].getAirInclusions()
            self.__x[i][0] = 1.0
            #print(self.__x[i][0])

            for contor in range(len(boneStructures)):
                self.__x[i][contor+1] = boneStructures[contor]

            for contor in range(len(airInclusions)):
                self.__x[i][contor+241] = airInclusions[contor]
                self.__y[i] = tomographList[i].getRelativeLocations()


    def compute(self):
        a = Inverse.invert(self.__x)
        return a
'''
public Matrix[] compute(){

        Matrix matrix_X=Matrix.from2DArray(X);

        Matrix transpose_X=matrix_X.transpose();
        Matrix matrix=transpose_X.multiply(matrix_X);
        double[][] array=new double[matrix.rows()][matrix.columns()];
        for(int i=0;i<matrix.rows();i++)
            for(int k=0;k<matrix.columns();k++)
                array[i][k]=matrix.get(i,k);
        Inverse.invert(array);
        Matrix multiply_X =Matrix.from2DArray(array);
        Matrix X_computation=multiply_X.multiply(transpose_X);

        return new Matrix[]{
                X_computation.multiply(Matrix.from1DArray(tomographList.size(),1,Y))
        };
    }
'''