from django.db import models

# Create your models here.

class CarsModel (models.Model):
    class Meta:
        verbose_name=('ماشین')
        verbose_name_plural=('CAR')


    CarsName=models.CharField(max_length=50,verbose_name="نام ماشین")
    CarsImage=models.ImageField(upload_to="CarsImage/",verbose_name="عکس ماشین",default='E:/Auto_gallery/media/1.jpg')
    CarsDescription=models.CharField(max_length=500,verbose_name="توضیحات ماشین")

    benzin=1
    gaz=2
    electronic=3
    hybrid=4
    Carsfuel_choices=((benzin,'بنزینی'),
                      (gaz,'گازویل'),
                      (electronic,'برقی'),
                      (hybrid,'دو گانه سوز '))
                     # ,verbose_name:="سوخت ماشین"
    Carsfuel=models.IntegerField(Carsfuel_choices,)

    def __str__(self):
        return  self.CarsName