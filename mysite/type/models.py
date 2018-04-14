from django.db import models
import statistics
import string

class Info(models.Model):
    author = models.CharField(max_length = 200)
    charLib = models.TextField()
    timeLib = models.TextField()
    def publish(self):
        self.save()

    def __str__(self):
        return self.author
		
class Summary(models.Model) :
	newID = models.TextField()
	author = models.TextField()
	comboListText = models.TextField();
	medListText =  models.TextField();
	def getData(obj):
		newId = obj.id
		infoObject = obj
		comboList = ""
		medList = ""
		try:
			
			charDict = infoObject.charLib.split(",")
			intDict = infoObject.timeLib.split(",")
					
			totalSentence = ""
			for i in range(len(charDict)):
				totalSentence += charDict[i]
				
			#print(totalSentence)

			listOfTuples = []
			#cycle all letters
			for i in ([""]+list(string.ascii_lowercase)):
				for j in ([""]+list(string.ascii_lowercase)):
					for k in (list(string.ascii_lowercase)):
						for l in (list(string.ascii_lowercase)):
							tuple = i+j+k+l
							#print(tuple)
							if(tuple not in listOfTuples):
								
								if tuple in totalSentence.lower():
								
									allTimes = []
									for m in range(len(totalSentence)-len(tuple)):
										pTuple = ""
										for n in range(len(tuple)):
											pTuple += totalSentence[(m+n)].lower()
										if (pTuple == tuple):
											allTimes.append(float(intDict[(m+len(tuple)-1)])-float(intDict[(m)]))
											
									#ADD IT TO FILE
									if (len(allTimes)>=4 and (len(tuple)>2)):
										listOfTuples.append(tuple)
										print(tuple,len(allTimes),statistics.mean(allTimes),statistics.median(allTimes), statistics.variance(allTimes))
										comboList += str(tuple)+", "
										medList += str(str(statistics.median(allTimes)))+", "
								#The entire sentence of what they wrote
								#list of every appearances, time for each
		except(AttributeError):	
			pass
		#print(comboList)
		#print(medList)
		return(comboList,medList,newId)
	def publish(self):
		self.save()
	def __str__(self):
		return self.author
		
class Applying(models.Model):
	author = models.CharField(max_length = 200)
	charLib = models.TextField()
	timeLib = models.TextField()
	def allHaveIt(tuple,list):
		if(not tuple[0] == " "):
			tuple = " "+tuple
		flag = False
		count = 0
		
		for file in list:
			first = 0
			for tupleC in file.comboListText.split(","):
				if(first == 0):
					tupleC = " "+tupleC
				if(tupleC == tuple):
					count += 1
				first+=1
		if(count == len(list)):
			flag = True
		print(tuple, flag)
		return flag
	def getMostUniqueCombo(name, list):
		print(name)
		print("List of People: ", list)#FIXME
		megaList = []
		compareList = []
		flag = True #print if name is not in list.
		comboList,medList,newId = Summary.getData(name)
		for line in comboList.split(","):
			if(not line[0] == " "):
				line = " "+line
			compareList.append(line)
			flag = False 
		file = comboList.split(",")
		for line in file:
			if(not line[0] == " "):
				line = " "+line
			if(Applying.allHaveIt(line,list) and len(line)>1 and not line in megaList):
				megaList.append(line)
			
		#Have the list of possible tuples
		tupleList = []
		for tuple in megaList:
			#print("IN MEGALIST")
			num = 0
			for t in range(len(comboList.split(","))):
				tuple2 = comboList.split(",")[t]
				if(t==0):
					tuple2=" "+tuple2
				if(tuple2 == tuple):
					num = medList.split(",")[t]
			
			peoplediff=[]		
			for person in list:
				for t in range(len(person.comboListText.split(","))):
					tuple2 = person.comboListText.split(",")[t]
					if(t==0):
						tuple2=" "+tuple2
					if(tuple2 == tuple):
						num1 = person.medListText.split(",")[t]
						#print(person, tuple, num1)
						peoplediff.append(abs(float(num1) - float(num)))
			dict = {}
			dict['name'] = tuple
			peoplediff = sorted(peoplediff)
			try:
				dict['diff'] = min(peoplediff[1:])
			except:
				dict['diff'] = min(peoplediff)
			print(tuple, peoplediff)
			tupleList.append(dict)
			

		newlist = sorted(tupleList, key=lambda k: k['diff'], reverse = True)
		print(newlist)
		returnList = [newlist[0]['name'],newlist[1]['name'],newlist[2]['name']]
		#print("this is what is returning", returnList)
		return(returnList)
	def getSentences(comboList):
		returnList = ""
		for combo in comboList:
			if(combo == " all"):
				returnList+=("last fall i called the tall man in the hall of the mall. ")
			elif(combo == " the"):
				returnList+=("together, they are the only other group out there. ")
			elif(combo == " and"):
				returnList+=("I hand stand on the land that is grand and not an island. ")
			else:
				returnList+=(combo)
		return (returnList)
	def whatTime(user, tuple,comboList,medList):
		
		i = 0
		for tuple1 in comboList.split(","):
			if(tuple1 == tuple):
				return(medList.split(",")[i])
			else:
				i+=1
		return(0)
	def getAnswer(user, list):
		comboList,medList,newId = Summary.getData(user)
		listOfWords = Applying.getMostUniqueCombo(user,list)
		personList = []
		for obj in list:
			dict = {}
			score = 0
			for tuple in listOfWords:
				timesList = (obj.medListText.split(","))
				combosList = (obj.comboListText.split(","))
				for i in range(len(timesList)):
					if combosList[i] == tuple:
						score+=abs(float(timesList[i])-float(Applying.whatTime(user,tuple,comboList,medList)))
			dict['name'] = obj.author
			dict['obj'] = obj
			dict['score'] = score
			personList.append(dict)
		newlist = sorted(personList, key=lambda k: k['score'], reverse = False)
		M = 0
		print(newlist)
		print(ApplyingAs.objects.last())
		for i in newlist:
			if (i['name']==ApplyingAs.objects.last().choice):
				break
			M+=1
		
		if(newlist[M]['score']<300):#For ms
			return("You are "+ newlist[M]['name'])
		else:
			return("Try Again")
	def publish(self):
		self.save()
	def __str__(self):
		return self.author
		
class ApplyingAs(models.Model):
	NAMES = [(n.author, n.author) for n in Summary.objects.all()]
	choice = models.CharField(max_length = 100)
	
	def __str__(self):
		return self.choice