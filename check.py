from events import *
org = 'fill'
event_name, event_id,start_date,end_date = 'republic day',1,'26 Jan 2023','26 Jan 2023'
start_time,end_time = '5 am', '12 pm'
capacity, availability = 500,50
user_registered = 'member.json'
events_json_file = 'events.json'
create_event(org, events_json_file, event_name, event_id,start_date,end_date,
                start_time,end_time,user_registered,
                capacity, availability)
event_id,full_name,mob_num,password,email_id=1,'biki',6589231478,'gtiokiu', 'biju@1234'
Register('member.json',1,'biki',6589231478,'gtiokiu', 'biju@1234')