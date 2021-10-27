# importing Required Modules
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('Arial Black', 'Arial.ttf'))




import csv
import json
import os


def generateCoordinates(rows, columns, canvas) :
	for i in range(rows):
		for j in range(columns):
			canvas.drawCentredString(j*100,i*100,"("+str(j*100 )+','+str(i*100 )+")")

#function to generate and save invoice in .pdf format
def generate_pdf():

	try:

		os.remove("catalogue.pdf")
	except:
		pass
	filename = "catalogue.pdf"

	# Creating Canvas
	c = canvas.Canvas(filename,pagesize=(1400,2000),bottomup=0)

	# Logo Section
	# Setting the origin to (10,40)
	c.translate(10,40)
	# Inverting the scale for getting mirror Image of logo
	c.scale(1,-1)

	# Inserting Logo into the Canvas at required position
	#c.drawImage("MF logo.png",0,0,width=25,height=30)
	c.drawImage("background.jpg",-20,-1960,width=1414,height=2000)

	# Title Section
	# Again Inverting Scale For strings insertion
	c.scale(1,-1)
	# Again Setting the origin back to (0,0) of top-left
	c.translate(-10,-40)
	# Setting the font for Name title of company
	c.setFont("Helvetica-Bold",8)
	# Inserting the name of the company


	generateCoordinates(20, 14, canvas  = c )
	# Setting the font for Name title of company
	#c.setFont("Arial",8)

	c.setFont('Courier-Bold', 32)


	c.drawCentredString(100,100,"Coding")
	c.setFont('Arial Black', 32)


	c.drawCentredString(100,200,"Coding")


	# End the Page and Start with new
	c.showPage()
	# Saving the PDF
	c.save()
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
