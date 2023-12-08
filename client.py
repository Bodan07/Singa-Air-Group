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

    
# Dictionary jadwal dan lokasi
list_jadwal = {
    "2023-12-02 12:30:00": "Bandung",
    "2023-12-02 14:30:00": "Yogyakarta",
    "2023-12-02 15:30:00": "Bali",
    "2023-12-02 16:30:00": "Lombok",
    "2023-12-02 18:30:00": "Labuan_Bajo"
}

# Menu untuk memilih jadwal dan lokasi
while True:
    print("\nMenu Pilihan Jadwal dan Lokasi:")
    for i, (jadwal, lokasi) in enumerate(list_jadwal.items(), 1):
        print(f"{i}. Jadwal: {jadwal}, Lokasi: {lokasi}")

    print("0. Keluar")
    user_input = input("Pilih nomor Tujuan (0 untuk keluar): ")

    if user_input == "0":
        break
    elif user_input.isdigit():
        index = int(user_input)
        if 1 <= index <= len(list_jadwal):
            selected_schedule = list(list_jadwal.keys())[index - 1]
            selected_location = list(list_jadwal.values())[index - 1]

            # Simulasi pengiriman pesan
            send_notification(selected_schedule, selected_location)
            # Tunggu beberapa detik
            time.sleep(15)
        else:
            print("Nomor jadwal tidak valid. Silakan pilih nomor yang sesuai.")
    else:
        print("Input tidak valid. Masukkan nomor yang sesuai.")