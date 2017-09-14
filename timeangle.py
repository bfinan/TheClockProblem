import re
def isNumber(data):
	try: return int(data)
	except ValueError: return False
timefile = open("times.txt")
try:
	for line in timefile:
		line=re.sub(':','',line)
		time = isNumber(line)
		if(line):
			if(100 <= time <= 2359):
				if time >= 1200 : time -= 1200
				mins = time % 100
				hours = time // 100
				minpercent = mins * 0.016667 
				minangle = minpercent * 360
				hourangle = hours * 30 + minpercent * 30
				solution = abs(hourangle - minangle)
				if solution > 180: solution = abs(solution - 360)
				print(solution)
			else: print "ERROR"
		else: print "ERROR"
finally:
	timefile.close()