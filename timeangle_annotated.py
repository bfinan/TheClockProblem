import re 															#import regexes
def isNumber(data):													#creating a function to check for only numeric characters
	try: return int(data)											#returns numeric characters as a string
	except ValueError: return False									#returns False for non-numeric characters
timefile = open("times.txt")										#Open the file
try:																
	for line in timefile:											#Read a line
		line=re.sub(':','',line)									#Remove colons
		time = isNumber(line)										#Check if numeric
		if(line):													#If so, begin extracting data
			if(100 <= time <= 2359):								#Check if time is within acceptable range
				if time >= 1200 : time -= 1200						#Set time from a zero value (for times greater than 12:00)
				mins = time % 100									#Get minutes value
				hours = time // 100									#Get hours value
				minpercent = mins * 0.016667 						#As an intermediate step, get the percentage of the hour passed
				minangle = minpercent * 360							#Get the angle between 0 and minute hand
				hourangle = hours * 30 + minpercent * 30			#Calculate angle between 0 and minute hand
				solution = abs(hourangle - minangle)				#Find one of the angles between the hands
				if solution > 180: solution = abs(solution - 360)	#If we got the bigger of the two, we calculate the smaller one
				print(solution)										#Print output
			else: print "ERROR"
		else: print "ERROR"
finally:
	timefile.close()												#Close the file