# https://leetcode.com/problems/sequential-digits/description/?envType=daily-question&envId=2024-02-02


def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
    
        # convert nums to string and use sliding window logic
        # O(1) solution as constant number of strings are generated
        sample = "123456789"
        n = 10
        result = []
        for length in range(len(str(low)), len(str(high)) + 1 ):
            for start in range(n - length):
                num = int(sample[start: start + length])
                if num >= low and num <= high:
                    result.append(num)
        return result
