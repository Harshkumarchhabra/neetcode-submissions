class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge case: if t is longer than s, it's impossible
        if t == "" or len(t) > len(s):
            return ""

        countt = Counter(t) # What we need
        sec = {}            # What we currently have in our window
        
        # 'count' tracks how many unique characters from 't' we have fully satisfied
        count = len(countt) 
        
        # Instead of building lists, we just remember the start and end index of the best window
        res = [-1, -1]
        resLen = float("infinity")
        
        i = 0
        for j in range(len(s)):
            char = s[j]
            # 1. Add the new right character to our window's dictionary
            sec[char] = sec.get(char, 0) + 1
            
            # 2. If this character fully satisfies what we need in 'countt', decrease our target count
            if char in countt and sec[char] == countt[char]:
                count -= 1
                
            # 3. When count == 0, our window is valid! Now we try to shrink it from the left.
            while count == 0:
                window_size = j - i + 1
                
                # Step A: Is this the smallest window we've seen? If so, save the indices!
                if window_size < resLen:
                    resLen = window_size
                    res = [i, j]
                    
                # Step B: We are about to move the left pointer, so remove the left character from 'sec'
                left_char = s[i]
                sec[left_char] -= 1
                
                # Step C: Did removing that character break our valid window?
                if left_char in countt and sec[left_char] < countt[left_char]:
                    count += 1 # We need this character again, which breaks the while loop!
                    
                # Step D: Actually move the left pointer
                i += 1
                
        # 4. Return the sliced string using our saved indices (if we found a valid window)
        if resLen != float("infinity"):
            return s[res[0] : res[1] + 1]
        else:
            return ""