# There are a total of n courses you have to take, labeled from 0 to n - 1.
#
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
#
# For example:
#
# 2, [[1,0]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.
#
# 2, [[1,0],[0,1]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
#
# Note:
# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
#
# click to show more hints.
#
# Hints:
# This problem is equivalent to finding if a cycle exists in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
# Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera explaining the basic concepts of Topological Sort.
# Topological sort could also be done via BFS.



class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
        degrees = [0] * numCourses
        childs = [[] for i in range(numCourses)]
        # childs = [[], [], [0], [1], [2,3] ]

        for pair in prerequisites:
            degrees[pair[0]] += 1
            # pair[1] is the pre course
            childs[pair[1]].append(pair[0])

        courses = set(range(numCourses))
        # why need flag? if len(numCourse) != 0, while loop will not end
        # why need the outer while loop?
        flag = True

        while flag and len(courses):
            flag = False
            removeList = []
            for c in courses:
                if degrees[c] == 0:
                    # remove the node with no in-coming edge
                    removeList.append(c)
                    flag = True
                    # decrease the node degree
                    for child in childs[c]:
                        degrees[child] -= 1
            for r in removeList:
                courses.remove(r)

        return len(courses) == 0

    def canFinish2(self, numCourses, prerequisites):
        degrees = [0] * numCourses
        childs = [[] for i in range(numCourses)]

        for pair in prerequisites:
            degrees[pair[0]] += 1
            # pair[1] is the pre course
            childs[pair[1]].append(pair[0])
        print degrees, childs
        courses = set(range(numCourses))
        # baseCourses = set()
        baseCourses = {idx for idx, val in enumerate(degrees) if val == 0}
        # for idx, val in enumerate(degrees):
        #     if val == 0:
        #         baseCourses.add(idx)
        print baseCourses





s = Solution()

numCourses = 5
prerequisites = [
    [2, 1], [3, 0], [4, 2], [4, 3]
]
print s.canFinish2(numCourses, prerequisites)












