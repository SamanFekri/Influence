import copy
import readData as rd

initialState,connect = rd.getData()
maxMoves = 20
states = []
lastRoundStates = []
lastRoundStates.append(initialState)

for moves in range(maxMoves):
	notRepeatedState = []
	newStates = []
	
	for i in range(len(lastRoundStates)):
		isExist = 0
		for j in range(len(states)):
			if lastRoundStates[i][0] == states[j][0]:
				isExist = 1;
				break;
		if isExist == 0:
			notRepeatedState.append(lastRoundStates[i])
	
	for i in range(len(notRepeatedState)):
		for j in range(len(connect)):
			tmp1 = copy.deepcopy(notRepeatedState[i])
			tmp2 = tmp1[0]
			for k in range(len(tmp2)):
				if connect[j][k] == 1:
					tmp2 = tmp2[:k]+ str(((int(tmp2[k])+1)%2)) +tmp2[k+1:]
			
			#print(tmp1[0]," > ",tmp2)
			tmp1[1].append(j)
			if '0' not in tmp2:
				print()
				print("result > ",tmp1[1])
				exit(1)
			
			newStates.append([tmp2,tmp1[1]])
	
	tmp=[]
	for i in range(len(newStates)):
		isExist = 0
		for j in range(i):
			if newStates[i][0] == newStates[j][0]:
				isExist = 1
		if isExist == 0:
			tmp.append(newStates[i])
	
	newStates = tmp
		
	
		
	for i in lastRoundStates:
		states.append(i)
		
	lastRoundStates= []

	
	
	print("number of old states: ",len(states)," number of new states: ",len(newStates))
	
	
	for i in range(len(newStates)):
		isExist = 0
		for j in range(len(states)):
			if newStates[i][0] == states[j][0]:
				isExist = 1;
				if len(newStates[i][1]) < len(states[j][1]):
					states[j][1] = newStates[j][1]
				break
				
		if isExist == 0:
			lastRoundStates.append(newStates[i])
			

print("It can`t be finish under ",maxMoves," moves !!!")