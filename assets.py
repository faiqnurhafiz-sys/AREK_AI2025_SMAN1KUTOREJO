from nilai_game import tn

# tn = total_nilai()

style = "=" * 20
style1 = "=" * 55

def status_pemain():
    status = "Baik"
    mood = "Senang"

    return status,mood

class majapahit:
    def __init__(self):
        status, mood = status_pemain()
        self.status = status
        self.mood = mood

    def nontifikasi_awal(self):
        print("""
         ________________________________________________________
        |                                                        |
        |   Apakah Anda ingin menjelajahi Kerajaan Majapahit?    |
        |                                                        |
        |   [1] Iya                                              |
        |   [2] Tidak                                            |
        |________________________________________________________|
    """)
        
    def nontifikasi_pencuri(self):
        print("""
         ________________________________________________________
        |                                                        |
        |   Pencuri itu ingin mengambil hartamu apa yang akan    |
        |   kamu lakukan?                                        |
        |                                                        |
        |   [1] Kabur                                            |
        |   [2] Lawan                                            |
        |   [3] Pasrah                                           |
        |________________________________________________________|
    """)
        
    def jalan_pilihan(self):
        print("""\n
         ________________________________________________________
        |                                                        |
        |   Terdapat 2 persimpangan jalan apa yang akan kamu     |
        |   lakukan?                                             |
        |                                                        |
        |   [1] Lewat Persimpangan Kanan                         |
        |   [2] Lewat Persimpangan Kiri                          |
        |________________________________________________________|
    """)
        
    def saran_pria_tua(self):
         print("""\n
         ________________________________________________________
        |                                                        |
        |   Maukah kamu mengikuti saran dari Pria Tua itu,       |
        |   apa yang akan kamu lakukan?                          |
        |                                                        |
        |   [1] Ikuti Saran Pria Tua Itu                         |
        |   [2] Tidak Mengikuti Saran Pria Tua Itu               |
        |________________________________________________________|
    """)
         
    def nontifikasi_akhir(self):
         print("""\n
         ________________________________________________________
        |                                                        |
        |   Seru bukan? selamat tinggal, semoga harimu           |
        |   menyenangkan!!!                                      |
        |                                                        |
        |   Ahahhahahahahaha................!!!!                 |
        |   (suara pria tua yang sedang tertawa terbahak bahak)  |
        |________________________________________________________|
    """)
         
    def nontifikasi_mati(self):
         print("""\n
         ________________________________________________________
        |                                                        |
        |   Sayang sekali kamu belum sempat menyelesaikannya!!   |
        |                                                        |
        |   Hahhhhhhhhhhhhhhh...............!!!!                 |
        |   (suara pria tua yang sedang menghela nafas)          |
        |________________________________________________________|
    """)


        
    def jendela_status(self):
        print(f"\n{style} STATUS PEMAIN {style}\n\nStatus: {self.status}\nMood: {self.mood}\nPoin: {tn.nilai}\n\n{style1}")
    
    def jendela_akhir(self):
        print(f"\n{style}= HASIL AKHIR ={style}\n\nTotal Poin: {tn.nilai}\nTotal Pertanyaan: 4\n1.Kerajaan Majapahit ada sekitar tahun? (contoh\n  jawaban: 1570 hingga 1789 masehi):\n2.Siapakah nama dari Patih terkenal itu? (contoh\n  jawaban: Patih Raka):\n3.Siapakah nama raja yang paling terkenal di Kerajaan\n  Majapahit? (contoh jawaban: Raja Raka Simulawarman):\n4.Siapakah pembuat dari Kitab Sutasomo sekaligus orang\n  yang bergelar Mpu? (contoh jawaban: Mpu Raka):\n\nJawaban:\n1.1293 hingga 1527 masehi\n2.Patih Gajah Mada\n3.Raja Hayam Wuruk\n4.Mpu Tantular\n\n{style1}")

    def jendela_akhir_tidak(self):
        print(f"\n{style}= HASIL AKHIR ={style}\n\nKarena kamu tidak menyelesaikan sampai akhir cerita\nkamu tidak mendapatkan pertanyaan dan poin.\n\n{style1}")

    def main_lagi(self):
        print("""\n
         ________________________________________________________
        |                                                        |
        |   Apakah anda ingin bermain game ini lagi?             |
        |                                                        |
        |   [1] Iya                                              |
        |   [2] Tidak                                            |
        |________________________________________________________|
    """)
        
    def sampai_juga(self):
        print("""\n\n
         ________________________________________________________
        |                                                        |
        |   Sampai jumpa lagi!!!!                                |
        |________________________________________________________|
    """)
        
    def judul(self):
        print("""
         ________________________________________________________
        |                                                        |
        |               P E T U A L A N G A N                    |
        |            D I  E R A  M A J A P A H I T               |
        |________________________________________________________|
    """)
        
    def main_game(self):
        print("""
         ________________________________________________________
        |                                                        |
        |   Apakah anda ingin bermain game Petualangan Di Era    |
        |   Majapahit?                                           |
        |                                                        |
        |   [1] Iya                                              |
        |   [2] Tidak                                            |
        |________________________________________________________|
    """)
        
    
    

# Contoh penggunaan:
if __name__ == "__main__":
    bg = majapahit()
    bg.nontifikasi_awal()
    bg.jendela_status()
    bg.jalan_pilihan()
    bg.jendela_akhir()
    bg.jendela_akhir_tidak()
    bg.main_lagi()
    bg.judul()
    bg.sampai_juga()
    bg.main_game()
   
