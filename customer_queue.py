class Customer:
    def __init__(self, name, transaction):
        self.name = name
        self.transaction = transaction

class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, customer):
        self.queue.append(customer)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def display_next_transaction(self):
        if self.is_empty():
            print("Antrean kosong")
        else:
            customer = self.queue[0]
            print(f"Transaksi berikutnya: {customer.transaction} - {customer.name}")

    def remove_completed_transaction(self):
        if self.is_empty():
            print("Antrean kosong")
        else:
            customer = self.queue.pop(0)
            print(f"Transaksi selesai: {customer.transaction} - {customer.name}")

queue = Queue()

while True:
    print("===== Sistem Antrean Transaksi Pelanggan =====")
    print("1. Tambah Transaksi ke Antrean")
    print("2. Tampilkan Transaksi Berikutnya")
    print("3. Hapus Transaksi Selesai")
    print("4. Keluar")

    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":
        name = input("Masukkan nama pelanggan: ")
        transaction = input("Masukkan jenis transaksi: ")
        customer = Customer(name, transaction)
        queue.enqueue(customer)
        print("Transaksi berhasil ditambahkan ke antrean.")
    elif pilihan == "2":
        queue.display_next_transaction()
    elif pilihan == "3":
        queue.remove_completed_transaction()
    elif pilihan == "4":
        print("Program berakhir! Terima kasih telah menggunakan program ini.")
        break
    else:
        print("Pilihan tidak valid. Silahkan masukkan pilihan yang benar.")
