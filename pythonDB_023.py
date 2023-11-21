import tkinter as tk
from tkinter import messagebox
import sqlite3

# Fungsi untuk membuat tabel jika belum ada
def create_table():
    conn = sqlite3.connect('data_nilai.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS nilai_siswa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_siswa TEXT,
            biologi INTEGER,
            fisika INTEGER,
            inggris INTEGER,
            prediksi_fakultas TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Fungsi untuk menyimpan data ke SQLite
def save_data(nama_siswa, biologi, fisika, inggris, prediksi_fakultas):
    conn = sqlite3.connect('data_nilai.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
        VALUES (?, ?, ?, ?, ?)
    ''', (nama_siswa, biologi, fisika, inggris, prediksi_fakultas))
    conn.commit()
    conn.close()

# Membuat tabel jika belum ada
create_table()

def submit_nilai():
    nama_siswa = entry_nama.get()
    nilai_biologi = int(entry_biologi.get())
    nilai_fisika = int(entry_fisika.get())
    nilai_inggris = int(entry_inggris.get())

    # Logika prediksi fakultas
    if nilai_biologi > nilai_fisika and nilai_biologi > nilai_inggris:
        prediksi_fakultas = 'Kedokteran'
    elif nilai_fisika > nilai_biologi and nilai_fisika > nilai_inggris:
        prediksi_fakultas = 'Teknik'
    else:
        prediksi_fakultas = 'Bahasa'

    save_data(nama_siswa, nilai_biologi, nilai_fisika, nilai_inggris, prediksi_fakultas)

    # Menampilkan hasil prediksi
    hasil_prediksi_label.config(text=f'Hasil Prediksi: {prediksi_fakultas}')
    messagebox.showinfo("Info", "Data berhasil disimpan!")

# Inisialisasi Tkinter
root = tk.Tk()
root.title("Input Nilai Siswa")

# Membuat dan menempatkan widget
label_nama = tk.Label(root, text="Nama Siswa:")
label_biologi = tk.Label(root, text="Nilai Biologi:")
label_fisika = tk.Label(root, text="Nilai Fisika:")
label_inggris = tk.Label(root, text="Nilai Inggris:")

entry_nama = tk.Entry(root)
entry_biologi = tk.Entry(root)
entry_fisika = tk.Entry(root)
entry_inggris = tk.Entry(root)

button_submit = tk.Button(root, text="Submit", command=submit_nilai)

# Label untuk menampilkan hasil prediksi
hasil_prediksi_label = tk.Label(root, text="Hasil Prediksi: ")

# Menempatkan widget di dalam grid
label_nama.grid(row=0, column=0)
entry_nama.grid(row=0, column=1)
label_biologi.grid(row=1, column=0)
entry_biologi.grid(row=1, column=1)
label_fisika.grid(row=2, column=0)
entry_fisika.grid(row=2, column=1)
label_inggris.grid(row=3, column=0)
entry_inggris.grid(row=3, column=1)
button_submit.grid(row=4, column=0, columnspan=2)

# Menampilkan hasil prediksi
hasil_prediksi_label.grid(row=5, column=0, columnspan=2)

# Menjalankan aplikasi Tkinter
root.mainloop()
