#########################
# 141044080 Yunus CEVIK #
#########################

# This algorithm looks at how many people know each other. Accordingly, if a person does not recognize at least 5 people, 
# it is removed from the list of guests. This person is removed from the group of friends and the lists are updated. 
# According to the current list, if a person does not recognize at least 5 people, that person is removed from the list. 
# Finally, everyone on the list recognizes at least 5 people and does not recognize at least 5 people.
def partyInviteesList(people,friends):
	while True:
		conditionList = []
		notConditionList = []
		tempList = people - set(friends)
		people -= tempList
		for person in friends.keys():
			personFriends = friends[person]
			if (len(personFriends) >= 5 and len(people - personFriends) >= 5):
				conditionList.append(person)
				conditionList += list(personFriends) + list(people - personFriends)
			else:
				notConditionList.append(person)

		for person in notConditionList:
			del friends[person]
			if person in conditionList:
				conditionList.remove(person)
			if person in people:
				people.remove(person)

		for person in friends.keys():
			friends[person] -= set(notConditionList)
		
		
		if len(notConditionList) == 0:
			return set(conditionList)- set(notConditionList)

people = {'Arif','Arin','Arkan','Arkut','Arman','Baha','Bahadir','Bahattin','Bahri','Baki','Cabbar','Cafer','Cahit','Can','Canalp',
'Dalan','Dalay','Dalya','Damra','Darcan','Efehan','Efekan','Efgan','Efrahim','Efran'}

friends = {	'Arif'		:{'Arin', 'Arkan', 'Arkut', 'Arman', 'Baha', 'Bahadir', 'Dalya', 'Efekan'},
			'Arin'		:{'Arif', 'Arkut', 'Arman', 'Bahattin', 'Dalya', 'Efekan'},
			'Arkan'		:{'Bahattin', 'Bahri','Cahit', 'Efehan','Arif', 'Arin'},
			'Arkut'		:{'Cahit', 'Baha', 'Bahadir', 'Efehan', 'Efrahim', 'Efran', 'Arin', 'Bahattin', 'Dalya'},
			'Arman'		:{'Baha', 'Efran', 'Damra', 'Arif'},

			'Baha' 		:{'Arif', 'Arkut', 'Arman','Baki', 'Efgan', 'Dalan', 'Bahri', 'Bahattin', 'Dalya'},
			'Bahadir' 	:{'Arif', 'Arkut', 'Efrahim ', 'Baki'},
			'Bahattin' 	:{'Arin', 'Arkan', 'Dalay', 'Dalya', 'Efehan', 'Bahri', 'Baha'},
			'Bahri' 	:{'Arkan', 'Cabbar', 'Darcan', 'Cafer', 'Baha', 'Dalya', 'Efekan', 'Efehan'},
			'Baki'		:{'Baha', 'Bahadir'},

			'Cabbar'	:{'Bahri', 'Efehan', 'Cafer', 'Efekan', 'Cahit', 'Baha', 'Can'},
			'Cafer'		:{'Bahri', 'Cabbar', 'Dalya', 'Dalay', 'Can', 'Dalan', 'Efehan', 'Baha'},
			'Cahit'		:{'Arkan', 'Arkut', 'Cabbar', 'Dalya', 'Dalay', 'Dalan', 'Efehan', 'Baha'},
			'Can'		:{'Efehan', 'Cafer', 'Efekan', 'Efran', 'Efrahim', 'Baha'},
			
			'Dalan' 	:{'Baha', 'Efgan', 'Darcan', 'Cahit', 'Cafer', 'Dalay', 'Bahri'},
			'Dalay' 	:{'Bahattin', 'Cafer', 'Cahit', 'Dalan', 'Damra', 'Efekan', 'Bahri', 'Can'},
			'Dalya' 	:{'Arin', 'Bahattin', 'Cafer', 'Cahit', 'Efgan', 'Efrahim', 'Bahri', 'Can'},
			'Damra' 	:{'Arman', 'Bahri', 'Darcan', 'Dalay', 'Efrahim', 'Efran', 'Can'},
			'Darcan'	:{'Bahri', 'Damra', 'Efran', 'Dalan', 'Efrahim', 'Can'},

			'Efehan' 	:{'Arkan', 'Arkut', 'Bahattin', 'Cabbar', 'Can', 'Efgan','Darcan'},
			'Efekan'	:{'Arin', 'Cabbar', 'Can', 'Dalay', 'Efran','Darcan'},
			'Efgan' 	:{'Baha', 'Bahadir', 'Dalan', 'Dalya', 'Efekan','Darcan', 'Can'},
			'Efrahim' 	:{'Arkut', 'Bahadir', 'Can', 'Dalya', 'Damra','Darcan'},
			'Efran' 	:{'Arkut', 'Arman', 'Baki', 'Efekan','Darcan'}
		}

def main():
	print("Party invitees list:",partyInviteesList(people,friends))

if __name__ == '__main__':
	main()