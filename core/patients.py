import pickle

class Patient :

    ''' Variables '''

    name = ""
    age = None
    gender = ""


    ''' Methods '''

    def create_user(self) :

        ''' Adds a new patient to "/database/patients.pkl" in database '''

    def patient_exists(self) :

        ''' Returns 1 if patient already exists, else, returns 0 '''

        return 1

    def make_appointment(self, doctor_name) :

        ''' Adds an appointment to "/database/appointments.pkl" in database '''



    def update_user(self) :

        ''' Changes the details of given user in "/database/patients.pkl" in database '''



    def get_appointments(self) :

        ''' Get all appointments of given patient name '''





        appointments = [        #temporary hardcoded values
            {
                "doctor_name" : "Stephen Strange",
                "time" : None
            },
            {
                "doctor_name" : "Doc Hudson",
                "time" : None
            },
        ]

        return appointments