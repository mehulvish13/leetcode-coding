class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        a={}
        ans=set()
        for i in range(26):
            a[chr(ord('a') + i)] = morse[i]
        for word in words:
            s=''
            for ch in word: 
                s=s+a[chr(ord(ch))]
            ans.add(s)
        return len(ans)