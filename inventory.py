import csv

def read_monster_names(filename):   #Membaca data nama monster berdasarkan id monster
    monster_names = {}
    with open(filename, 'r') as file:
        csv_reader = csv.DictReader(file, delimiter=';')
        for row in csv_reader:
            monster_names[row['id']] = row['type']
    return monster_names

def read_monster_hp(filename):  #Membaca data hp monster berdasarkan id monster
    monster_hp = {}
    with open(filename, 'r') as file:
        csv_reader = csv.DictReader(file, delimiter=';')
        for row in csv_reader:
            monster_hp[row['id']] = row['hp']
    return monster_hp

def read_data(filename):  #Membaca data csv
    data = []
    with open(filename, 'r') as file:
        csv_reader = csv.DictReader(file, delimiter=';')
        for row in csv_reader:
            data.append(row)
    return data

def interface_inventory(user_id, coin_owca, data_monster, data_item, monster_names, monster_hp):  #Prosedur penampilan inventory
    print(f'>>> INVENTORY\n')
    print(f'========== INVENTORY LIST (User ID: {user_id}) ==========')
    print(f'Jumlah O.W.C.A. Coin-mu sekarang {coin_owca}.')
    for i, row in enumerate(data_monster, start=1):
        monster_id = row['monster_id']
        if monster_id in monster_names and monster_id in monster_hp:
            monster_name = monster_names[monster_id]
            hp = monster_hp[monster_id]
            print(f"{i}. Monster        (Name: {monster_name}, Lvl: {row['level']}, HP: {hp})")
    for i, row in enumerate(data_item, start=len(data_monster)+1):
        print(f"{i}. Potion        (Type: {row['type']}, Qty: {row['quantity']})")

def main_inventory():  #Prosedur utama program inventory
    monster_names = read_monster_names('monster.csv')
    monster_hp = read_monster_hp('monster.csv')   
    data_monster = read_data('monster_inventory.csv')
    data_item = read_data('item_inventory.csv')
    
    # Filter data hanya untuk user_id yang sama
    data_monster_user = [row for row in data_monster if row['user_id'] == str(user_id)]
    data_item_user = [row for row in data_item if row['user_id'] == str(user_id)]
    
    interface_inventory(user_id, coin_owca, data_monster_user, data_item_user, monster_names, monster_hp)

# PROGRAM UTAMA
coin_owca = 900
while True:
    user_id = int(input(f'Masukkan id pemain :\n'))  #Sesuai program
    if user_id == 0:
        break
    if __name__ == "__main__":
        main_inventory()
        print("\n")
