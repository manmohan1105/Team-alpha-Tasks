
'''
Q. https://www.hackerrank.com/challenges/the-quickest-way-up/problem

Markov takes out his Snakes and Ladders game, stares at the board and wonders: "If I can always roll the die to whatever number I want, what would be the least number of rolls to reach the destination?"
Rules The game is played with a cubic die of 6 faces numbered 1 to 6 .
Starting from square , land on square  with the exact roll of the die. If moving the number rolled would place the player beyond square , no move is made.
If a player lands at the base of a ladder, the player must climb the ladder. Ladders go up only.
If a player lands at the mouth of a snake, the player must go down the snake and come out through the tail. Snakes go down only.

Function Description
Complete the quickestWayUp function in the editor below. It should return an integer that represents the minimum number of moves required.
quickestWayUp has the following parameter(s):

ladders: a 2D integer array where each  contains the start and end cell numbers of a ladder
snakes: a 2D integer array where each  contains the start and end cell numbers of a snake

'''
import collections

def quickestWayUp(ladders, snakes):
    go_to_node=[0]*110
    for i in range(101):
        go_to_node[i]=i
    for  start, end in ladders:
        go_to_node[start]=end
            
    for  start, end in snakes:
        go_to_node[start]=end
    vis=set()
    dist=[0]*110
    q=collections.deque()
    q.append(1)
    vis.add(1)
    while len(q)>0:
        curr_node=q.popleft()
        for i in range(1,7):
            next_node=go_to_node[i+curr_node]    
            if next_node>=1 and next_node<=100 and next_node not in vis:
                vis.add(next_node)
                q.append(next_node)
                dist[next_node]=1+dist[curr_node]
    if not dist[100]:
        return  -1
    return dist[100]   