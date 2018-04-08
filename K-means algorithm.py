import xlrd
import random
import numpy
import math

def compute_euclidean_distance(centroids):
	#------------------------Calculate distance from each centriod--------------------#
	for l in range(0,nclusters):
		for m in range(0,rows-1):
			distance[l][m] = math.sqrt((centroids[l][0] - X[m])**2 + (centroids[l][1] - Y[m])**2)
	
	print("\n\n\t\t\t\t\t<------------ Distance Table ----------->\n")
	for m in range(0,nclusters):
		print(distance[m])
	
def Assigning_to_clustors(distance):
	#----------------------------------Assigning to clustors---------------------------#

	for m in range(0,rows-1):
		small=distance[0][m]
		for l in range(1,nclusters):
			if small > distance[l][m]:
				small =  distance[l][m]
				for n in range(0,nclusters):
					clusters[n][m]=0
				clusters[l][m]=1
			else:
				for n in range(0,nclusters):
					clusters[n][m]=0
				clusters[0][m]=1
	print("\n\n\t\t\t\t<------------ Cluster Distribution Table ----------->\n")
	for m in range(0,nclusters):
		print(clusters[m])

def Calculating_Mean_centeriods():
	#----------------------------------Calculating Mean centeriods---------------------------#
	print("\n\n\t\t\t\t\t<------------ Centriods ----------->\n")
	for l in range(0,nclusters):
		SUMX = 0
		SUMY = 0
		count = 0
		for m in range(0,rows-1):
			if(clusters[l][m]==1):
				count=count+1
				SUMX=SUMX+X[m]
				SUMY=SUMY+Y[m]
		if count != 0:
			centroids[l][0]=SUMX/count
			centroids[l][1]=SUMY/count
		print("Centroid",l+1,": (",centroids[l][0]," , ",centroids[l][1]," )")
def Copy_cluster(temp_clusters,clusters):
	for l in range(0,nclusters):
		for m in range(0,rows-1):
			temp_clusters[l][m]=clusters[l][m]
	

#------------------------Reading Data from Excel file--------------------#
obj = xlrd.open_workbook("./selected.xlsx")
sheet = obj.sheet_by_index(0)
rows = sheet.nrows
X = sheet.col_values(1,1,rows)
Y = sheet.col_values(2,1,rows)
print("X = ",X)
print("Y = ",Y)
nclusters = eval(input("\nEnter the number of clusters you want to make: "))
#--------------------Creating arrays for storing calculations--------------------#
C = []
distance = [[0 for x in range(rows-1)] for y in range(nclusters)]
clusters = [[0 for x in range(rows-1)] for y in range(nclusters)]
centroids = [[0 for x in range(2)] for y in range(nclusters)]
temp_clusters = [[0 for x in range(rows-1)] for y in range(nclusters)]

#------------------Selecting random and unique centroids from list---------------#
num=1;
print("\n\n\n\n-----------------------------------------------Itteration Number : ",num," -------------------------------------------------")
print("\n\n\t\t\t\t\t<------------ Centriods ----------->\n")
C.append(random.randint(0,len(X)-1))
centroids[0][0]=X[C[0]]
centroids[0][1]=Y[C[0]]
print("\nCentroid 1 : (",X[C[0]]," , ",Y[C[0]]," )")

for i in range(1,nclusters):
	temp = random.randint(0,len(X)-1)
	if temp in C:
		C2 = random.randint(0,len(X)-1)
		while temp in C == 1:
			temp = random.randint(0,len(X)-1)
		C.append(temp)
		centroids[i][0]=X[C[i]]
		centroids[i][1]=Y[C[i]]
		print("Centroid",i+1,": (",centroids[i][0]," , ",centroids[i][1]," )")
	else:
		C.append(temp)
		centroids[i][0]=X[C[i]]
		centroids[i][1]=Y[C[i]]
		print("Centroid",i+1,": (",centroids[i][0]," , ",centroids[i][1]," )")

#------------------------Calculate distance from each centriod--------------------#
compute_euclidean_distance(centroids)
#----------------------------------Assigning to clustors---------------------------#
Assigning_to_clustors(distance)
#----------------------------------Calculating Mean centeriods---------------------------#
Calculating_Mean_centeriods()

num=num+1
print("\n\n\n\n-----------------------------------------------Itteration Number : ",num," -------------------------------------------------")
compute_euclidean_distance(centroids)

Copy_cluster(temp_clusters,clusters)

Assigning_to_clustors(distance)

while temp_clusters != clusters:
	print("\n\n\t\t\t\tThe cluster distribution is changed in last itteration")
	num=num+1
	print("\n\n\n\n-----------------------------------------------Itteration Number : ",num," -------------------------------------------------")
	Calculating_Mean_centeriods()
	compute_euclidean_distance(centroids)
	Copy_cluster(temp_clusters,clusters)
	Assigning_to_clustors(distance)
