import csv
import numpy as np

#background:

#Massive online classes have allowed for distributed experimentation into what practices
#optimize students’ learning. Coursera, a free online education platform that started at Stanford,
#is testing out new ways of teaching a concept in probability. They have two different learning
#activities activity1 and activity2 and they want to figure out which activity leads to
#better learning outcomes. After interacting with a learning activity Coursera evaluates a
#student’s learning outcome by asking them to solve a set of questions.
#Over a two-week period, Coursera randomly assigns each student to either be given activity1
#(group A), or activity2 (group B). The activity that is shown to each student and the student’s
#measured learning outcomes can be found in the file learningOutcomes.csv.

#TASK:
#calculate the difference and p-value of the sample mean of activity1 and activity2
#Also do this for people of different level of backgrounds

def main():
	learningOutcomes = loadLearningOutcomes()
	backgrounds = loadBackgrounds()
	catelist = findingCategorylist(backgrounds,learningOutcomes,'more')
	mean1_more = calculatesamplemean('activity1',catelist)
	mean2_more = calculatesamplemean('activity2',catelist)
	print("p value for more" )
	print(pvalue_bootstrap(getSize('activity1',catelist),getSize('activity1',catelist),abs(mean1_more - mean2_more),catelist))
	print("mean difference for more")
	print(abs(mean1_more - mean2_more))
	print(" ")


	catelistless = findingCategorylist(backgrounds,learningOutcomes,'less')
	mean1_less = calculatesamplemean('activity1',catelistless)
	mean2_less = calculatesamplemean('activity2',catelistless)
	print("p value for less" )
	print(pvalue_bootstrap(getSize('activity1',catelistless),getSize('activity1',catelistless),abs(mean1_less - mean2_less),catelistless))
	print("mean difference for less")
	print(abs(mean1_less - mean2_less))
	print(" ")

	catelistave = findingCategorylist(backgrounds,learningOutcomes,'average')
	mean1_ave = calculatesamplemean('activity1',catelistave)
	mean2_ave = calculatesamplemean('activity2',catelistave)
	print("p value for average" )
	print(pvalue_bootstrap(getSize('activity1',catelistave),getSize('activity1',catelistave),abs(mean1_ave - mean2_ave),catelistave))
	print("mean difference for average")
	print(abs(mean1_ave - mean2_ave))
	print(" ")
	mean1 = calculatesamplemean('activity1',learningOutcomes)
	mean2 = calculatesamplemean('activity2',learningOutcomes)

	print("Sample mean difference part a")
	print(abs(mean1 - mean2))

	pvalue = pvalue_bootstrap(542,510,abs(mean1-mean2),learningOutcomes)
	print("pvalue for part a")
	print(pvalue)

def getSize(keyword, list):
	count = 0
	for ele in list:
			if(keyword == ele[1]):
				count += 1
	return count


def calculatesamplemean(activity,olist):
	count = 0.0
	summ = 0.0
	for element in olist:
		if(element[1] == activity):
			count += 1
			summ += element[2]
	return summ/(count);

def calmeandifference(sample1,sample2):
	count1 = 0.0
	sum1 = 0.0
	for element in sample1:
		sum1 += element
		count1 += 1
	mean1 = sum1/count1

	count2 = 0.0
	sum2 = 0.0
	for element in sample2:
		sum2 += element
		count2 += 1

	mean2 = sum2/count2
	return abs(mean2-mean1)

#bootstrapping, calculating the p value of the difference of randomly choosing two samples from the original sample space	
def pvalue_bootstrap(n, m, diff, samplelist):
	count_extreme = 0.0
	datalist = []
	for element in samplelist:
		datalist.append(element[2])
	
	for i in range(10000):
		resample1 = np.random.choice(datalist,n)
		resample2 = np.random.choice(datalist,m)
		#randomly choosing two samples
		new_diff = calmeandifference(resample1,resample2)

		#compare if the difference is greater than original difference
		if new_diff >= diff:
			count_extreme += 1 

	return count_extreme/10000


#Calculte the difference in means of categories: more experience, average experience and less experience
def findingCategorylist(bglist, resultlist, keyword):
	findlist = []
	for element in bglist:

		if(element[1] == keyword):
			
			for ele in resultlist:
				if(ele[0] == element[0]):
					findlist.append(ele)
	return findlist



# Example loading for the problem on A/B testing.
# Returns a list of student data. Each student is a list
# with three elements: their id, their activity and their 
# learning outcome.
def loadLearningOutcomes():
	reader = csv.reader(open('learningOutcomes.csv'))
	learningOutcomes = []
	for row in reader:
		studentId = row[0]
		activity = row[1]
		outcome = float(row[2]) # make sure outcome is a number!
		learningOutcomes.append([studentId, activity, outcome])
	return learningOutcomes


# Example loading for the problem on A/B testing.
# Returns a list of student backgrounds. Each student is a list
# with two elements: their id, their background.
def loadBackgrounds():
	reader = csv.reader(open('background.csv'))
	learningOutcomes = []
	for row in reader:
		learningOutcomes.append(row)
	return learningOutcomes


# Example code for looping over a list in python. This 
# function prints out the list
def outputList(l):
	for row in l:
		print(row)
	print('\n----\n')


if __name__ == '__main__':
	main()
