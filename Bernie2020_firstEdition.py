#<METADATA>
GROUP_NAME = 'Economic'
PROBLEM_NAME = 'Bernie 2020'
GROUP_MEMBERS = ['Omar Shaikh Omar','Arif Chu','Evan Kuniyoshi','Daniel Hu']
PROBLEM_VERSION ='1.0'
VERSION_DATE = 'SPT 11 2019'
#<COMMON VARIABLE>
HEALTH = 100
JOB = ['job1','job2','job3','job4','job5','job6','job7','job8','job9']
SHOPLIST = ['item1','item2','item3','item4','item5','item6','item7','item8']
HOUSEACT = ['act1','act2','act3','act4','act5','act6','act7','act8','act9']
INSURANCE = ['plan1','plan2','paln3']
PROFILE = {'family member':['father','mother','child','grandpa','grandma'],
           'location':['location1','location2','location3'],'job':['job1',
           'job2','job3'],'health condition':['well','sick','very sick',
           'died'],'insurance paln':['planA','planB','planC'],'now have':
           ['item1','item2','item3']}
CLASS = ['upper class','middle class','lower class']
year = 2000
month = 1
day = 1
DATE = str(year)+'  ',+str(month)+'  '+str(day)
MONEY = 500
INCOME = 0


class state:
#define a new type of data, state, which should include functionalities that
#allows users to click buttons to change indicators, creates an array to
#represent the UI chart, and includes the basic move function that is used in
#the operators
    def __init__(self, health=None, job=None, shop=None, houseact=None, insurance
                 =None, socialClass=None, income=0):
        self.health = health
        self.job = job
        self.shop = shop
        self.houseact = act
        self.insurance = insurance
        self.socialClass = Sclass
        self.income = income

class operator:
#this should calls the move functions from the state and uses to change state 
