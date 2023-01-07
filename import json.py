import json
from datetime import *
class event:
    def __init__(self):
        pass
def create_event(org, events_json_file, event_name, event_id,start_date,end_date,
                start_time,end_time,user_registered,
                capacity, availability):
    details = {'org':org,'Name' : event_name, 'Id': event_id, 
    'Start_Date' : start_date,
         'End_Date' : end_date, 'Start_Time' : start_time, 'End_Time' : end_time, 'User' : user_registered,
                'Capacity' : capacity, 'Availability' : availability
    }
    f = open(events_json_file, 'r+')
    try :
        data = json.load(f)
        if details not in data:
            data.append()
            f.seek(0)
            f.truncate()
            json.dump(data,f)
            return True
    except json.decoder.JSONDecodeError:
        l = []
        l.append(details)
        json.dump(l,f)
        f.close()
        return True
    return False
def view_event(org,events_json_file):
    org = input()
    f= open(events_json_file,'r+')
    for sub in f:
        if sub['org']==org:
            print(sub.items())
    f.close()
def view_events_Id(events_json_file,event_id):
    event_id = input()
    f = open(events_json_file,'r+')
    for i in f:
        if i['Id'] == event_id:
            print(i.items())
    f.close()
def update_events(org,events_json_file,event_id,details_to_be_updated):
    event_id = input()
    f = open(events_json_file,'r+')
    content = json.load(f)
    for i in f:
        if i['Id']== event_id:
            details_to_be_updated = {
                        'org':org,
                        'Id':event_id
            }
        f = open(events_json_file,'r+')
        json.dump(details_to_be_updated,f)
        return True
    return False

def Delete_event(org,events_json_file,event_id):
    event_id = input()
    f = open(events_json_file,'r+')
    content = json.load(f)
    for i in f:
        if i["Id"] == event_id:
            content.pop()

def Register(members_json_file,event_id,full_name,mob_num,password,email_id):
    c_date = str(date.today())
    t_now = datetime.time
    c_time = t_now.strftime("%H:%M:%S")
    event_id = input()
    f = open(members_json_file,'r+')
    content = json.load(f)
    for i in f:
        if i["Id"] == event_id:
            u_details = {
                'Full_name':full_name,
                'Mobile_Num':mob_num,
                "Password": password,
                "Email_ID": email_id
                }
            f = open(members_json_file,'r+')
            json.dump(u_details,f)
            return True
        return False

        



    
