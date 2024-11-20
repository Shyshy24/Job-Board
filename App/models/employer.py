from App.database import db
from App.models.job import Job 

class Employer(db.Model):
    
    companyName = db.Column(db.String(100),primary_key=True)
    postedJobs = db.relationship("Job",back_populates="employer")     
    
    def __init__(self, companyName):
        self.companyName = companyName 
    
    def get_json(self):
        return {
            'companyName': self.companyName,
            'postedJobs': [job.get_json() for job in self.postedJobs]
        }