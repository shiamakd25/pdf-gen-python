from fpdf import FPDF

pdf = FPDF(orientation="portrait", unit="mm", format="A4")

pdf.add_page()

pdf.set_font(family="Times", style="", size=12)
pdf.cell(w=0, h=12, txt="Hello There", align="L", ln=1, border=1)
pdf.cell(w=0, h=12, txt="Hello There Again", align="L", ln=1, border=1)

pdf.output("output.pdf")