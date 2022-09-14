class Solution:
    answer = 0
    
    def __init__(self):
        self.answer = 0
        
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dist = [[0] * len(wordList) for i in wordList]

        for i, iv in enumerate(wordList):
            for j, jv in enumerate(wordList):
                diff = 0
                for k in range(len(iv)):
                    if iv[k] != jv[k]:
                        diff+=1
                dist[i][j] = diff
        
        begin_word_idx = -1
        end_word_idx = -1
        for i, iv in enumerate(wordList):
            if beginWord == iv:
                begin_word_idx = i
            if endWord == iv:
                end_word_idx = i
        
        visited = [False] * len(wordList)
        q = [beginWord]
        ct = 0
        bfs(endWord, wordList, q, visited, 1)
    
    
    def bfs(self, endWord, wordList, q, visited, ct):
        temp = q[0]
        q = q[-1]
        if temp == endWorld:
            return ct
        
        