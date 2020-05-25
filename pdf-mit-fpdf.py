import fpdf
from fpdf import FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial","", 20) #B und I für bold und italic
pdf.cell(10,10,"Graf-Computer-Service", 0, 0, "L")

pdf.cell(120,10)
pdf.cell(160,5,"10.12.2017" ,0,1,"L")


pdf.cell(10,15,"Bartholomäusstr. 66" ,0,1,"L")
pdf.cell(10,5,"90489 Nürnberg" ,0,1,"L")
pdf.output("fickpdf.pdf", "F")

