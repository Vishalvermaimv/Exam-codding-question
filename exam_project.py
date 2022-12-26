import json
import datetime
from datetime import date

def Create_Event(org,events_json_file,Event_ID,
Event_Name,Start_Date,Start_Time,End_Date,
End_Time,Users_Registered,Capacity,Availability):
    d={
        'org':org,
        'event_id':Event_ID,
        'event_name':Event_Name,
        'start_date':Start_Date,
        'start_time':Start_Time,
        'end_date':End_Date,
        'end_time':End_Time,
        'user': Users_Registered,
        'capacity':Capacity,
        'availability':Availability
        }
    f=open(events_json_file,'r')
    try:
        content=json.load(f)
        if d not in content:
            f.seek(0)
            f.truncate()
            json.dump(content,f)
    except json.JSONDecodeError:
            l=[]
            l.append(d)
            json.dump(l,f)
    f.close()

def View_Events(org,events_json_file):
    org=input()
    f=open(events_json_file,'r')
    for sub in f:
        if sub['org']==org:
            print(sub.items())
    f.close()

def View_Event_ById(events_json_file,event_id):
    event_id = input()
    with open(events_json_file,'r')as f:
        for sub in f:
            if sub['Event_ID']==event_id:
                print(sub.items())

def Update_event(org,events_json_file,event_id,detail_to_be_updated,updated_detai):
    event_id=input()
    with open(events_json_file,'r') as f:
        content=json.load(f)
        for sub in f:
            if sub['Event-ID']==event_id:
                detail_to_be_updated={
                'org':org,
                'event_id':event_id
                }
            with open(events_json_file,'w') as f:
                json.dump(detail_to_be_updated,f)
            return True
        else:
            return False

def Delete_Event(org,events_json_file,event_id):
    event_id=input()
    with open(events_json_file,'r')as f:
        content =json.load(f)
        for sub in f:
            if sub['Event_ID']==event_id:
                d.pop(sub)

def Register_for_Event(events_json_file,event_id,Full_Name):
    date_today=str(date.today())
    now=datetime.now()
    current_time=now.strftime("%H:%M:%S")
    event_id=input()
    with open(events_json_file,'r') as f:
        content=json.load(f)
        for sub  in f:
            if sub['Event_ID']==event_id:
                d={
                    "fullname":Full_Name
                }
                with open(events_json_file,'w'):
                    json.dump(d,f)
            return True
        else:
            return False

def Update_Password(members_json_file,Full_Name,new_password):
    name=input()
    with open(members_json_file,'r')as f:
        content=json.load(f)
        for sub in f:
            if sub["Full_name"]==Full_Name:
                new_password=input()
                sub.update(new_password)
            return True
        else:
            return False
def View_all_Events(events_json_file):
    with open(events_json_file) as f:
        content= json.load(f)
        ve=f.read(content)

