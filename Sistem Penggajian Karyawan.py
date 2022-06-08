from mysql.connector import connect; from prettytable import PrettyTable; from os import system as cmd
#Koneksi ke database
db = connect(host = 'localhost', user = 'root', database = 'karyawan')
csr = db.cursor(dictionary = True)

class Karyawan:
    def __init__(self, nama):
        self.nama = nama
        csr.execute(f'SELECT * FROM karyawan WHERE nama = "{self.nama}" ')
        data = csr.fetchone()
        if data == None:
                print("Karyawan Tidak Terdaftar")
        
        else:
                self._nama = data['nama']
                self._jabatan = data['jabatan']
                Gaji(self._nama,self._jabatan)
 
        
    

    def kelola():
                x=input("Apakah anda ingin mengelola data karyawan?(y/n) ")
                if x == "y" :
                            print("Menu Kelola Tabel Karyawan")
                            print("1.Tambahkan Karyawan")
                            print("2.Update Karyawan")
                            print("3.Delete Karyawan")
                            print("4.Tampilkan Data Karyawan")
                            a=input("Masukkan pilihan : ")
                            if a == "1":
                                csr.execute('SELECT * FROM gaji')
                                data = csr.fetchall()
                                jabatan = []
                                for data0 in data:
                                    jabatan.append(data0['jabatan'])
                                Id=int(input("Masukkan id karyawan : "))
                                Nama=input("Masukkan nama karyawan : ")
                                Jabatan=input("Masukkan jabatan karyawan : ")
                                if Jabatan in jabatan:
                                    csr.execute(f"INSERT INTO karyawan (id,nama,jabatan) VALUES ({Id},'{Nama}','{Jabatan}')")
                                    db.commit()
                                else:
                                    print('Tidak ada jabatan')
                                Karyawan.kelola()
                            elif a == "2":
                                id=input("Masukkan id karyawan yang diubah: ")
                                nama=input("Masukkan nama karyawan: ")
                                jabatan=input("Masukkan jabatan karyawan: ")
                                csr.execute(f'UPDATE karyawan SET {nama=} ,{jabatan=} WHERE {id=} ')
                                db.commit()
                                Karyawan.kelola()
                            elif a== "3":
                                id=input("Masukkan id karyawan yang dihapus: ")
                                csr.execute(f'DELETE FROM karyawan WHERE {id=} ')
                                db.commit()
                                Karyawan.kelola()
                            elif a=="4":
                                csr.execute("""SELECT * FROM karyawan""")
                                records = csr.fetchall()
                                pt = PrettyTable()
                                pt.field_names = csr.column_names
                                print("Total Baris:  ", len(records))
                                for row in records:
                                    pt.add_row([row['id'], row['nama'], row['jabatan']])
                                print("\n")
                                print(pt)
                                Karyawan.kelola()

            
                
                else: 
                    Gaji.kelola()
                        
        

class Gaji(Karyawan):
    def __init__(self,nama,jabatan):
        self._nama=nama
        self._jabatan=jabatan

        csr.execute(f'SELECT * FROM gaji WHERE jabatan="{self._jabatan}"')
        data = csr.fetchone()
        self.upah, self.tunjangan, self.potongan = data['upah'], data['tunjangan'], data['potongan']


        self.slip_gaji()
    
    def kelola():
                x=input("Apakah anda ingin mengelola data gaji?(y/n) ")
                if x == "y" :
                            print("Menu Kelola Tabel gaji")
                            print("1.Tambahkan data gaji")
                            print("2.Update Gaji")
                            print("3.Delete Gaji")
                            print("4.Tampilkan Data Gaji")
                            a=input("Masukkan pilihan : ")
                            if a == "1":
                                jabatan=input("Masukkan Jabatan : ")
                                upah=input("Masukkan upah : ")
                                tunjangan=input("Masukkan tunjangan : ")
                                potongan=input("Masukkan potongan : ")
                                csr.execute(f"INSERT INTO gaji (jabatan,upah,tunjangan,potongan) VALUES ('{jabatan}','{upah}','{tunjangan}','{potongan}')")
                                db.commit()
                                input()
                                Gaji.kelola()
                                
                            elif a == "2":
                                jabatan=input("Masukkan Jabatan yang ingin diubah : ")
                                upah=input("Masukkan upah baru : ")
                                tunjangan=input("Masukkan tunjangan baru : ")
                                potongan=input("Masukkan potongan baru : ")
                                csr.execute(f'UPDATE gaji SET {upah=} ,{tunjangan=},{potongan=} WHERE {jabatan=} ')
                                db.commit()
                                input()
                                Gaji.kelola()
                            elif a== "3":
                                jabatan=input("Masukkan id gaji yang dihapus: ")
                                csr.execute(f'DELETE FROM gaji WHERE {jabatan=} ')
                                db.commit()
                                input()
                                Gaji.kelola()
                            elif a=="4":
                                csr.execute("""SELECT * FROM gaji""")
                                records = csr.fetchall()
                                print("Total Baris:  ", len(records))
                                pt = PrettyTable()
                                pt.field_names = csr.column_names
                                for row in records:
                                    pt.add_row([row['jabatan'], row['upah'], row['tunjangan'], row['potongan']])
                                print(pt)
                                input()
                                Gaji.kelola()
                else:
                    nama = input('Nama Karyawan : ')
                    Karyawan(nama)
    def hitung(self):
        gaji = self.upah + self.tunjangan - self.potongan
        return gaji
        
    def slip_gaji(self):
        pt = PrettyTable()
        pt.field_names = ['Nama', 'Jabatan', 'Gaji']
        pt.add_row([self._nama, self._jabatan, self.hitung()])
        print('\nSlip Gaji:', pt, sep = '\n\n')

if __name__ == '__main__':
    while 1:
        cmd('cls')
        Karyawan.kelola()
        input()
    print('Terima Kasih')
