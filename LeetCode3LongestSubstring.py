

# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/?envType=list&envId=parorti3

# O(2N) time complexity & O(N) with sliding window

        hmap = Counter()
        max_count = 0
        left = right = 0
        while (right < len(s)):
            hmap[s[right]] += 1

            while hmap[s[right]] > 1:
                l = s[left]
                hmap[l] -= 1
                left += 1
             
            max_count = max(max_count, right - left + 1)
            right += 1
        return max_count


    # O(N) time complexity & O(N)
        hmap = {}
        max_count = 0
        i = 0
        for j in range(len(s)):
            if s[j] in hmap:
                i = max(hmap[s[j]], i)
            
            max_count = max(max_count, j - i + 1)
            hmap[s[j]] = j + 1
        return max_count
