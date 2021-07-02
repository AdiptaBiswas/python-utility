'''
=> HTML Parser <=

HTMLParser instance is fed HTML data and calls handler methods when start tags, 
end tags, text, comments, and other markup elements are encountered.
'''

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):        
        print ('\nStart :',tag)
        for ele in attrs:
            print ('->',ele[0],'>',ele[1])
            
    def handle_endtag(self, tag):
        print ('\nEnd   :',tag)
        
    def handle_startendtag(self, tag, attrs):
        print ('\nEmpty :',tag)
        for ele in attrs:
            print ('->',ele[0],'>',ele[1])
   
MyParser = MyHTMLParser()
MyParser.feed(''.join([input("Enter HTML document: ").strip()]))

'''
Output:

Enter HTML document: <body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>

Start : body
-> data-modal-target > None      
-> class > 1

Start : h1

End   : h1

Empty : br

End   : body


End   : html
'''
