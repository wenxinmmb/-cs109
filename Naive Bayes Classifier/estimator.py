
import csv
import numpy as np
import math

def main():
	with open('heart-train.txt') as infile:
		line_num = 1
		intput_var = 0
		data_size = 0
		array0 = []
		array1 = []
		array0.append(0)
		array1.append(0)
		class_size = 2

		#reading training data set
		for line in infile:
			data = line.split();

			if(line_num == 1):
				data = line.split();
				intput_var = int(data[0])
			
			elif(line_num == 2):
				data = line.split()
				data_size = int(data[0])
				for k in range(intput_var):
					array0.append(0)
					array1.append(0)

			else:
				data = line.split(':')
				features = line.split()
				features[intput_var-1] =features[intput_var-1][:1] 
				#print(features)
				classt = int(data[1])
				
				if (classt == 0):
					array0[0] += 1
					for k in range(intput_var):
						array0[k+1] += int(features[k])
				
				elif (classt == 1):
					array1[0] += 1
					for k in range(intput_var):
						array1[k+1] += int(features[k])
			line_num += 1
			
			
		P_y0 = float(array0[0])/data_size
		P_y1 = float(array1[0])/data_size
		

		naive_0 = []
		naive_1 = []
		for kk in range(intput_var):
			naive_0.append(0)
			naive_1.append(0)
			naive_0[kk] = float(array0[kk+1]) /array0[0]
			naive_1[kk] = float(array1[kk+1]) /array1[0]

		processTestData('heart-test.txt', P_y0, P_y1, naive_0, naive_1,array0,array1)

#Processing testing data set, using naive bayes assumption that each feather is independent conditioned on the class
def processTestData(file, y0, y1, l0, l1,la0,la1):
	metadata =[]
	correct = 0
	wrong = 0
	c1 = 0
	w1 = 0
	c2 = 0
	w2 = 0
	with open(file) as infile:
		line_num = 1
		intput_var = 0
		data_size = 0
		array0 = []
		array1 = []
		class_size = 2

		for line in infile:
			data = line.split();

			if(line_num == 1):
				data = line.split();
				intput_var = int(data[0])
			
			elif(line_num == 2):
				data = line.split()
				data_size = int(data[0])
				for k in range(intput_var):
					array0.append(0)
					array1.append(0)

			else:
				data = line.split(':')
				features = line.split()
				features[intput_var-1] =features[intput_var-1][:1] 

				
				answer = int(data[1])
				testdata =[]
				for ii in range(intput_var):
					testdata.append(int(features[ii]))
				
				result = Maximumlikely(y0,y1,l0,l1,testdata)
				#result = Laplace(y0,y1,la0,la1,testdata) #switching to this when using laplace

				if(result == answer):
					correct += 1
					if(answer == 0):
						c1 += 1
					else:
						c2 +=1

				else:
					wrong += 1
					if(answer == 1):
						w1 += 1
					else:
						w2 +=1
		
			line_num += 1
	print("Class 0: tested")
	print(c1+w1)
	print("correct:" )
	print(c1)
	print("Class 1: tested")
	print(c2+w2)

	print("correct:" )
	print(c2)

	print("correct: ")
	print(correct)
	print("wrong: ") 
	print( wrong)

	print("Accuracy:")
	print(float(correct)/(correct+wrong))
	return 

#Maximum likelyhood estimator as prior
def Maximumlikely(p_y0, p_y1, list0, list1,testdata):
 	prob0 = np.log(p_y0)
 	prob1 = np.log(p_y1)

 	for index in range(len(testdata)):
 		if(testdata[index] == 1):
 			prob0 += np.log(list0[index])
 			prob1 += np.log(list1[index])
 		else:
 			prob0 += np.log(1 - list0[index])
 			prob1 += np.log(1 - list1[index])

 	if(prob0 > prob1):
 		return 0
 	else:
 		return 1
#Laplace estimator as prior
def Laplace(p_y0, p_y1, list0, list1,testdata):
 	prob0 = np.log(p_y0)
 	prob1 = np.log(p_y1)

 	for index in range(len(testdata)):
 		if(testdata[index] == 1):
 			prob0 += np.log(float(list0[index+1]+1.0)/(list0[0]+2.0))
 			prob1 += np.log(float(list1[index+1]+1.0)/(list1[0]+2.0))
 		else:
 			prob0 += np.log(float(list0[0]-list0[index+1]+1.0)/(list0[0]+2.0))
 			prob1 += np.log(float(list1[0]-list1[index+1]+1.0)/(list1[0]+2.0))

 	if(prob0 > prob1):
 		return 0
 	else:
 		return 1

if __name__ == '__main__':
	main()