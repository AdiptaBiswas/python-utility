# If there is a dictionary with list in value (eg. below)

fav_cities = {"Andy": ["NY", "Paris", "Tokyo"], "Mark": ["Singapore", "LA"],
"Haley": ["LA", "NY", "Barcelona"], "Johnny": ["Madrid", "Rome", "Prague", "Amsterdam"],
"Michelle": ["Washington DC", "Mumbai", "Dubai", "Berlin"]}


# Code

for name, cities in fav_cities.items():
    for city in cities:
        print("{} loves {}".format(name, city))
    print(" ")
            

# O/P

'''
Johnny loves Madrid                                                                                                                              
Johnny loves Rome                                                                                                                                
Johnny loves Prague                                                                                                                              
Johnny loves Amsterdam                                                                                                                           

Michelle loves Washington DC                                                                                                                     
Michelle loves Mumbai                                                                                                                            
Michelle loves Dubai                                                                                                                             
Michelle loves Berlin                                                                                                                            

Mark loves Singapore                                                                                                                             
Mark loves LA                                                                                                                                    

Haley loves LA                                                                                                                                   
Haley loves NY                                                                                                                                   
Haley loves Barcelona                                                                                                                            

Andy loves NY                                                                                                                                    
Andy loves Paris                                                                                                                                 
Andy loves Tokyo   
'''