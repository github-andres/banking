import numpy as np
from datetime import datetime, timedelta


class PersonGen:
       
    def __init__(self, dict_item):
        self.id = None
        self.nationality = [dict_item[0],]
        self.gender = "M" if np.random.rand() > dict_item[1].female_perc else "F"
        self.age_at_registration = np.random.triangular(0, dict_item[1].avg_age, dict_item[1].life_exp)
        self.registed_mother = None
        self.registed_father = None
        self.marital_status = "single"
        self.has_children = []        
        self.date_of_birth = datetime.now() - timedelta(self.age_at_registration * 365.25)


    def marital_status_change(self, new_status):
        marital_status_list = ["single", "married", "divorced", "separated", "widower/widow"]
        if new_status in marital_status_list:
            self.marital_status = new_status

    
      

if __name__ == "__main__":
    pass
 
        
    