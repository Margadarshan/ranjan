#! /usr/bin/python

"""Convert txt file into csv file"""

# writer=open('a.csv','w')

# with open('a.txt',"r") as org:
#     while True:
#             i=org.read(1)

#             if(i==' '):
#                 i=','
 			  # if(i=='\n'):
      #             i='\r'


#             if(i==''):
#                 break

#             writer.write(i)

# org.close()
# writer.close()

""" Load csv file into database"""

import psycopg2

f=open("data.csv","r")
g=open("traffic.csv","r")

conn=psycopg2.connect("dbname=leaflet user=postgres password=postgres host=localhost")

#Activate connection curser
cur=conn.cursor()

# cur.execute("SELECT temperature,humidity,dust FROM map_sensormodel")
# rows=cur.fetchall()
# print(rows)

# cur.execute("INSERT INTO map_sensormodel(temperature,humiditu) VALUES(%s,%s)", ("Ashma","Gurung"))
# conn.commit()

#into the database
cur.copy_from(f,'map_sensormodel',columns=('temperature','humidity','dust','date_posted'),sep=",")
cur.copy_from(g,'map_vehiclemodel',columns=('vehicle_count',))
conn.commit()


# cur.execute("SELECT temperature,humidity,dust FROM map_sensormodel")
# rows=cur.fetchall()
# print(rows)

cur.close()
conn.close()
f.close()
g.close()