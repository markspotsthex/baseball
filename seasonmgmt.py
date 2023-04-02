import rostermgr.core as r
import transactions.keepers as tk
import transactions.draft as td

s23 = r.get_roster()
tk.set_keepers(s23)
td.set_draft(s23)
r.update_roster(s23)

#print(s23)

r.put_on_il(s23,{'to':[('Suzuki','Seiya')],'date':'2023-03-24'})
r.update_roster(s23)

r.put_on_il(s23,{'to':[('Montas','Frankie')],'date':'2023-03-24'})
r.update_roster(s23)

r.add_from_FA(s23,{'add':[('Canha','Mark')],'date':'2023-03-26'})

r.put_on_il(s23,{'to':[('Wright','Kyle')],'date':'2023-03-26'})
r.update_roster(s23)

r.add_from_FA(s23,{'add':[('Pepiot','Ryan')],'date':'2023-03-26'})
r.add_from_FA(s23,{'add':[('Brash','Matt')],'date':'2023-03-26'})

r.add_from_FA(s23,{'drop':[('Brash','Matt')]
                   ,'add':[('Karinchak','James')]
                   ,'date':'2023-03-27'})

r.swap_on_IL(s23,{'from':[('Suzuki','Seiya')]
                  ,'to':[('Fried','Max')]
                  ,'date':'2023-03-30'})

r.add_from_Waivers(s23,{'drop':[('Pepiot','Ryan')]
                        ,'add':[('Baty','Brett')]
                        ,'date':'2023-03-31'})

r.roster_save_j(s23)
#print(s23)