
def isValid( s):
        """
        :type s: str
        :rtype: bool
        """
        type1 = []
        type2 = []
        type3 = []
        k = len(s) % 2
        if k != 0:
            return
        for j in range(0, len(s)):

            if s[j] == '(' or s[j] == ')':
                type1.append(s[j])

            elif s[j] == '{' or s[j] == '}':
                type2.append(s[j])

            elif s[j] == '[' or s[j] == ']':
                type3.append(s[j])

        a = len(type1)
        b = len(type2)
        c = len(type3)

        if a % 2 != 0:
            if b%2 !=0:
                if c%2!=0:
                    return False
        else:
            return True


s="([)]"
print(isValid(s))