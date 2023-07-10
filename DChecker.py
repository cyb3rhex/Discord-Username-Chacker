import requests

print(
"""
 (                                             
 )\ )    (       )               )             
(()/(    )\   ( /(    (       ( /(    (   (    
 /(_)) (((_)  )\())  ))\  (   )\())  ))\  )(   
(_))_  )\___ ((_)\  /((_) )\ ((_)\  /((_)(()\  
 |   \((/ __|| |(_)(_))  ((_)| |(_)(_))   ((_) 
 | |) || (__ | ' \ / -_)/ _| | / / / -_) | '_| 
 |___/  \___||_||_|\___|\__| |_\_\ \___| |_|   
                                                  
                                                                            
-------------------
Dev: LSDeep
Version: 1.0.0
-------------------
"""
)

TOKEN = 'Your-Token'

def get_username(user_id):
    response = requests.get(f'https://discord.com/api/v8/users/{user_id}', 
                            headers={'Authorization': f'Bot {TOKEN}'})
    if response.status_code == 200:
        return response.json()['username'] + '#' + response.json()['discriminator']
    else:
        return None

def check_username(username):
    # Replace this with a list of user IDs you're interested in.
    user_ids = ['id1', 'id2', 'id3']  
    for user_id in user_ids:
        existing_username = get_username(user_id)
        if existing_username == username:
            print('Username is taken.')
            return
    print('Username is not taken.')
    
username_to_check = 'user#1234'
check_username(username_to_check)
