import tkinter as tk

def create_matrix(x, y, initial):
    return [[initial for i in range(x)] for j in range(y)]

def find_location(c):
    loc = []
    if c == 'J':
        c = 'I'
    for i, j in enumerate(my_matrix):
        for k, l in enumerate(j):
            if c == l:
                loc.append(i)
                loc.append(k)
                return loc

def encrypt():
    msg = entry_msg.get().upper().replace(" ", "")
    i = 0
    for s in range(0, len(msg) + 1, 2):
        if s < len(msg) - 1:
            if msg[s] == msg[s + 1]:
                msg = msg[:s + 1] + 'X' + msg[s + 1:]
    if len(msg) % 2 != 0:
        msg = msg[:] + 'X'
    result = ""
    while i < len(msg):
        loc = find_location(msg[i])
        loc1 = find_location(msg[i + 1])
        if loc[1] == loc1[1]:
            result += "{}{}".format(my_matrix[(loc[0] + 1) % 5][loc[1]], my_matrix[(loc1[0] + 1) % 5][loc1[1]]) + ' '
        elif loc[0] == loc1[0]:
            result += "{}{}".format(my_matrix[loc[0]][(loc[1] + 1) % 5], my_matrix[loc1[0]][(loc1[1] + 1) % 5]) + ' '
        else:
            result += "{}{}".format(my_matrix[loc[0]][loc1[1]], my_matrix[loc1[0]][loc[1]]) + ' '
        i = i + 2
    label_result.config(text="Şifrelenmiş Metin: " + result)

def decrypt():
    msg = entry_cipher.get().upper().replace(" ", "")
    result = ""
    i = 0
    while i < len(msg):
        loc = find_location(msg[i])
        loc1 = find_location(msg[i + 1])
        if loc[1] == loc1[1]:
            result += "{}{}".format(my_matrix[(loc[0] - 1) % 5][loc[1]], my_matrix[(loc1[0] - 1) % 5][loc1[1]]) + ' '
        elif loc[0] == loc1[0]:
            result += "{}{}".format(my_matrix[loc[0]][(loc[1] - 1) % 5], my_matrix[loc1[0]][(loc1[1] - 1) % 5]) + ' '
        else:
            result += "{}{}".format(my_matrix[loc[0]][loc1[1]], my_matrix[loc1[0]][loc[1]]) + ' '
        i = i + 2
    label_result.config(text="Deşifrelenmiş Metin: " + result.replace(' ',''))


def update_matrix():
    global my_matrix
    key = entry_key.get().replace(" ", "").upper()
    result = list()
    for c in key:
        if c not in result:
            if c == 'J':
                result.append('I')
            else:
                result.append(c)
    flag = 0
    for i in range(65, 91):
        if chr(i) not in result:
            if i == 73 and chr(74) not in result:
                result.append("I")
                flag = 1
            elif flag == 0 and i == 73 or i == 74:
                pass
            else:
                result.append(chr(i))
    k = 0
    my_matrix = create_matrix(5, 5, 0)
    for i in range(0, 5):
        for j in range(0, 5):
            my_matrix[i][j] = result[k]
            k += 1

def exit_program():
    root.destroy()

root = tk.Tk()
root.title("Playfair Şifreleme")

root.geometry("640x480")

label_key = tk.Label(root, text="Anahatarı Giriniz:")
label_key.grid(column=0,row=0)

entry_key = tk.Entry(root)
entry_key.grid(column=1,row=0)

update_button = tk.Button(root, text="Matrixi Güncelle", command=update_matrix)
update_button.grid(column=2,row=0)

encrypt_key = tk.Label(root, text="Şifrelenecek Mesajı Giriniz:")
encrypt_key.grid(column=0,row=1)

entry_msg = tk.Entry(root)
entry_msg.grid(column=1,row=1)

button_encrypt = tk.Button(root, text="Şifrele", command=encrypt)
button_encrypt.grid(column=2,row=1)

decrypt_key = tk.Label(root, text="Deşifrelenecek Mesajı Giriniz:")
decrypt_key.grid(column=0,row=2)

entry_cipher = tk.Entry(root)
entry_cipher.grid(column=1,row=2)

button_decrypt = tk.Button(root, text="Deşifrele", command=decrypt)
button_decrypt.grid(column=2,row=2)


label_result = tk.Label(root, text="")
label_result.grid(column=1,row=3)

button_exit = tk.Button(root, text="Çıkış", command=exit_program)
button_exit.grid(column=2,row=4)

root.mainloop()
