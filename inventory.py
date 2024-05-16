import csv
#apalah
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

def read_monster_atk(filename):  #Membaca data hp monster berdasarkan id monster
    monster_atk = {}
    with open(filename, 'r') as file:
        csv_reader = csv.DictReader(file, delimiter=';')
        for row in csv_reader:
            monster_atk[row['id']] = row['atk_power']
    return monster_atk

def read_monster_def(filename):  #Membaca data hp monster berdasarkan id monster
    monster_def = {}
    with open(filename, 'r') as file:
        csv_reader = csv.DictReader(file, delimiter=';')
        for row in csv_reader:
            monster_def[row['id']] = row['def_power']
    return monster_def

def read_data(filename):  #Membaca data csv
    data = []
    with open(filename, 'r') as file:
        csv_reader = csv.DictReader(file, delimiter=';')
        for row in csv_reader:
            data.append(row)
    return data


def interface_inventory(user_id, coin_owca, data_monster, data_item, monster_names, monster_hp, monster_atk, monster_def):  #Prosedur penampilan inventory
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
    selected_id = input("\nKetikkan id untuk menampilkan detail item:\n>>> ")
    if selected_id == "EXIT" or selected_id == "exit":
        return
    elif selected_id == "INVENTORY" or selected_id == "inventory":
        print("\n")
        main_inventory()
    else:
        show_inventory_detail(int(selected_id), data_monster, data_item, monster_names, monster_hp, monster_atk, monster_def)

def show_inventory_detail(selected_id, data_monster, data_item, monster_names, monster_hp, monster_atk, monster_def):
    total_monsters = len(data_monster)
    total_items = len(data_item)
    while True:
        if 1 <= selected_id <= total_monsters:
            selected_monster = data_monster[selected_id - 1]
            monster_id = selected_monster['monster_id']
            monster_name = monster_names.get(monster_id, "Unknown")
            hp = monster_hp.get(monster_id, "Unknown")
            atk = monster_atk.get(monster_id, "Unknown")
            deff = monster_def.get(monster_id, "Unknown")
            print(f"Monster\nName      : {monster_name}\nATK Power : {atk}\nDEF Power : {deff}\nHP        : {hp}\nLevel     : {selected_monster['level']}\n")
        elif total_monsters + 1 <= selected_id <= total_monsters + total_items:
            selected_item = data_item[selected_id - total_monsters - 1]
            print(f"Potion\nType     : {selected_item['type']}\nQuantity : {selected_item['quantity']}")
        else:
            print("Invalid inventory ID")
        selected_id = input("\nKetikkan id untuk menampilkan detail item:\n>>> ")
        if selected_id == "EXIT" or selected_id == "exit":
            break
        elif selected_id == "INVENTORY" or selected_id == "inventory":
            print("\n")
            main_inventory()
            break
        else:
            selected_id = int(selected_id)


def main_inventory():  #Prosedur utama program inventory
    monster_names = read_monster_names('monster.csv')
    monster_hp = read_monster_hp('monster.csv')
    monster_atk = read_monster_atk('monster.csv')   
    monster_def = read_monster_def('monster.csv')   
    data_monster = read_data('monster_inventory.csv')
    data_item = read_data('item_inventory.csv')

    # Filter data hanya untuk user_id yang sama
    data_monster_user = [row for row in data_monster if row['user_id'] == str(user_id)]
    data_item_user = [row for row in data_item if row['user_id'] == str(user_id)]
    
    interface_inventory(user_id, coin_owca, data_monster_user, data_item_user, monster_names, monster_hp, monster_atk, monster_def)

# PROGRAM UTAMA
user_id = int(input(f'Masukkan id pemain :\n'))  #Sesuai program nanti
coin_owca = int(input(f'Koin O.W.C.A : '))  #Sesuai program nanti
main_inventory()

