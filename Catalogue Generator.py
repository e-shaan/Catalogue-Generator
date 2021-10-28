# importing Required Modules
from reportlab.pdfgen import canvas as c

import csv
import json
import os
'''
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('Arial Black', 'Arial.ttf'))
'''


def generateCoordinates(rows, columns, canvas) :
	# Setting the font fo coordinates
	canvas.setFont("Helvetica-Bold",8)

	for i in range(rows):
		for j in range(columns):
			canvas.drawCentredString(j*100,i*100,"("+str(j*100 )+','+str(i*100 )+")")

'''
template function

def writeCourseName(course_name, canvas):
	canvas.setFont("Helvetica-Bold",8)
	canvas.drawCentredString(0,0, "")

'''

def writeCourseName(course_name, canvas):


	canvas.setFont('Courier-Bold', 50)
	canvas.drawCentredString(180 , 170 , course_name[0])
	canvas.drawCentredString(180 , 220 , course_name[1])
	canvas.drawCentredString(180 , 270 , course_name[2])


#function to generate catalogue in pdf format
def generate_pdf():

	#delete any existing pdf
	try:
		os.remove("catalogue.pdf")
	except:
		pass


	filename = "catalogue.pdf"

	# Creating Canvas
	canvas = c.Canvas(filename,pagesize=(1400,2000),bottomup=0)


	# Setting the origin to (10,40)
	canvas.translate(10,40)
	# Inverting the scale for getting mirror Image of logo
	canvas.scale(1,-1)

	# Inserting Logo into the Canvas at required position
	#canvas.drawImage("MF logo.png",0,0,width=25,height=30)
	canvas.drawImage("background.jpg",-20,-1960,width=1414,height=2000)


	# Title Section
	# Again Inverting Scale For strings insertion
	canvas.scale(1,-1)
	# Again Setting the origin back to (0,0) of top-left
	canvas.translate(-10,-40)

	generateCoordinates(20, 14, canvas  )


	course_name = ["Coding", "Comprehensive", "Course"]

	writeCourseName(course_name, canvas)




	# End the Page and Start with new
	canvas.showPage()
	# Saving the PDF
	canvas.save()
	os.system('catalogue.pdf')


#function to extract contents from .csv files
def extract_from_csv():


	file = open("NONE_INR.json")
	data = json.load(file)
	#print(json.dumps(data,indent = 4))
	file.close()

	for i in data:
		id = str(i['id'])
		amount = str(i['amount'])
		currency = str(i['currency'])
		order_id = str(i['order_id'])
		email = str(i['email'])
		contact = str(i['contact'])
		created_at = str(i['ltrim(rtrim(created_at))'])
		settled_at = str(i['ltrim(rtrim(settled_at))'])

		generate_pdf(id,amount,currency,order_id,email,contact,created_at,settled_at)
generate_pdf()
#extract_from_csv()
