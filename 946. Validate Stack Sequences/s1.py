class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        pop_flag = 0
        for i in range(len(pushed)):
            stack.append(pushed[i])
            while stack and stack[-1] == popped[pop_flag]:
                stack.pop()
                pop_flag +=1
        
        return True if len(stack) ==0 else False 
