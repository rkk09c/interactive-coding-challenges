input = [0, 0, 1, 0, 0, 1, 0]

def jumpingOnClouds(c):
    steps, cumulus, idx = 0, 0, 0
    
    while idx < len(c):
				print('idx: ' + str(idx))    	
        if c[idx] + 2 == cumulus:
            idx += 2
            steps += 1
        else:
            idx += 1
            steps += 1
            
    return steps

if __name__ == "__main__":
		result = jumpingOnClouds(input)
		return 'result: ' + result

