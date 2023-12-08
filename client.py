import json
from xmlrpc.client import ServerProxy
import time

# Buat objek proxy untuk berkomunikasi dengan server
server = ServerProxy("http://localhost:8000/")

# Fungsi untuk mengirim pesan


def send_notification(boarding_schedule, transit_location):
    message = {
        "boarding_schedule": boarding_schedule,
        "transit_location": transit_location
    }

    response1, response2 = server.process_message(message)
    with open("client_lokasi.txt", "w") as f:
        f.write(response1)

    with open("client_boarding.txt", "w") as f:
        f.write(response2)
    
    print("Meminta data boarding . . .")

    


# Simulasi pengiriman pesan
send_notification("2023-12-02 15:30:00", "Bali")

# Tunggu beberapa detik
time.sleep(15)

# Simulasi pengiriman pesan baru
send_notification("2023-12-02 12:30:00", "Yogyakarta")