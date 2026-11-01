class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        endings = [0] * 26
        for i in range(len(s)):
            endings[ord(s[i]) - ord("a")] = i

        # when I encounter each character I extend the goal with the endings, 
        # when going toward the goal, if the goal is extended I continue
        goal = endings[ord(s[0]) - ord("a")]
        res = []
        counter = 0
        for i in range(len(s)):
            counter += 1
            end = endings[ord(s[i]) - ord("a")]
            goal = max(goal, end)

            if i == goal:
                res.append(counter)
                counter = 0
     

        return res


        
        