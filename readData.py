import json
def getData():
	try:
		path = input("Enter path to data: ")
		with open(path) as data_file:    
			data = json.load(data_file)
			n = int(data["number"])
			initial = data["initial"]
			conncet = [[0 for i in range(n)] for j in range(n)]
			for i in range(n):
				list = data["connect"][i][str(i)]
				for j in list:
					conncet[i][j] = 1
		
			print("Data file matrix:")
			print(conncet)
			print()
			
			initialState = {initial:[]}
			return initialState,conncet
			
	except:
		print("error in reading data")
		exit(1)