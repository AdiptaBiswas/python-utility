'''
* The password is valid only if it starts with 'lowercase characters', followed by special characters '!@#$%' followed by 'numbers'
* In any other case the string is 'not valid'
* Use this code to 'validate password'
'''

def validate(str):
    pat= '^[a-z].*\d$'
    match = re.search(pat, str)
    if(match):
        return True
    else:
        return False

def main():
    testcases = int(input()) #testcases
    while(testcases > 0):
        str = input()
        print(validate(str))
        testcases -= 1
        
if __name__=='__main__':
    main()
    
'''
Input: "asdsab@!@234"

Output: True
'''
