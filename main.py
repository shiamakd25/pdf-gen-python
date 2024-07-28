from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="portrait", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    for i in range(row["Pages"]):
        pdf.add_page()
        
        pdf.set_font(family="Times", style="B", size=24)
        pdf.set_text_color(19, 19, 71)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=0)
        pdf.line(10, 21, 200, 21)

        pdf.ln(260)

        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 200)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R", ln=1, border=0)
pdf.output("output.pdf")