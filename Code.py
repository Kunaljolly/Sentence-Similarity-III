class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1, words2 = sentence1.split(), sentence2.split()
        
        # Find longest common prefix
        prefix_len = 0
        while prefix_len < len(words1) and prefix_len < len(words2) and words1[prefix_len] == words2[prefix_len]:
            prefix_len += 1
        
        # Find longest common suffix
        suffix_len = 0
        while suffix_len < len(words1) and suffix_len < len(words2) and words1[-suffix_len-1] == words2[-suffix_len-1]:
            suffix_len += 1
        
        # Check if one sentence is a concatenation of prefix and suffix from the other
        return prefix_len + suffix_len >= min(len(words1), len(words2))
