#Ahmed A.Allam
import numpy as numb
import math
def MatrixMultiplication( MatrixA,MatrixB ):
   MatrixC=[]
   if len(MatrixA[0])==len(MatrixB):
     for h in range(len(MatrixA)):
        MatrixC.append([0] * len(MatrixB[0]))
     for i in range(len(MatrixA)):  
        for j in range (len(MatrixB[0])):
            for k in range(len(MatrixA[0])):
                MatrixC[i][j]=round(MatrixC[i][j]+MatrixA[i][k]*MatrixB[k][j], 4)
   print(MatrixC)
   return MatrixC

def MatrixMultiplicationNumpy( MatrixA,MatrixB):
   "This Function Calcualtes Matrix Multiplication of two matrices A and B the matrices are passed as a list of row by row elements if the are not matched it return a null array"
   MatrixC=None
   if MatrixA is not None and MatrixB is not None:
     if len(MatrixA[0])==len(MatrixB):
       A=numb.array(MatrixA)
       B=numb.array(MatrixB)
       MatrixC=A.dot(B)
   return MatrixC

def MatrixInverse( MatrixA):
   "This Function Calcualtes Matrix Inverse passed as a list of row by row elements if the are not matched it return a null array"

   A=numb.array(MatrixA)
   x=numb.linalg.det(A)
   if (x==0):
     MatrixC=None
   else:  
    MatrixC=numb.linalg.inv(MatrixA) 
   return MatrixC


def checkSquare(number):
    root = math.sqrt(number)
    if int( root+0.5 ) ** 2 == number:
        return True
    else:
        return False

#print (MatrixMultiplicationNotNummby([[1 ,0, 2],[2, 5, 6],[3, 7, 30]],[[1,2],[7,10],[9,60]]))
#print (MatrixMultiplication(MatrixInverse([[1 ,0, 2],[2, 5, 6],[3, 7, 30]]),[[1,2],[7,10],[9,60]]))

def PowerMethod(noOfIterations, Matrix, initialValues):
         eigenValue = []
         eigenVector = []
         for i in range(noOfIterations):
            eigenVector = MatrixMultiplication(Matrix, initialValues)
            print("Eigen vector before dividing is: ")
            print(eigenVector)
            eigenValue = max(eigenVector)
            newEigenVector = [[]]
            newEigenVector[0] = [round(x[0] /  eigenValue[0],4) for x in eigenVector]
            for i in range(len(newEigenVector[0])):
                  initialValues[i] = [newEigenVector[0][i]]
                  
            print("Eigen vector after dividing is: ")

            print(initialValues)
         initialValues.append(eigenValue)
         return initialValues
    
    
#PowerMethod(3, [[9, -1, 2], [-1,5,0], [2,0,5]], [[3], [0] ,[1]])
# print(numb.linalg.inv(numb.array([[7.0, 0.0, -2.0], [0.0, 3.0, 0.0], [-2.0, 0.0, 7.0]])))
# print(MatrixInverse([[7.0, 0.0, -2.0], [0.0, 3.0, 0.0], [-2.0, 0.0, 7.0]]))
# print(MatrixMultiplication([[0.1556, 0.0       ,  0.0444],
#  [0.0       ,  0.3333, 0.0        ],
#  [0.0444 ,0.0        , 0.1556]], [[0.1],[0.9],[0.09]]))
