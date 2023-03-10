# ! time = O(NlogN + (N/2)) where (N) is the len of the costs
# ! space  = O(N)            //    //  / / / / / // / / / / //

class Solution:
    def twoCitySchedCost(self, costs: list[list[int]]) -> int:
        min_cost = 0
        diff = []
        for i in range(len(costs)):
            diff.append([costs[i][0], costs[i][1], costs[i][1]-costs[i][0]])
        diff.sort(key=lambda x: x[2])
        l, r = 0, len(diff)-1
        while l < r:
            min_cost += diff[l][1] + diff[r][0]
            l += 1
            r -= 1
        return min_cost


costs = [[10, 20], [30, 200], [400, 50], [30, 20]]
print(Solution(). twoCitySchedCost(costs=costs, ))
