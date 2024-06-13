from fpdf import FPDF

def generate_report(violations, file_name):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    for violation in violations:
        pdf.cell(200, 10, txt=str(violation), ln=True)

    pdf.output(file_name)
