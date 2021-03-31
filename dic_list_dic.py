# If there is a nested Dictionary of Lists of Dictionaries (eg. below)

sample_dict = {"dog": [
{"name": "tom", "owner": "haley", "breed": "corgi"},
{"name": "terry", "owner": "john", "breed": "retriever"}],
"cat": [
{"name": "dora", "owner": "filip", "breed": "persian"}]
}


# Code

for k, v in sample_dict.items():
	print("Animal -> {}".format(k.title()))
	print(" ")
	for i in v:
	    for j, k in i.items():
	        print("{} -> {}".format(j.title(), k.title()))
	    print(" ")
	
# O/P

'''
Animal -> Dog                                                                                                                                    

Owner -> Haley                                                                                                                                   
Name -> Tom                                                                                                                                      
Breed -> Corgi                                                                                                                                   

Owner -> John                                                                                                                                    
Name -> Terry                                                                                                                                    
Breed -> Retriever                                                                                                                               

Animal -> Cat                                                                                                                                    

Owner -> Filip                                                                                                                                   
Name -> Dora                                                                                                                                     
Breed -> Persian
'''

