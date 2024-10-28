import psutil
notepad_si = False
for proceso in psutil.process_iter(['name','pid','cpu_times','memory_percent']):

    if proceso.name() == 'notepad.exe':
        notepad_si = True
        notepad_id = proceso.pid

    else:
        print('Nombre', proceso.info['name'],'--ID' ,proceso.info['pid'],'--CPU' ,sum(proceso.info['cpu_times'][:2]),'--Memoria', proceso.info['memory_percent'])


    if notepad_si == True:
        print('El notepad se esta ejecutando', notepad_id)


print('Escribe 0 para salir')
print('Dame el Id del proceso que desee terminar')
id_terminar = int(input())
while id_terminar != 0:
    try:
        for proc in psutil.process_iter(['pid']):
            id_proceso = proc.info['pid']

            if id_terminar == id_proceso:
                proc.terminate()

    except (psutil.NoSuchProcess):
        print ('ERROR: no existe ese id del proceso')
    except (psutil.AccessDenied):
        print ('ERROR: no tienes acceso para matar este proceso')
    print('Escribe 0 para salir')
    id_terminar = int(input('Dame mas procesos anda'))

