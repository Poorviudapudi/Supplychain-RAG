import os
from fpdf import FPDF

def txt_to_pdf(txt_path, pdf_path):
    with open(txt_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("helvetica", size=10)
    
    # Need to handle encoding errors and avoid un-renderable characters
    # Let's replace rupees symbol and dash with ASCII approximations to be safe.
    text = text.replace('₹', 'Rs ').replace('—', '-').replace('…', '...').replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    # replace latin-1 incompatible chars
    text = text.encode('latin-1', 'replace').decode('latin-1')
    
    pdf.multi_cell(0, 5, text)
    pdf.output(pdf_path)

if __name__ == "__main__":
    base_dir = "C:\\Users\\swapn\\.gemini\\antigravity\\scratch\\supplychain-rag\\data"
    
    txt1 = os.path.join(base_dir, "Meridian_Procurement_Policy_Handbook_v4.2.txt")
    pdf1 = os.path.join(base_dir, "Meridian_Procurement_Policy_Handbook_v4.2.pdf")
    txt_to_pdf(txt1, pdf1)
    
    txt2 = os.path.join(base_dir, "Meridian_Supply_Chain_Review_Q1_FY2025-26.txt")
    pdf2 = os.path.join(base_dir, "Meridian_Supply_Chain_Review_Q1_FY2025-26.pdf")
    txt_to_pdf(txt2, pdf2)
    
    print("PDFs created successfully.")
