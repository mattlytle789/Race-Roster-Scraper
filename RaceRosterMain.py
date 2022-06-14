import requests
from bs4 import BeautifulSoup
import xlwt
from xlwt import Workbook

# Accessing the data from the website
url = 'https://raceroster.com/events/2022/56070/the-2022-asics-falmouth-road-race/fundraising-organization/34911'
response = requests.get(url) # variable to hold the response to the request in a string
#print(response.text) ####DEBUGGING

# Creating the soup object for the html parser
htmlSoup = BeautifulSoup(response.text, 'html.parser')

# lists to hold the participants and their earnings
participantData = []
# ResultSet that hold all of the paragraph tags
pTags = htmlSoup.find_all('p')

# Filling the participants data into a list
individualsStartFlag = False # flag to signal the start of the list of individuals
for tag in pTags:
	#print(tag) ####DEBUGGING
	if (individualsStartFlag):
		participantData.append(tag.text)
	if (tag.text == 'Click on an individual below to make a donation.'):
		individualsStartFlag = True
	if (tag.text == ''):
		individualsStartFlag = False

# Splitting the participants and earnings 
index = 0 # variable to track what the index of he list is
names = [] # lsit of the participants names
earnings = [] # list of the participants earnings
for data in participantData:
	if (index%2 == 0): # if the index is a name cell
		if (data != ''):
			names.append(data)
	else: # if the index is an earnings cell
		if (data != ''):
			earnings.append(data[9:])
	index+=1

# writing data to an excel file
excelFile = Workbook()
sheet1 = excelFile.add_sheet('Sheet1')
for i in range(0,len(names)):
	sheet1.write(i,0,names[i])
	sheet1.write(i,1,earnings[i])
excelFile.save('RaceRosterData.xls')
# creating a dictionary with the participants and earnings
#participantDict = {}
#for i in range(0,len(names)):
#	participantDict[names[i]] = int(earnings[i])

####DEBUGGING
#print(participantData)
#print(names)
#print(earnings)
#print(participantDict)
