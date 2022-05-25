n = int(input())
mesage_Watner = ""

hex_message = str(input())
mesage_Watner = mesage_Watner + hex_message

print(bytes.fromhex(mesage_Watner).decode('utf-8'))