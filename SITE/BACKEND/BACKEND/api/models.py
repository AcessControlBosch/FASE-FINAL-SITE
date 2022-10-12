from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

#impede a criação de usuários com emails repetidos
#User._meta.get_field('email')._unique = True
#impede com que o email seja null ou vazio durante cadastro
#User._meta.get_field('email').blank = False
#User._meta.get_field('email').null = False

class JobPosition(models.Model):
    # permission_classes = (IsAuthenticated,)
    typeJob = models.CharField(max_length=25)
    def __str__(self):
        return self.typeJob

class Associate(models.Model):

    # permission_classes = (IsAuthenticated,)
    name = models.CharField(max_length=100)
    EDV = models.CharField(max_length=10)
    id_card = models.CharField(max_length=30, null=True, blank= True, default=0)
    skill = models.BooleanField(default=False)
    skill2 = models.BooleanField(default=False)
    adminU = models.BooleanField(default=False)
    birth = models.DateField(default='', null=False, blank=False)
    jobposition = models.ForeignKey(JobPosition, related_name="jobPositon", on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Machine(models.Model):

    # permission_classes = (IsAuthenticated,)

    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    status = models.BooleanField()
    ipaddress = models.CharField(max_length=20)
    statusMaint= models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.name

class Question(models.Model):

    # permission_classes = (IsAuthenticated,)

    type = models.CharField(max_length=15)

    def __str__(self):
        return self.type

class GreenBook(models.Model):
    idMachineFK = models.ForeignKey(Machine, related_name="machineGreenBook", on_delete=models.CASCADE)
    typeQuestion = models.ForeignKey(Question, related_name="question", on_delete=models.CASCADE)
    question = models.CharField(max_length=50)


class Areas(models.Model):

    # permission_classes = (IsAuthenticated,)

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Maintenance(models.Model):
    # permission_classes = (IsAuthenticated,)
    date = models.DateField()
    Initialhour = models.TimeField()
    Finishhour = models.TimeField(blank=True, null=True)
    idMachineFK = models.ForeignKey(Machine, related_name="machineMaintenance", on_delete=models.CASCADE)
    idAssociateFK = models.ForeignKey(Associate, related_name="associate", on_delete=models.CASCADE)

class ReleaseMachine(models.Model):
    date = models.DateField()
    InitialHour = models.TimeField()
    FinishHour = models.TimeField(blank=True, null=True)
    idMachineFK = models.ForeignKey(Machine, related_name="machineReleaseMachine", on_delete=models.CASCADE)
    idAssociateFK = models.ForeignKey(Associate, related_name="associateReleaseMachine", on_delete=models.CASCADE)

class Observation(models.Model):

    # permission_classes = (IsAuthenticated,)

    date = models.DateField()
    hour = models.TimeField() # default='', blank=True, null=True
    description = models.CharField(max_length=500)
    idMachineFK = models.ForeignKey(Machine, related_name="machineObservation", on_delete=models.CASCADE)
    idAssociateFK = models.ForeignKey(Associate, related_name="associateObservation", on_delete=models.CASCADE)

class Login(models.Model):
    name = models.CharField(max_length=200)
    edv = models.CharField(max_length=200)
    idAreaFK = models.ForeignKey(Areas, related_name="areaLogin", on_delete=models.CASCADE)
