import copy
import readData as rd

initialState,connect = rd.getData()
maxMoves = 20
states = {}
lastRoundStates = {}
lastRoundStates.update(initialState)


for moves in range(maxMoves):
	notRepeatedState = {}
	newStates = {}

	notRepeatedState.update(lastRoundStates)
	
	for i in notRepeatedState.keys():
		for j in range(len(connect)):
			tmp1 = copy.deepcopy(notRepeatedState[i])
			tmp2 = i
			for k in range(len(tmp2)):
				if connect[j][k] == 1:
					tmp2 = tmp2[:k]+ str(((int(tmp2[k])+1)%2)) +tmp2[k+1:]
			
			tmp1.append(j)
			if '0' not in tmp2:
				print()
				print("result > ",tmp1)
				exit(1)
			
			newStates.update({tmp2:tmp1})

	states.update(lastRoundStates)
	lastRoundStates= {}

	print("number of old states: ",len(states)," number of new states: ",len(newStates))
	
	for i in newStates.keys():
		if i in states.keys():
			if len(newStates[i]) < len(states[i]):
				states[i] = newStates[i]
		else:
			lastRoundStates.update({i:newStates[i]})

print("It can`t be finish under ",maxMoves," moves !!!")