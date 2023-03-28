from heapq import heappush,heappop


class Solution:
	def kClosest(self, points: list[list[int]], k: int):
		maxHeap =[]
		origin = [0,0]
		point = points.pop()
		distant  = ((origin[0]-point[0])**2+(origin[1]-point[1])**2)
		maxHeap = [[-distant,point[0],point[1]]]
		res = []
		while points:
			point = points.pop()
			distant  = ((origin[0]-point[0])**2+(origin[1]-point[1])**2)
			heappush(maxHeap,[-distant,point[0],point[1]])
			if len(maxHeap) > k :
				heappop(maxHeap)

		for _,x,y in maxHeap:
			res.append([x,y])
		return res



points =[[3,3],[5,-1],[-2,4]]
k = 2
print(Solution(). kClosest(points = points , k = k , ))