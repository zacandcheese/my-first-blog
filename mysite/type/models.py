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
				
			print(totalSentence)

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
									if len(allTimes)>=3:
										listOfTuples.append(tuple)
										print(tuple,len(allTimes),statistics.mean(allTimes),statistics.median(allTimes), statistics.variance(allTimes))
										comboList += str(tuple)+", "
										medList += str(str(statistics.median(allTimes)))+", "
								#The entire sentence of what they wrote
								#list of every appearances, time for each
		except(AttributeError):	
			pass
		print(comboList)
		print(medList)
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
			for tupleC in file.comboListText.split(","):
				if(tupleC == tuple):
					count += 1
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
			num = 0
			for t in range(len(comboList.split(","))):
				if(comboList.split(",")[t] == tuple):
					num = medList.split(",")[t]
			peoplediff=[]		
			for person in list:
				for t in range(len(person.comboListText.split(","))):
					if(person.comboListText.split(",")[t] == tuple):
						num1 = person.medListText.split(",")[t]
						#print(person, tuple, num1)
						peoplediff.append(abs(float(num1) - float(num)))
			dict = {}
			dict['name'] = tuple
			dict['diff'] = min(peoplediff)
			tupleList.append(dict)

		newlist = sorted(tupleList, key=lambda k: k['diff'], reverse = True)
		#print(newlist)
		returnList = [newlist[0]['name'],newlist[1]['name'],newlist[2]['name']]
		print("this is what is returning", returnList)
		return(returnList)
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
		
		print(newlist)
		if(newlist[0]['score']<300):#For ms
			return("you are "+ newlist[0]['name'])
		else:
			return("you do no match")
	def publish(self):
		self.save()
	def __str__(self):
		return self.author
		
class ApplyingAs(models.Model):
	NAMES = [(n.author, n.author) for n in Summary.objects.all()]
	choice = models.CharField(max_length = 100)
	
	def __str__(self):
		return self.choice