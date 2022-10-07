from django.db import models


class Medication(models.Model):
    name    = models.CharField(max_length=255)
    weight  = models.IntegerField()
    code    = models.CharField(max_length=255)
    image   = models.ImageField(upload_to='medication')
    # drone   = models.ForeignKey(Drone, models.CASCADE)

    def __str__(self):
        return self.name

class Drone(models.Model):
    serial_number    = models.IntegerField()
    MODEL            = (('1', 'Lightweigth'), ('2', 'Middleweigth'), ('3', 'Cruiserweigth'),('4', 'Heavyweigth'),)
    model            = models.CharField( max_length = 1, choices=MODEL)
    weight_limit     = models.IntegerField()
    battery_capacity = models.IntegerField()
    STATE            = (('1', 'IDLE'), ('2', 'LOADING'), ('3', 'LOADED'),('4', 'DELIVERING'),('5', 'DELIVERED'),('6', 'RETURNING'),)
    state            = models.CharField(max_length = 1, choices=STATE)
    medications      = models.ManyToManyField(Medication, blank=True)

    def __str__(self):
        return str(self.serial_number)

    def save(self, *args, **kwargs):
        if not self.serial_number:
            if self.model == "1":
                self.weight_limit = 125
                return super().save(self,*args,**kwargs)
            elif self.model == "2":
                self.weight_limit = 250
                return super().save(self,*args,**kwargs)
            elif self.model == "3":
                self.weight_limit = 375
                return super().save(self,*args,**kwargs)
            elif self.model == "4":
                self.weight_limit = 500
                return super().save(self,*args,**kwargs)
        else:
            if self.model == "1":
                self.weight_limit = 125
                return super(Drone,self).save(force_update=True)
            elif self.model == "2":
                self.weight_limit = 250
                return super(Drone,self).save(force_update=True)
            elif self.model == "3":
                self.weight_limit = 375
                return super(Drone,self).save(force_update=True)
            elif self.model == "4":
                self.weight_limit = 500
                return super(Drone,self).save(force_update=True)



