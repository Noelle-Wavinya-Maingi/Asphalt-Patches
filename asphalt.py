## Write a function def solution(S) that has the length of S as n, patches and i as an index variable

## The function should check if the current segment has a pothole and if it does it increments the patches count by 1. 

## It should also move to the segment after the patched ones by skipping two segments.

## If there are no potholes in the current segment we should move to the next segment then return the number of patches required

def solution(S):

    n = len(S)
    patches = 0
    i = 0

    while i < n:
        if S[i] == 'X':
            patches += 1

            i += 3
        
        else:
            i += 1
        
    return patches

## Test Cases
print(solution(".X..X"))
print(solution("X.XXXXX.X."))
print(solution("XX.XXX.."))
print(solution("XXXX"))
print(solution('.X...XX'))
