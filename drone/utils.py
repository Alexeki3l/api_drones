import time

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
            instance.battery_capacity = instance.battery_capacity - div
            instance.save()
            time.sleep(15)

        if str(n) == '5':
            print('DELIVERED')
            instance.state ='5'
            instance.save()
            print('delete')
            for medication in instance.medications.all():
                instance.medications.remove(medication)
            time.sleep(5)

        if str(n) == '6':
            print('RETURNING')
            instance.state ='6'
            instance.battery_capacity -= 5.0
            instance.save()
            time.sleep(15)
            instance.state ='1'
            instance.save()
            break
 
        else:
            instance.state = f'{n}'
            instance.save()
            time.sleep(15)
            n+=1
    if instance.battery_capacity <= 25:
        time.sleep(60)
        instance.battery_capacity = 100
        instance.save()
    
    