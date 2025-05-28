# Anagram Grouping

n = input("Input: ").lower().split(" ")
words_list = []
res = {}

for i in n:
    words_list.append(i)

for i in words_list:
    sorted_words = "".join(sorted(i))
    if sorted_words not in res:
        res[sorted_words] = []
    
    res[sorted_words].append(i)

final = list(res.values())
print(final)


# Longest Consecutive Sequence

def LCS(a):
    size = len(a)

    if size == 0:
        return 0
    
    longest = 1
    store = set()

    for i in range(0, size):
        store.add(a[i])

    for i in store:
        if i-1 not in store:
            count = 1
            x = i
            while x+1 in store:
                x += 1
                count += 1

            longest = max(longest, count)

    return longest

a = [100,200,1,2,3,4]
res = LCS(a)
print(res)


# Course Schedule

def canFinish(n, prerequisites):
    graph = {i: [] for i in range(n)}
    for a, b in prerequisites:
        graph[b].append(a)

    visited = [0] * n  # 0 = unvisited, 1 = visiting, 2 = visited

    def hasCycle(course):
        if visited[course] == 1:  # Cycle detected
            return True
        if visited[course] == 2:  # Already checked, no cycle
            return False

        visited[course] = 1  # Mark as visiting
        for next_course in graph[course]:
            if hasCycle(next_course):
                return True
        
        visited[course] = 2  # Mark as visited
        return False

    for course in range(n):
        if hasCycle(course):
            return False  # Cycle detected, cannot finish all courses

    return True  # No cycle, all courses can be completed

# Example Usage
n = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
print(canFinish(n, prerequisites))  # Output: True
