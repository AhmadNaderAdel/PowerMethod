import operations
import tkinter as tk
from tkinter import ttk
import math
root = tk.Tk()
root.title("Power Method")
root.geometry("600x700")
#label = ttk.Label(root, text = "Why are you being weird")
#label.grid(row = 1, column = 1)
fields = []


#Enter your initial values label
label1 = ttk.Label(root, text = "Enter the initial values:(seperate numbers by a space)")
label1.grid(row = 0, column = 0, sticky='W')

#Initial Values
initValues = ttk.Entry(root, width = 25)
initValues.grid(row = 1, column = 0, sticky='W')
sep2 = ttk.Separator(root,orient='vertical')

#Enter the number of iterations
label2 = ttk.Label(root, text = "Enter the number of iterations:")
label2.grid(row = 2, column = 0, sticky='W')

#Initial Values
iterations = ttk.Entry(root, width = 5)
iterations.grid(row = 3, column = 0, sticky='W')



#Enter your matrix:
label3 = ttk.Label(root, text = "Enter your square matrix:")
label3.grid(row = 4, column = 0, sticky='W')

label4 = ttk.Label(root, text = "(Enter the numbers in the form of an array where numbers are seperated by a space)")
label4.grid(row = 5, column = 0, sticky='W')


#Matrix 
matrix = tk.Text(root ,width=40, height = 10)
matrix.grid(row = 6, column = 0, sticky = 'W')
lengthy = 7
def calculateHighest():
    global iterations, matrix, initValues
    try:
        noOfIterations = iterations.get()
        matrixOfNumbers = matrix.get('1.0', "end")
        initial = initValues.get().split()
        initialMatrix = [[float(x)] for x in initial]
    #print(initialMatrix)
    #print(noOfIterations + " " + matrixOfNumbers + " " + initial)    
        array = matrixOfNumbers.split()
        intArray = [float(item) for item in array]
        if not (noOfIterations and matrixOfNumbers and initial) or array == []:
            errorWindow = tk.Toplevel()
            errorLabel = ttk.Label(errorWindow, text = "Make sure all the fields have input")
            okButton = ttk.Button(errorWindow, text = "Ok", command = errorWindow.destroy)
            errorLabel.pack()
            okButton.pack()
            return     
        if operations.checkSquare(len(intArray)):
            dimension = int(math.sqrt(len(intArray)))
            TwoDArray = [[None for x in range(dimension)] for y in range(dimension)]
            if dimension != len(initialMatrix):
                errorWindow = tk.Toplevel()
                errorLabel = ttk.Label(errorWindow, text = "No of Matrix columns must match no of row in initial values")
                okButton = ttk.Button(errorWindow, text = "Ok", command = errorWindow.destroy)
                errorLabel.pack()
                okButton.pack()
                return   
            #print(TwoDArray)
            counter = 0
            #x = [[foo for i in range(10)] for j in range(10)]
            for i in range(0,dimension ):
                for j in range(0, dimension) :
                    #print("row is " + str(i) + " column is "+ str(j))
                    TwoDArray[i][j] = intArray[counter]  #intArray[counter]
                    counter += 1
            #print(" Matrix is sent to the Power Method function like this: ")
            #print(TwoDArray)
            #print(TwoDArray)
            result = operations.PowerMethod(int(noOfIterations), TwoDArray , initialMatrix)
            
            
            resultWindow = tk.Toplevel()
            resultWindow.title("Result")
            resultWindow.geometry("200x200")
            
            eigenVectorLabel = tk.Label(resultWindow, text = "eigenvector is ")
            eigenVectorLabel.grid(row = 0, column = 0)
            firstAvailableLength = 1
            for i in range(len(result)-1):
                #print(result[i])
                newLabel = tk.Label(resultWindow, text = str(result[i]))  
                newLabel.grid(row = firstAvailableLength, column = 0)
                firstAvailableLength += 1        

            newLabel = tk.Label(resultWindow, text = "eigenvalue is ")
            newLabel.grid(row = firstAvailableLength, column = 0)
            firstAvailableLength += 1
            newLabel = tk.Label(resultWindow, text = str(result[len(result)-1]))
            newLabel.grid(row = firstAvailableLength, column = 0)
            firstAvailableLength += 1
            
            
            okButton = ttk.Button(resultWindow, text = "Ok", command = resultWindow.destroy)
            
            okButton.grid(row = firstAvailableLength, column = 0)
            
            
            
        
        else:
            errorWindow = tk.Toplevel()
            errorLabel = ttk.Label(errorWindow, text = "please you enter a square matrix")
            okButton = ttk.Button(errorWindow, text = "Ok", command = errorWindow.destroy)
            errorLabel.pack()
            okButton.pack()
            return 
            
    except:
        #failure code
        errorWindow = tk.Toplevel()
        errorLabel = ttk.Label(errorWindow, text = "please make sure you enter only numbers")
        okButton = ttk.Button(errorWindow, text = "Ok", command = errorWindow.destroy)
        errorLabel.pack()
        okButton.pack()
        return 
def clearWindow(window):
    window.destroy()

def calculateLowest():
    global iterations, matrix, initValues
    try:
        noOfIterations = iterations.get()
        matrixOfNumbers = matrix.get('1.0', "end")
        initial = initValues.get().split()
        initialMatrix = [[float(x)] for x in initial]
    #print(initialMatrix)
    #print(noOfIterations + " " + matrixOfNumbers + " " + initial)    
        array = matrixOfNumbers.split()
        intArray = [float(item) for item in array]
        if not (noOfIterations and matrixOfNumbers and initial) or array == []:
            errorWindow = tk.Toplevel()
            errorLabel = ttk.Label(errorWindow, text = "Make sure all the fields have input")
            okButton = ttk.Button(errorWindow, text = "Ok", command = errorWindow.destroy)
            errorLabel.pack()
            okButton.pack()
            return     
        if operations.checkSquare(len(intArray)):
            dimension = int(math.sqrt(len(intArray)))
            TwoDArray = [[None for x in range(dimension)] for y in range(dimension)]
            if dimension != len(initialMatrix):
                errorWindow = tk.Toplevel()
                errorLabel = ttk.Label(errorWindow, text = "No of Matrix columns must match no of row in initial values")
                okButton = ttk.Button(errorWindow, text = "Ok", command = errorWindow.destroy)
                errorLabel.pack()
                okButton.pack()
                return   
            #print(TwoDArray)
            counter = 0
            #x = [[foo for i in range(10)] for j in range(10)]
            for i in range(0,dimension ):
                for j in range(0, dimension) :
                    #print("row is " + str(i) + " column is "+ str(j))
                    TwoDArray[i][j] = intArray[counter]  #intArray[counter]
                    counter += 1
            #print(" Matrix is sent to the Power Method function like this: ")
            #print(TwoDArray)
            TwoDArray = operations.MatrixInverse(TwoDArray)
            #print(TwoDArray)
            result = operations.PowerMethod(int(noOfIterations), TwoDArray , initialMatrix)
            
            
            resultWindow = tk.Toplevel()
            resultWindow.title("Result")
            resultWindow.geometry("200x200")
            
            eigenVectorLabel = tk.Label(resultWindow, text = "eigenvector is ")
            eigenVectorLabel.grid(row = 0, column = 0)
            firstAvailableLength = 1
            for i in range(len(result)-1):
                #print(result[i])
                newLabel = tk.Label(resultWindow, text = str(result[i]))  
                newLabel.grid(row = firstAvailableLength, column = 0)
                firstAvailableLength += 1        

            newLabel = tk.Label(resultWindow, text = "eigenvalue is ")
            newLabel.grid(row = firstAvailableLength, column = 0)
            firstAvailableLength += 1
            newLabel = tk.Label(resultWindow, text = str(result[len(result)-1]))
            newLabel.grid(row = firstAvailableLength, column = 0)
            firstAvailableLength += 1
            
            
            okButton = ttk.Button(resultWindow, text = "Ok", command = resultWindow.destroy)
            
            okButton.grid(row = firstAvailableLength, column = 0)
            
            
            
        
        else:
            errorWindow = tk.Toplevel()
            errorLabel = ttk.Label(errorWindow, text = "please you enter a square matrix")
            okButton = ttk.Button(errorWindow, text = "Ok", command = errorWindow.destroy)
            errorLabel.pack()
            okButton.pack()
            return 
            
    except:
        #failure code
        errorWindow = tk.Toplevel()
        errorLabel = ttk.Label(errorWindow, text = "please make sure you enter only numbers")
        okButton = ttk.Button(errorWindow, text = "Ok", command = errorWindow.destroy)
        errorLabel.pack()
        okButton.pack()
        return 

#calculate largest eigen pair
calculateLargest = tk.Button(root, text = "Calculate largest eigen pair ", command = calculateHighest)
calculateLargest.grid(row = 7, column = 0, sticky = 'W')

#calculate smallest eigen pair
calculateSmallest = tk.Button(root, text = "Calculate Smallest eigen pair", command = calculateLowest)
calculateSmallest.grid(row = 8, column = 0, sticky = 'W')
root.mainloop()


 