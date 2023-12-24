from xmlrpc.client import ServerProxy
import time
import json

# Buat objek proxy untuk berkomunikasi dengan server
server = ServerProxy("http://localhost:8000/",allow_none=True)

# Fungsi untuk menampilkan menu
def show_menu():
    menu = server.print_menu()
    print(menu)

# Fungsi untuk menyimpan data ke dalam file
def save_to_file(data, filename):
    with open(filename, "w") as f:
        f.write(data)
        print(f"Data disimpan di {filename}")

# Meminta list jadwal dari server
list_jadwal_str = server.get_list_jadwal()
list_jadwal = json.loads(list_jadwal_str)

# Menampilkan menu dari server
while True:
    print("\nMenu Pilihan Jadwal dan Lokasi:")
    show_menu()

    # Meminta input dari pengguna
    user_input = input("Masukkan nomor atau nama kota (0 untuk keluar): ")

    if user_input == "0":
        print("Terima kasih. Sampai jumpa lagi!")
        break

    if user_input.isdigit():
        index = int(user_input)
        if 1 <= index <= len(list_jadwal):
            selected_schedule = list(list_jadwal.keys())[index - 1]

            # Simulasi pengiriman pesan
            try:
                result_loc, result_sch = server.process_message({"boarding_schedule": selected_schedule, "transit_location": None})
                # Menyimpan hasil ke file
                save_to_file(result_sch, "client_boarding.txt")
            except Exception as e:
                print(f"Error: {e}")
            finally:
                # Tunggu beberapa detik
                time.sleep(2)
        else:
            print("Nomor jadwal tidak valid. Silakan pilih nomor yang sesuai.")
    else:
        # Simulasi pengiriman pesan
        try:
            result_loc, result_sch = server.process_message({"transit_location": user_input, "boarding_schedule": None})
            # Menyimpan hasil ke file
            save_to_file(result_loc, "client_location.txt")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            # Tunggu beberapa detik
            time.sleep(2)
