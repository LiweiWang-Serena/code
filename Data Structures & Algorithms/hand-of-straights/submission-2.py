class Solution:
    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        hand.sort()

        for start in hand:
            if count[start] != 0:
                for i in range(start, start + groupSize):
                    if count[i] == 0:
                        return False
                    count[i] -= 1
        return True

        