class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        rtype=False
        r=x
        d=0
        j=0
        
        while x>0:
            j=x%10
            d=(d*10)+j
            x=int(x/10)
            
            
        if d==r:
            rtype=True
            print("\n \n--------------------------the no. is palindrome------------------------------------")
            return rtype
        else:
            print("\n \n--------------------------------------the no is not a palindrom number--------------------------")
            return rtype

s=Solution()
j=int(input("\n \n \n \nplz enter the value to check if palindrom or not--------------------> "))
print(s.isPalindrome(j))