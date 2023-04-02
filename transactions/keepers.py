def set_keepers(roster_dict):
    roster_dict['transactions'].append({
    'to':'active'
    ,'from':'available'
    ,'player_names':[
         ('Goldschmidt','Paul')
        ,('Edman','Tommy')
        ,('Rutschman','Adley')
        ]
    ,'tdesc':'Retained'
    ,'ttype':'Keeper'
    ,'tdate':'2023-03-23'
    ,'t_id':0
    })
    return roster_dict
