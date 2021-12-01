from django.db import models
from django.db.models.fields import AutoField
from novels.helper import PDF

class novel_auth(models.Model):
    ID = models.BigIntegerField(primary_key=True)
    Novel_link = models.TextField(max_length=255)
    Novel_Name = models.TextField(max_length=255)
    Author_link = models.TextField(max_length=255)
    Author_Name = models.TextField(max_length=255)
    Country_link = models.TextField(max_length=255)
    Country_Name = models.TextField(max_length=255)
    Pdf_File_Path = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        pdf = PDF()
        pdf.print_chapter()
        pdf.form(self.Author_Name , self.Novel_Name , self.Novel_link)
        pdf.output(f'{self.Novel_Name}.pdf', 'F')
        self.Pdf_File_Path = f'{self.Novel_Name}.pdf'
        super(novel_auth, self).save(*args, **kwargs)

    

    
    