 '''
 * Provided with a string, this code will help to 'find all the numbers and print them'
 * Regular expression module 'Re' is required to be imported
 '''

def numberMatcher(str):
    pat= "\d+"##write the pattern here
    match=re.findall(pat,str) ##find all finds all the matched texts and returns a list
    if(match): 
        for i in match:
            print(i, end=" ")
    else:
        print(-1,end="")

def main():
    testcases = int(input()) #testcases
    while(testcases > 0):
        str = input()
        numberMatcher(str)
        print()
        testcases -= 1
        
if __name__=='__main__':
    main()
    
'''
Input: "asdasd123asmdasdk34234kfdsd34sdfk5"

Output: 123 34234 34 5
