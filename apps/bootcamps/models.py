from django.db import models 
from django.conf import settings

class BootcampCategory(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    

class Bootcamp(models.Model):
    class status(models.TextChoices):
        DRAFT = 'draft' , 'pishnevis'
        REGISTRATION  =  'registration' , 'darhale sabt nam'
        ONGOING  = 'ongoing' , 'darhale bargozari'
        FINISHED = 'finished' , 'bargozar shode'
        CANCELED = 'canceled' , 'laghv shode'

    category = models.ForeignKey(BootcampCategory , on_delete=models.CASCADE , related_name='bootcamps')
    title = models.CharField(max_length=150)
    start_date = models.DateField()
    days_of_week = models.CharField(max_length=100)
    time = models.CharField(max_length=100) #saat bargozari 
    capacity = models.PositiveIntegerField()
    status = models.CharField(max_length=20 , choices=status.choices , default=status.DRAFT)

    def __str__(self):
        return self.title



class BootcampRole(models.Model):
    class RoleType(models.TextChoices):
        STUDENT = 'student' , 'student'
        MENTOR = 'mentor' , 'mentor'
        TEACHER = 'teacher' , 'teacher'

    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE ,related_name='bootcamp_roles')
    Bootcamp = models.ForeignKey(Bootcamp ,  on_delete=models.CASCADE , related_name='bootcamp_roles')
    role = models.CharField(max_length=10 , choices=RoleType.choices)

    class Meta:
        unique_together = ('user' , 'bootcamp' , 'role')

    def __str__(self):
        return f"{self.user.phone_number} - {self.bootcamp.title} - {self.role}"
