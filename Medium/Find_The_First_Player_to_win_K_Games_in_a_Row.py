class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        n = len(skills)
        current_winner = skills[0]
        win_count = 0
        
        for i in range(1, n):
            if current_winner > skills[i]:
                win_count += 1
            else:
                current_winner = skills[i]
                win_count = 1
            
            if win_count == k:
                break
        
        return skills.index(current_winner)
