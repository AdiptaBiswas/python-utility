# If there is a list of dictionaries containing list of dictionaries in value (eg. below)

sample_dict = [{"dog": [
{"name": "tom", "owner": "haley", "breed": "corgi"},
{"name": "terry", "owner": "john", "breed": "retriever"}]},
{"cat": [
{"name": "dora", "owner": "filip", "breed": "persian"}]
}]


# Code

for a in sample_dict:
    for b, c in a.items():
        print("Animal -> {}".format(b.title()))
        print(" ")
        for d in c:
            for e, f in d.items():
                print("{} -> {}".format(e.title(), f.title()))
            print(" ")
        print(" ")
            

# O/P

'''
Animal -> Dog                                                                                                                                    

Breed -> Corgi                                                                                                                                   
Name -> Tom                                                                                                                                      
Owner -> Haley                                                                                                                                   

Breed -> Retriever                                                                                                                               
Name -> Terry                                                                                                                                    
Owner -> John                                                                                                                                    


Animal -> Cat                                                                                                                                    

Breed -> Persian                                                                                                                                 
Name -> Dora                                                                                                                                     
Owner -> Filip  
'''