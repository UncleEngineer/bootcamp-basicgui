# writecsv.py
import csv

def writecsv(data):
	# data = ['Time',10,500]
	with open('data.csv','a',newline='',encoding='utf-8') as file:
		fw = csv.writer(file) # fw = file writer
		fw.writerow(data)
	print('Success')

d = ['2021-05-11 10:15:10',50,5000]

writecsv(d)