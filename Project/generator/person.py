
import random as random

class Person(object):
    
    '''
    This class creates a Person object having incapsulated data
    structure( ID,age,country,home address etc.)
    '''
    
    def __init__(self):
        
        self.ID = str()
        self.age = int()
        self.gender = str()
        self.foreign_address = dict()
        self.home_address = dict()
        self.profession = dict()
        self.date_out = str()
        self.date_return = str()
        self.interest = str()
        self.social_work = str()
        self.remittance = str()
        self.travell = str()
        self.fund2invest = int()
        self.personal_view = str()
       
        
    '''
    This function generates a random ID of 10 letters.
    '''   
    def set_ID(self):
        self.ID = random_ID(10)
        
    '''
    This function generates a random gender.
    '''    
    def set_gender(self):
        self.gender = random.choice(["male","female"])
        
    '''
    This function generates a random home address
    '''
    def set_age(self):
        self.age = random_age()
        
    '''
    This function generates a random age uniformly distributed
    '''    
    def set_home_address(self,data):
        self.home_address = random_home_address(data)
        
        
    '''
    This function generates a random foreign address
    '''
    def set_foreign_address(self,data):
        self.foreign_address = random_foreign_address(data)
    

    '''
    This function generates a random age uniformly distributed
    '''
    def set_profession(self,data):
        self.profession = random_profession(data)
        
    
    '''
    This function generates a random fund available to invest
    ''' 
    def set_fund2invest(self,data):
        self.fund2invest = random_fund2invest(data)
        
        
    '''
    This function generates a random out date uniformly distributed
    ''' 
    def set_date_out(self):
        self.date_out = random_date(2010,2019) 
    
      
    '''
    This function generates a random in date uniformly distributed
    ''' 
    def set_date_return(self):
        self.date_return = random_date(2019,2025) 
        
    '''
    This function generates a random in date uniformly distributed
    ''' 
    def set_personal_view(self,data):
        self.personal_view = random_view(data)
    
    
    '''
    This function generates a random in date uniformly distributed
    ''' 
    def set_interest(self,data):
        self.interest = random_interest(data)
        
    '''
    This function generates a random in date uniformly distributed
    ''' 
    def set_social_work(self,data):
        self.social_work = random_social_work(data)
    
    
    '''
    This function generates a random in date uniformly distributed
    ''' 
    def set_remittance(self):
        self.remittance = random_remittance() 
        
    '''
    This function generates a random in date uniformly distributed
    ''' 
    def set_travell(self,data):
        self.travell = random_travell(data)
    
        
    
    
#====================================================================
# Supporting Functions for class 'Person'
#=====================================================================
    
 
'''
This function generates a random ID of 10 letters.
'''  
def random_ID(N):
        
        letters = ["A", "B", "C", "D","E",\
               "F", "G", "H", "I", "J",\
               "K", "L", "M", "N", "O",\
               "P", "Q", "R", "S", "T",\
               "U", "V", "W", "X", "Y", "Z"]
        numbers = [str(i) for i in range(10)]
        ID = ""
        for k in range(N):
            t = random.choice([0,1])
            if t == 0: ID = ID + random.choice(letters)
            else: ID = ID + random.choice(numbers)
        
        return ID
        
    
'''
 This function generates a random age uniformly distributed
'''
def random_age():
    age = random.randint(25,50)
    return age
        
'''
 This function generates a random home address 
'''    
def random_home_address(data):
    province = random.choice(list(data.keys()))
    district = random.choice(list(data[province].keys()))
    MCP =  random.choice(list(data[province][district].keys()))
    ward = random.choice(data[province][district][MCP])
    address = {"province": province,\
              "district": district,\
              "MCP": MCP,\
              "ward":ward}
    return address



'''
 This function generates a random foreign address 
'''    
def random_foreign_address(data):
    rdata = random.choice(data)
    country = rdata['name']
    lat = rdata['lat']
    lon = rdata['lon']
    ID = rdata['ID']
    city = random.choice(rdata['cities'])
    foreign_add = {"country":country,\
                   "ID":ID,\
                   "lat":lat,\
                   "lon":lon,\
                   "city":city}
                   
    return foreign_add



'''
 This function generates a random foreign address 
'''    
def random_profession(data):
    all_prof = list(data.keys())
    major = random.choice(all_prof)
    branch = random.choice(data[major])
    prof = {"major": major, "branch":branch}
    return prof



'''
 This function generates a random date
'''    
def random_date(y1,y2):
    year = random.randint(y1,y2)
    month = random.randint(1,12)
    day = random.randint(1,30)
    date = str(year) + "." + str(month) + "." + str(day)
    return date


'''
 This function generates a random view
'''    
def random_view(data):
    view = random.choice(data)
    return view


'''
 This function generates a random investment
'''    
def random_fund2invest(data):
    InvInt = {}
    for key,value in data.items():
        sector = str(key)
        InvInt.update({sector:str(random.randint(1,10))+str("%")})
    InvInt.update({"total_fund":random.randint(500,10000)})
    return InvInt
        

'''
 This function generates a random interest
'''    
def random_interest(data):
    pint = random.choice(data)
    return pint
                          
                          
'''
 This function generates a random social work
'''                              
def random_social_work(data):
    SW = []
    for item in range(random.randint(2,5)):
        date = random_date(2001,2018)
        sw = random.choice(data)
        SW.append({"date":date,"work":sw})
    return SW
                       
'''
 This function generates a random remittance 
'''                           
def random_remittance(): 
    R = []
    for i in range(random.randint(3,6)):                  
        month = random.randint(1,12)
        amount = random.randint(100,1000)
        R.append({"month":month,"amount":amount})
    return R

'''
 This function generates a random travell pattern
'''                           
def random_travell(data): 
    T = []
    for i in range(random.randint(2,5)):
        date = random_date(2010,2019)
        place = random.choice(data)
        country = place['name']
        city = random.choice(place['cities'])
        T.append({"date":date,"place" : {"country":country,"city":city}})
    return T
           
 
                       