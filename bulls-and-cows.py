'''
https://leetcode.com/problems/bulls-and-cows/

You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.

For example:

Secret number:  "1807"
Friend's guess: "7810"
Hint: 1 bull and 3 cows. (The bull is 8, the cows are 0, 1 and 7.)
Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows. In the above example, your function should return "1A3B".

Please note that both secret number and friend's guess may contain duplicate digits, for example:

Secret number:  "1123"
Friend's guess: "0111"
In this case, the 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow, and your function should return "1A1B".
You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.
'''

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull = cow = 0
        b = [0 for i in range(10)]
        for i, c in enumerate(guess):
            if secret[i] == c:
                bull += 1
            else:
                b[int(guess[i])] += 1
        for i, c in enumerate(secret):
            if c != guess[i] and b[int(c)]:
                cow += 1
                b[int(c)] -= 1
        return '%sA%sB' % (bull, cow)


if __name__ == '__main__':
    f = Solution().getHint
    assert f('1807', '7810') == '1A3B'
    assert f('1123', '0111') == '1A1B'
    assert f('1122', '2211') == '0A4B'
