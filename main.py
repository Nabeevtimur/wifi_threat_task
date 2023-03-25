from who_is_on_my_wifi import who
import datetime
import time

with open('vendors.txt') as file:
	vendors = file.read()

frequency = 300

def check_for_threads():
	WHO = who()  # who(n)
	num_of_devices = len(WHO)
	for j in range(0, num_of_devices):
		if WHO[j][5] in vendors:
			comm = f"\nОбнаружена потенциальная угроза!\nВероятно, это камера или другое устройство слежения:\n\n{WHO[j][0]} {WHO[j][1]}\n{WHO[j][2]} {WHO[j][3]}\n{WHO[j][4]} {WHO[j][5]}\n"
			print(comm)
	print(f'Количество подключенных к сети устройств: {num_of_devices}')
	print(f'Время последней проверки: {datetime.datetime.now().strftime("%d-%m-%Y %H:%M")}')
	print(WHO)


#while True:
#	check_for_threads()
#	time.sleep(frequency)
check_for_threads()