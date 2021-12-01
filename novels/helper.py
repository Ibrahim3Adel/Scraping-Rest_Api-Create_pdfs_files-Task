from typing import overload
from fpdf import FPDF
import qrcode
import arabic_reshaper

class PDF(FPDF):

    def reshape(self,text):
        text_to_be_reshaped = text
        reshaped_text = arabic_reshaper.reshape(text_to_be_reshaped)
        rev_text = reshaped_text[::-1]
        return rev_text

    def form(self,author_name,bookUrl,book_name):
        pdf = PDF()
        pdf.print_chapter()

        # Logo
        qr = qrcode.QRCode()
        qr.add_data(f'{bookUrl}')
        img = qr.make_image()
        img.save(f'{book_name}.png')
        self.image(f'{book_name}.png', 75,60, 66,link= bookUrl)
        #ana
        pdf.set_y(140)
        pdf.set_x(80)
        pdf.add_font("NotoSansArabic", style="", fname="./NotoSansArabic-Regular.ttf", uni=True)
        pdf.set_font('NotoSansArabic', '', 45)
        author = self.reshape(book_name)
        pdf.write(8, author)
        pdf.set_y(170)
        pdf.set_x(80)
        book = self.reshape(author_name)
        pdf.write(8,book)
        pdf.output(f'{book_name}.pdf', 'F')

    def print_chapter(self):
        self.add_page()
        
    def takeit(Author_Name,Novel_link,Novel_Name):
        pdf = PDF()
        pdf.print_chapter()
        pdf.form(Author_Name,Novel_link,Novel_Name)
        pdf.output(f'{Novel_Name}.pdf', 'F')

