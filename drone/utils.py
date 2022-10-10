import time
from django.conf import settings

def change_state(instance):
    
    n=3
    cont = 0
    for medication in instance.medications.all():
        cont += medication.weight
    
    while True:
        
        if str(n) == '4':
            print('DELIVERING')
            
            instance.state ='4'
            div = cont/instance.weight_limit*10
            instance.battery_level = instance.battery_level - div
            instance.save()
            time.sleep(settings.TIME/4)

        if str(n) == '5':
            print('DELIVERED')
            instance.state ='5'
            # instance.save()
            print('delete')
            for medication in instance.medications.all():
                instance.medications.remove(medication)
            instance.save()
            time.sleep(settings.TIME/12)

        if str(n) == '6':
            print('RETURNING')
            instance.state ='6'
            instance.battery_level -= 5.0
            instance.save()
            time.sleep(settings.TIME/4)
            instance.state ='1'
            instance.save()
            break
 
        else:
            instance.state = f'{n}'
            instance.save()
            time.sleep(settings.TIME/4)
            n+=1
    if instance.battery_level <= 25:
        time.sleep(settings.TIME)
        instance.battery_level = 100
        instance.save()
    
    