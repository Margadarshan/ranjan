#! /usr/bin/python

"""Convert txt file into csv file"""
import datetime 

date_posted=datetime.datetime.now().ctime()


writer=open('data.csv','w+')
reader=open('data.txt','r')

lines=reader.readlines()
latest_data=lines[len(lines)-1]
latest_list=list(latest_data.split(" "))

master_str=""

for i in latest_list:
	master_str=master_str+','+str(i)

master_str=master_str+','+date_posted
writer.write(master_str[1:])

#for counting vehicles
writer=open('traffic.csv','w+')
reader=open('traffic.txt','r')
lines=reader.readlines()
latest_data=lines[len(lines)-1]
writer.write(latest_data)


reader.close()
writer.close()
