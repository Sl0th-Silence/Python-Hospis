#This will be a py file for the user class

class Staff: #initialize variables on instance
    def __init__(self, user_id, first_name, last_name, contact_email, department):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.contact_email = contact_email
        self.department = department

    #Other variables
    #lists
    patient_list = []
    supervisor_list = []

    #Getters
    def get_user_id(self):
        return self.user_id
    def get_first_name(self):
        return self.first_name
    def get_last_name(self):
        return self.last_name
    def get_contact_email(self):
        return self.contact_email
    def get_department(self):
        return self.department

    #Setters
    def set_user_id(self, user_id):
        self.user_id = user_id
    def set_first_name(self, first_name):
        self.first_name = first_name
    def set_last_name(self, last_name):
        self.last_name = last_name
    def set_contact_email(self, contact_email):
        self.contact_email = contact_email
    def set_department(self, department):
        self.department = department

    #methods
    #find patient by name
    def find_patient_by_name(self, name):
        for i in range(0, len(self.patient_list)):
            if self.patient_list[i] == name:
                return self.patient_list[i]
        return None
    #Add patient to start
    def add_patient_to_start(self, name):
        self.patient_list.insert(0, name)

    #Add to end
    def add_patient_to_end(self, name):
        self.patient_list.append(name)

    #Remove from start
    def remove_patient_from_start(self):
        del self.patient_list[0]
        
    def remove_patient_from_end(self):
        del self.patient_list[len(self.patient_list) - 1]

    #Show all
    def show_all_patients(self):
        for i in range(0, len(self.patient_list)):
            print(self.patient_list[i])