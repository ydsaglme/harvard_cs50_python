from fpdf import FPDF

name = input("Name: ")
pdf = FPDF()
pdf.add_page()
pdf.image("shirtificate.png", 17.5, 70, 175)
pdf.set_font("helvetica", "B", 60)
pdf.cell(0, 60, txt = "CS50 Shirtificate", align = "C")
pdf.set_font("helvetica", "B", 30)
pdf.set_text_color(255, 255, 255)
pdf.text(60, 150, txt = f"{name} was here")
pdf.output("shirtificate.pdf")
