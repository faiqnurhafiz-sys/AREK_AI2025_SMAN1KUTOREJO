from assets import majapahit
from story import sg
import system
import time

style = "=" * 70
bg = majapahit()

def tanya_main_lagi():
    while True:
        try:
            bg.main_lagi()
            pilihan = int(input("\nMain lagi? (1 = Ya / 2 = Tidak): "))

            if pilihan == 1:
                system.hilangkan_teks()
                print("Siap mengulang...")
                for i in range(1, 4):
                    time.sleep(1)
                    print(i)
                print("Mulai!\n")
                return True

            elif pilihan == 2:
                system.hilangkan_teks()
                bg.sampai_juga()
                return False

            else:
                print("Pilih angka 1 atau 2!")

        except ValueError:
            print("Masukkan angka yang bener dong 😆")



def main():
    while True:
        cerita_selesai = False
        try:
            bg.judul()
            bg.main_game()
            pilihan_main = int(input("\nPilihanmu (1/2): "))
            if pilihan_main == 1:
                sg.petunjuk()
                time.sleep(5)
                sg.story_awal()
                system.hilangkan_teks()
                bg.nontifikasi_awal()
                pilihan_nontifikasi = int(input("\nPilihanmu (1/2): "))
                if pilihan_nontifikasi == 1:
                    sg.story_awal_iya()
                    bg.jalan_pilihan()
                    pilihan_jalan = int(input("\nPilihanmu (1/2): "))
                    if pilihan_jalan == 1:
                        sg.persimpangan_kanan()
                        bg.saran_pria_tua()
                        pilihan_saran = int(input("\nPilihanmu (1/2): "))
                        if pilihan_saran == 1:
                            sg.ikuti_saran()
                            sg.menemui_raja()
                            system.hilangkan_teks()
                            bg.nontifikasi_akhir()
                            sg.akhir_cerita()
                            system.hilangkan_teks()
                            bg.jendela_akhir()
                            cerita_selesai = True

                        elif pilihan_saran == 2:
                            sg.tidak_ikuti_saran()
                            bg.nontifikasi_mati()
                            sg.belum_sempat()
                            sg.story_awal_tidak()
                            system.hilangkan_teks()
                            bg.jendela_akhir_tidak()
                            cerita_selesai = True

                        else:
                            print(f"\n{style}\n\nMasukkan angka yang benar, agar tidak mengulangi dari awal\n\n{style}")
                            time.sleep(3)

                    elif pilihan_jalan == 2:
                        sg.persimpangan_kiri()
                        bg.nontifikasi_pencuri()
                        pilihan_pencuri = int(input("Pilihanmu (1/2): "))
                        if pilihan_pencuri == 1:
                            sg.kabur_pencuri()
                            bg.saran_pria_tua()
                            pilihan_saran_1 = int(input("Pilihanmu (1/2): "))
                            if pilihan_saran_1 == 1:
                                sg.ikuti_saran()
                                sg.menemui_raja()
                                system.hilangkan_teks()
                                bg.nontifikasi_akhir()
                                sg.akhir_cerita()
                                system.hilangkan_teks()
                                bg.jendela_akhir()
                                cerita_selesai = True  

                            elif pilihan_saran_1 == 2:
                                sg.tidak_ikuti_saran()
                                bg.nontifikasi_mati()
                                sg.belum_sempat()
                                sg.story_awal_tidak()
                                system.hilangkan_teks()
                                bg.jendela_akhir_tidak()
                                cerita_selesai = True

                            else:
                                print(f"\n{style}\n\nMasukkan angka yang benar, agar tidak mengulangi dari awal\n\n{style}")
                                time.sleep(3)
                                            
                        elif pilihan_pencuri == 2:
                            sg.lawan_pencuri()
                            bg.nontifikasi_mati()
                            sg.belum_sempat()
                            sg.story_awal_tidak()
                            system.hilangkan_teks()
                            bg.jendela_akhir_tidak()
                            cerita_selesai = True
                            
                        elif pilihan_pencuri == 3:
                            sg.pasrah_pencuri()
                            bg.nontifikasi_mati()
                            sg.belum_sempat()
                            sg.story_awal_tidak()
                            system.hilangkan_teks()
                            bg.jendela_akhir_tidak()
                            cerita_selesai = True

                        else:
                            print(f"\n{style}\n\nMasukkan angka yang benar, agar tidak mengulangi dari awal\n\n{style}")
                            time.sleep(3)
                            
                    else:
                        print(f"\n{style}\n\nMasukkan angka yang benar, agar tidak mengulangi dari awal\n\n{style}")
                        time.sleep(3)
                        
                elif pilihan_nontifikasi == 2:
                    sg.story_awal_tidak()
                    system.hilangkan_teks()
                    bg.jendela_akhir_tidak()
                    cerita_selesai = True 
                    
                else:
                    print(f"\n{style}\n\nMasukkan angka yang benar, agar tidak mengulangi dari awal\n\n{style}")
                    time.sleep(3)

            elif pilihan_main == 2:
                system.hilangkan_teks()
                cerita_selesai = True

            else:
                print(f"\n{style}\n\nMasukkan angka yang benar, agar tidak mengulangi dari awal\n\n{style}")
                time.sleep(3)

        except ValueError: 
            print("Masukkan angka yang benar")
        if cerita_selesai:
            if not tanya_main_lagi():
                exit()
            else:
                continue

if __name__ == "__main__":
    main()

            
      
                

            
