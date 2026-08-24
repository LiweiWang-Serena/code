class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if (endWord not in wordList) or (beginWord == endWord):
            return 0

        n = set(wordList)
        step = 0


        q = deque([(beginWord, 1)])
        visited = set([beginWord])
        while q:
            word, step = q.popleft()
            if word == endWord:
                return step
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in n and new_word not in visited:
                        visited.add(new_word)
                        q.append((new_word, step + 1))
        return 0
                    
        