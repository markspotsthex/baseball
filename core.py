##########################################################################
"""
import
"""
##########################################################################

import pickle
import json

##########################################################################
"""
This section is to establish blank roster dictionary
"""
##########################################################################
roster_dict = {
 'move_ct':0
,'active':{
  'count':0
 ,'player_names':[]
 }
,'injured_moves':0
,'injuredlist':{
  'count':0
 ,'player_names':[]
 }
,'transaction_ct':0
,'transactions':[]
}

##########################################################################
"""
This section is for updating roster
"""
##########################################################################
def update_roster(x):
    temp_il=[]
    temp_a=[]
    t_ct = 0
    m_ct = 0

    for t in x['transactions']:
         #if add to active roster
        if (t['to']=='active'):
            for p in t['player_names']:
                temp_a.append(p)
                if (t['tdesc']=='Acquired') & (t['ttype']!='Draft'):
                    t_ct += 1
                if (t['from']=='injuredlist'):
                    temp_il.remove(p)

        if (t['from']=='active'):
            for p in t['player_names']:
                temp_a.remove(p)            
                if (t['to']=='injuredlist'):
                    m_ct += 1
                    temp_il.append(p)

    x['active']['player_names']=temp_a
    x['injuredlist']['player_names']=temp_il

    x['transaction_ct']=t_ct
    x['injured_moves']=m_ct
    x['active']['count']=len(x['active']['player_names'])
    x['injuredlist']['count']=len(x['injuredlist']['player_names'])
    x['move_ct'] = len(x['transactions'])

#UDF for generic transaction type
def add_from_type(x,pl,tt):
    t_ct = x['transaction_ct']+1
    x['transactions'].append({
         'to':'available'
        ,'from':'active'
        ,'player_names':pl['drop']
        ,'tdesc':'Dropped'
        ,'ttype':'Roster'
        ,'tdate':pl['date']
        ,'t_id':t_ct
    })
    x['transactions'].append({
         'to':'active'
        ,'from':'available'
        ,'player_names':pl['add']
        ,'tdesc':'Acquired'
        ,'ttype':tt
        ,'tdate':pl['date']
        ,'t_id':t_ct

    })
    return update_roster(x)

#UDF for FA acquisition
def add_from_FA(x,pl):
    return add_from_type(x,pl,'Free Agent')
    
#UDF for Waiver acquisition
def add_from_Waivers(x,pl):
    return add_from_type(x,pl,'Waivers')

#UDF for IL swap (player off and player on)
def swap_on_IL(x,pl):
    m_ct = x['injured_moves']+1
    x['transactions'].append({
     'to':'active'
    ,'from':'injuredlist'
    ,'player_names':pl['from']
    ,'tdesc':'Injured List'
    ,'ttype':'From IL'
    ,'tdate':pl['date']
    ,'i_id':m_ct
    })
    x['transactions'].append({
     'to':'injuredlist'
    ,'from':'active'
    ,'player_names':pl['to']
    ,'tdesc':'Injured List'
    ,'ttype':'To IL'
    ,'tdate':pl['date']
    ,'i_id':m_ct
    })

##########################################################################
"""
This section is for saving changes
"""
##########################################################################

#UDF to save changes  
def roster_save(x):
    try:
        roster_save_p(x)
        roster_save_j(x)
    except:
        print("Whoops")
#roster_save(roster_dict)

#UDF for backup to file    
def roster_save_p(x):
    try:
        with open('roster_f.pkl','wb') as roster_f:
            pickle.dump(x,roster_f)
            roster_f.close()
    except:
        print("Whoops, bad pickle")

def roster_save_j(x):
    try:
        with open("roster.json", "w") as roster_j:
            json.dump(x, roster_j, indent = 2)
            roster_j.close()
    except:
        print("Whoops, bad JSON")
        
#UDF to restore roster from pickle
def roster_load():
    try:
        with open('roster_f.pkl','rb') as roster_f:
            x = pickle.load(roster_f)
            return x
    except:
        print("Whoops")
#r_d = roster_load()


