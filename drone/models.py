from django.db import models
from django.db.models.signals import post_save


class Medication(models.Model):
    name    = models.CharField(max_length=255) # (allowed only letters, numbers, ‘-‘, ‘_’)
    weight  = models.IntegerField()  #  weight < 500 g
    code    = models.CharField(max_length=255)
    image   = models.ImageField(upload_to='medication')  #  (allowed only upper case letters, underscore and numbers);

    class Meta:
        verbose_name = 'Medication'
        verbose_name_plural = 'Medications'

    def __str__(self):
        return self.name

class Drone(models.Model):
    serial_number    = models.CharField(max_length = 100)  # max_length = 100
    MODEL            = (('1', 'Lightweigth'), ('2', 'Middleweigth'), ('3', 'Cruiserweigth'),('4', 'Heavyweigth'),)
    model            = models.CharField( max_length = 1, choices=MODEL)
    weight_limit     = models.IntegerField(null=True, blank=True)
    battery_level    = models.FloatField(default=100)
    STATE            = (('1', 'IDLE'),('2','LOADING'),('3','LOADED'),('4','DELIVERING'),('5','DELIVERED'),('6','RETURNING'),('6','RETURNING'),)
    state            = models.CharField(max_length = 1, choices=STATE)
    medications      = models.ManyToManyField(Medication, blank=True)
    created          = models.DateTimeField(auto_now_add=True)
    updated          = models.DateTimeField(auto_now=True) 

    class Meta:
        verbose_name = 'Drone'
        verbose_name_plural = 'Drones'

    def __str__(self):
        return str(self.serial_number)

    def save(self, *args, **kwargs):
        if not self.created:
            if self.model == "1":
                self.weight_limit = 125
                self.state = '1'
                return super(Drone,self).save(force_insert=True)
            elif self.model == "2":
                self.weight_limit = 250
                self.state = '1'
                return super(Drone,self).save(force_insert=True)
            elif self.model == "3":
                self.weight_limit = 375
                self.state = '1'
                return super(Drone,self).save(force_insert=True)
            elif self.model == "4":
                self.weight_limit = 500
                self.state = '1'
                return super(Drone,self).save(force_insert=True)
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


class DroneHistory(models.Model):
    drones         = models.ForeignKey(Drone, on_delete=models.CASCADE)
    state          = models.CharField(max_length = 15)
    battery_level  = models.FloatField()
    created        = models.DateTimeField(auto_now_add=True)

    class Meta:
            verbose_name = 'drone_history'
            verbose_name_plural = 'drones_history'

    def __str__(self):
        return str(self.drones)

    def create_drone_history(sender, instance, created, **kwargs):
        if created:
            DroneHistory.objects.create(drones = instance, state = instance.get_state_display(), battery_level = instance.battery_level)

        else:
            if not DroneHistory.objects.filter(drones = instance, state = instance.get_state_display(), battery_level = instance.battery_level, created = instance.updated).exists():
                DroneHistory.objects.create(drones = instance, state = instance.get_state_display(), battery_level = instance.battery_level)
            else:
                pass

    post_save.connect(create_drone_history, sender = Drone)