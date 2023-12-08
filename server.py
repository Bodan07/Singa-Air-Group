import json
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Inisialisasi data awal jadwal boarding dan lokasi transit
current_boarding_schedule = None
current_transit_location = None

list_jadwal1 = {
    "2023-12-02 12:30:00": "Bandung",
    "2023-12-02 14:30:00": "Yogyakarta",
    "2023-12-02 15:30:00": "Bali",
    "2023-12-02 16:30:00": "Lombok",
    "2023-12-02 18:30:00": "Labuan_Bajo"
}

# Fungsi untuk memproses pesan dan menyimpannya ke file
def process_message(message):
    global current_boarding_schedule, current_transit_location

    if message["transit_location"] in list_jadwal1.values() :
        result_loc = ""
        result_sch = ""
        with open("lokasi.txt", "wt") as file:
            for i, (key,value) in enumerate(list_jadwal1.items()):
                if message["transit_location"] == value:
                    break
                    
                    # with open("boarding.txt", "wt") as file:
                    #     print(json.dumps(f"{key}"))
                    #     file.write(json.dumps(f"{key}") + "\n")

                # print(json.dumps(f"{value}"))
                result_loc += "Lokasi transit ke-"+str(i+1)+ " "+ value + " "+ "\n"
                result_sch += "Jadwal boarding ke-"+str(i+1)+ " " + key + " "+ "\n"
        return result_loc, result_sch
    
    elif message["boarding_schedule"] in list_jadwal1.keys() :
        result_loc = ""
        result_sch = ""
        with open("lokasi.txt", "wt") as file:
            for i, (key,value) in enumerate(list_jadwal1.items()):
                if message["boarding_schedule"] == key:
                    break
                    
                    # with open("boarding.txt", "wt") as file:
                    #     print(json.dumps(f"{key}"))
                    #     file.write(json.dumps(f"{key}") + "\n")

                # print(json.dumps(f"{value}"))
                result_loc += "Lokasi transit ke-"+str(i+1)+ " "+ value + " "+ "\n"
                result_sch += "Jadwal boarding ke-"+str(i+1)+ " " + key + " "+ "\n"
        return result_loc, result_sch

    


# Buat server XML-RPC
server = SimpleXMLRPCServer(("localhost", 8000), allow_none=True)

# Tambahkan fungsi ke server
server.register_function(process_message, "process_message")

print("Server Lion Air siap menerima pesan.")
server.serve_forever()