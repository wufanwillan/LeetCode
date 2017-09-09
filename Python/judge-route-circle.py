# Time:  O(n)
# Space: O(1)

# Initially, there is a Robot at position (0, 0). Given a sequence of its moves,
# judge if this robot makes a circle, which means it moves back to the original place.
#
# The move sequence is represented by a string. And each move is represent by a character.
# The valid robot moves are R (Right), L (Left), U (Up) and D (down).
# The output should be true or false representing whether the robot makes a circle.
#
# Example 1:
# Input: "UD"
# Output: true
# Example 2:
# Input: "LL"
# Output: false
    
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        h,v=0,0
        for move in moves:
            if move>'L':
                if move>'R':
                    v+=1
                else:
                    h+=1
            elif move>'D':
                h-=1
            else:
                v-=1
        return not(h|v)
