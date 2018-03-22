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
	author = models.TextField()
	comboListText = models.TextField();
	medListText =  models.TextField();
	def getData(obj):
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
		return(comboList,medList)
	def publish(self):
		self.save()
	def __str__(self):
		return self.author