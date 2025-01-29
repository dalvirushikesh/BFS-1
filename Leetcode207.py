#Time Complexity = O(V+E)
#Space Complexity = O(V)

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map for prerequisites
        prevMap = {i: [] for i in range(numCourses)}
        
        for crs, pre in prerequisites:
            prevMap[crs].append(pre)

        visitSet = set()

        def dfs(crs):
            if crs in visitSet:  # Detect a cycle
                return False
            if not prevMap[crs]:  # No prerequisites, course can be completed
                return True
            visitSet.add(crs)

            for pre in prevMap[crs]:
                if not dfs(pre):
                    return False

            visitSet.remove(crs)
            prevMap[crs] = []  # Mark course as fully visited
            return True

        # Check if all courses can be completed
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True