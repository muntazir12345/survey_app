import psycopg2

conn = psycopg2.connect(database="verceldb",  
                            user="default", 
                            password="I2xBTqlk9fPD",  
                            host="ep-black-snow-a4zmdro9-pooler.us-east-1.aws.neon.tech") 
c = conn.cursor()
command="""CREATE TABLE IF NOT EXISTS response_details (
                    id SERIAL PRIMARY KEY,"""
for i in range(1,11):
    command+=f'''
                plausibility_video{i} TEXT,
                valence_video{i} TEXT,
                arousal_video{i} TEXT,
        '''
command+="""age_group TEXT,
            gender TEXT,
            education TEXT,
            occupation TEXT,
            responsiveness TEXT,
            user_experience TEXT,"""
for i in range(1,7):
    command+=f'AQ_{i} TEXT,'
command=command[:-1]+")"
c.execute(command)
conn.commit()
conn.close()