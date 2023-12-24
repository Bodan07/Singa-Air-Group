import json
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Inisialisasi data awal jadwal boarding dan lokasi transit

list_jadwal1 = {
    "2023-12-02 12:30:00": "Bandung",
    "2023-12-02 14:30:00": "Yogyakarta",
    "2023-12-02 15:30:00": "Bali",
    "2023-12-02 16:30:00": "Lombok",
    "2023-12-02 18:30:00": "Labuan_Bajo"
}

# Fungsi untuk memproses pesan dan menyimpannya ke file
def process_message(message):
    if message["transit_location"] in list_jadwal1.values():
        result_loc = ""
        result_sch = ""
        for i, (key, value) in enumerate(list_jadwal1.items()):
            if message["transit_location"] == value:
                break
            result_loc += "Lokasi transit ke-" + str(i + 1) + " " + value + " " + "\n"
            result_sch += "Jadwal boarding ke-" + str(i + 1) + " " + key + " " + "\n"
        return result_loc, result_sch

    elif message["boarding_schedule"] in list_jadwal1.keys():
        result_loc = ""
        result_sch = ""
        for i, (key, value) in enumerate(list_jadwal1.items()):
            if message["boarding_schedule"] == key:
                break

            result_loc += "Lokasi transit ke-" + str(i + 1) + " " + value + " " + "\n"
            result_sch += "Jadwal boarding ke-" + str(i + 1) + " " + key + " " + "\n"
        return result_loc, result_sch


# Fungsi baru untuk mencetak menu
def print_menu():
    menu = "Menu Lion Air:\n"
    for i, (key, value) in enumerate(list_jadwal1.items()):
        menu += f"{i + 1}. Jadwal: {key}, Lokasi: {value}\n"
    return menu

# Buat server XML-RPC
server = SimpleXMLRPCServer(("localhost", 8000), allow_none=True)

# Tambahkan fungsi ke server
server.register_function(process_message, "process_message")
server.register_function(print_menu, "print_menu")

print("Server Lion Air siap menerima pesan.")
server.serve_forever()
