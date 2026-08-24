import string
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #bfs
        #base case 
        if (endWord not in wordList) or (beginWord == endWord):
            return 0

        #initial
        n = set(wordList)
        step = 0


        #bfs 
        q = deque([(beginWord, 1)])
        visited = set([beginWord])
        while q:
            word, step = q.popleft()
            if word == endWord:
                return step
            
            for i in range(len(word)):

                for c in string.ascii_lowercase: 
                    new = word[:i] + c + word[i+1:]
                    if new in n and new not in visited:
                        visited.add(new)
                        q.append((new, step + 1))

        return 0

        





