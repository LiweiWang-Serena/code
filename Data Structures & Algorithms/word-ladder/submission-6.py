
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #bfs
        if (endWord not in wordList) or (beginWord == endWord):
            return 0


        #bfs
        n = set(wordList)
        step = 0
        visited = set([beginWord])
        q = deque([(beginWord, 1)])
        while q:
            word, step = q.popleft()
            if word == endWord:
                return step
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new = word[:i] + c +word[i+1:]
                    if new in wordList and new not in visited:
                        visited.add(new)
                        q.append((new, step))
        return 0
        



