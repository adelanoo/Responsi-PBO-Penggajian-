from mysql.connector import connect; from prettytable import PrettyTable; from os import system as cmd
#Koneksi ke database
db = connect(host = 'localhost', user = 'root', database = 'karyawan')
csr = db.cursor(dictionary = True)

class Jabatan:
    def __init__(self, nama):
        self.nama = nama
        csr.execute(f'SELECT * FROM karyawan WHERE nama LIKE "{self.nama}%"')
        data = csr.fetchone()
        if data == None:
            print("Karyawan Tidak Terdaftar")  
        else:
            self._nama = data['nama']
            self._jabatan = data['jabatan']
            LaporanGaji(self._nama,self._jabatan)
 
    def kelola():
        x=input("Apakah anda ingin mengelola data Jabatan?(y/n) ")
        if x == "y" :
            print("Menu Kelola Tabel Jabatan")
            print("1.Tambahkan Jabatan")
            print("2.Update Jabatan")
            print("3.Delete Jabatan")
            print("4.Tampilkan Data Jabatan")
            a=input("Masukkan pilihan : ")

            if a == "1":
                csr.execute('SELECT * FROM gaji')
                data = csr.fetchall()
                jabatan = []
                for data0 in data:
                    jabatan.append(data0['jabatan'])
                Id=int(input("Masukkan id Jabatan : "))
                Nama=input("Masukkan nama Jabatan : ")
                jabatan=input("Masukkan Jabatan : ")
                if jabatan in jabatan:
                    csr.execute(f"INSERT INTO karyawan (id,nama,jabatan) VALUES ({Id},'{Nama}','{jabatan}')")
                    db.commit()
                else:
                    print('Tidak ada jabatan')
                    Jabatan.kelola()
                            
            elif a == "2":
                id=input("Masukkan id Jabatan yang diubah: ")
                nama=input("Masukkan nama Jabatan: ")
                jabatan=input("Masukkan Jabatan: ")
                csr.execute(f'UPDATE karyawan SET {nama=} ,{jabatan=} WHERE {id=} ')
                db.commit()
                Jabatan.kelola()
                            
            elif a== "3":
                id=input("Masukkan id Jabatan yang dihapus: ")
                csr.execute(f'DELETE FROM karyawan WHERE {id=} ')
                db.commit()
                Jabatan.kelola()
                                
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
                
                Jabatan.kelola()

        else: 
            LaporanGaji.kelola()
                        
class Supervisor(Jabatan):
    def gaji(self):
        csr.execute(f'SELECT * FROM gaji WHERE jabatan="{self._jabatan}"')
        data = csr.fetchone()
        self.tunjangan =  data['tunjangan'] * 1.3
        return self.tunjangan

class Manager(Jabatan):
    def gaji(self):
        csr.execute(f'SELECT * FROM gaji WHERE jabatan="{self._jabatan}"')
        data = csr.fetchone()
        self.tunjangan =  data['tunjangan'] * 2
        return self.tunjangan

class HRD(Jabatan): 
    def gaji(self):
        csr.execute(f'SELECT * FROM gaji WHERE jabatan="{self._jabatan}"')
        data = csr.fetchone()
        self.tunjangan =  data['tunjangan'] * 1.4
        return self.tunjangan
        
class Keuangan(Jabatan): 
    def gaji(self):
        csr.execute(f'SELECT * FROM gaji WHERE jabatan="{self._jabatan}"')
        data = csr.fetchone()
        self.tunjangan =  data['tunjangan'] * 1.9
        return self.tunjangan

class Karyawan(Jabatan): 
    def gaji(self):
        csr.execute(f'SELECT * FROM gaji WHERE jabatan="{self._jabatan}"')
        data = csr.fetchone()
        self.tunjangan =  data['tunjangan'] * 1.2
        return self.tunjangan
        

class LaporanGaji(Jabatan):
    def __init__(self,nama,jabatan):
        self._nama=nama
        self._jabatan=jabatan
        csr.execute(f'SELECT * FROM gaji WHERE jabatan="{self._jabatan}"')
        data = csr.fetchone()
        self.upah, self.potongan = data['upah'], data['potongan']
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
                LaporanGaji.kelola()

            elif a == "2":
                jabatan=input("Masukkan Jabatan yang ingin diubah : ")
                upah=input("Masukkan upah baru : ")
                tunjangan=input("Masukkan tunjangan baru : ")
                potongan=input("Masukkan potongan baru : ")
                csr.execute(f'UPDATE gaji SET {upah=} ,{tunjangan=},{potongan=} WHERE {jabatan=} ')
                db.commit()
                input()
                LaporanGaji.kelola()
            
            elif a== "3":
                jabatan=input("Masukkan id gaji yang dihapus: ")
                csr.execute(f'DELETE FROM gaji WHERE {jabatan=} ')
                db.commit()
                input()
                LaporanGaji.kelola()
            
            elif a=="4":
                csr.execute("""SELECT * FROM gaji""")
                records = csr.fetchall()
                pt = PrettyTable()
                pt.field_names = csr.column_names
                print("Total Baris:  ", len(records))
                for row in records:
                    pt.add_row([row['jabatan'], row['upah'], row['tunjangan'], row['potongan']])
                    print("\n")
                    print(pt)
                   
                LaporanGaji.kelola()
        else:
            nama = input('Nama Karyawan : ')
            Jabatan(nama)
    
    def hitung(self):
        if self._jabatan =="Supervisor":
            self.tunjangan=Supervisor.gaji(self)
        elif self._jabatan =="Manager":
            self.tunjangan=Manager.gaji(self)
        elif self._jabatan =="HRD":
            self.tunjangan=HRD.gaji(self)
        elif self._jabatan =="Keuangan":
            self.tunjangan=Keuangan.gaji(self)
        else :
            self.tunjangan=Karyawan.gaji(self)
        gaji = self.upah + self.tunjangan - self.potongan
        return int(gaji)
        
    def slip_gaji(self):
        pt = PrettyTable()
        pt.field_names = ['Nama', 'Jabatan', 'Gaji']
        pt.add_row([self._nama, self._jabatan, self.hitung()])
        print('\nSlip Gaji:', pt, sep = '\n\n')

if __name__ == '__main__':
    while 1:
        cmd('cls')
        Jabatan.kelola()
        input()
    print('Terima Kasih')
