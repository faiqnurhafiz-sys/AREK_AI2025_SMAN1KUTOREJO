import time
import system
from assets import majapahit
from nilai_game import tn

sy = system
bg = majapahit()
def nama_story():
    nama = input("\nSiapa Namamu: ")
    return nama

def nama_patih_story():
    nama_patih = input("\nSiapakah nama dari Patih terkenal itu? (contoh jawaban: Patih Raka): ").lower().strip()
    return nama_patih

def nama_raja_story():
    nama_raja = input("\nSiapakah nama raja yang paling terkenal di Kerajaan Majapahit? (contoh jawaban: Raja Raka Simulawarman): ").lower().strip()
    return nama_raja

def nama_mpu_story():
    nama_mpu = input("\nSiapakah pembuat dari Kitab Sutasomo sekaligus orang yang bergelar Mpu? (contoh jawaban: Mpu Raka): ").lower().strip()
    return nama_mpu

class story_game:
    def __init__(self):
        self.nama = None
        self.nama_patih = None
        self.nama_raja = None
        self.nama_mpu = None

    def isi_nama(self):
        self.nama = nama_story()

    def isi_nama_patih(self):
        self.nama_patih = nama_patih_story()

    def isi_nama_raja(self):
        self.nama_raja = nama_raja_story()

    def isi_nama_mpu_(self):
        self.nama_mpu = nama_mpu_story()

        
    def story_awal(self):
        bg.jendela_status()
        sy.type_effect("\nHari ini, kelasku kedatangan narasumber istimewa dari Dinas Kebudayaan dan Pariwisata (Disparbud)\nProvinsi Jawa Timur.")
        time.sleep(1)
        sy.type_effect("\nNarasumber tersebut tampak masih muda, mungkin berusia sekitar dua puluh hingga tiga puluh tahun.")
        time.sleep(1)
        sy.type_effect("\nIa datang untuk memberikan penjelasan mengenai berbagai kebudayaan yang ada di Jawa Timur, salah satunya tentang \nKerajaan Majapahit.")
        time.sleep(3)
        sy.type_effect("\nNarasumber: Sebelum itu perkenalkan nama saya adalah Kak Fajar.")
        time.sleep(1)
        sy.type_effect("\nAku dan Teman-temanku: Hai Kak Fajar!!.")
        time.sleep(1)
        sy.type_effect("\nKak Fajar: Hai juga semua...")
        time.sleep(1)
        sy.type_effect("\nKak Fajar: Baik kita langsung ke materi saja ya!!.")
        time.sleep(1)
        sy.type_effect("\nAku dan Teman-temanku: Baik kak!!.")
        time.sleep(1)
        sy.type_effect("\nKak Fajar: Seperti yang kita ketahui, Jawa Timur mempunyai banyak sekali kebudayaan maupun peninggalan dari\njaman dahulu. Salah satunya adalah Kerajaan Majapahit...................")
        time.sleep(3)
        sy.type_effect("\nAku: Hoammmm, penjelasannya lama sekali. Membuatku menjadi mengantuk saja ")
        sy.type_effect("\nTanpa kusadari aku tertidur di tengah penjelasannya.")
        bg.status = "Tertidur"
        time.sleep(1)
        sy.type_effect("\nSaat aku membuka mataku, tiba-tiba  muncullah sebuah nontifikasi. Entah darimana nontifikasi itu berasal,\nia tiba-tiba memberikan pesan seperti berikut: ")
        time.sleep(1)
    
    def story_awal_tidak(self):
        sy.type_effect("\nKak Fajar: Hei.....bangunlah....")
        time.sleep(1)
        sy.type_effect("\nSontak akupun terbangun dari tidurku!!, sambil mengusap air liurku.")
        bg.mood = "Kaget"
        bg.jendela_status()
        time.sleep(1)
        sy.type_effect("\nKak Fajar: Anak-anak mari kita pergi ke Museum Trowulan.")
        time.sleep(1)
        sy.type_effect("\nAkupun pergi ke Museum Trowulan bersama Kak Fajar dan teman-teman sekelasku. .")
        time.sleep(1)
        sy.type_effect("\nSesampainya di Museum Trowulan, aku dan teman-temanku melihat-lihat bekas peninggalan Kerajaan Majapahit.")
        time.sleep(1)
        sy.type_effect("\nSaat sedang melihat-lihat, aku penasaran dengan lukisan wajah yang bernama Patih Gajah Mada. \nSambil penasaran aku bertanya ke Kak Fajar.")
        bg.mood = "Senang"
        bg.status = "Penasaran"
        bg.jendela_status()
        time.sleep(1)
        sy.type_effect("\nAku: Kak Fajar!!, Kalo boleh tahu siapakah Patih Gaja Mada itu?.")
        time.sleep(1)
        sy.type_effect("\nKak Fajar: Patih Gajah Mada adalah salah satu jenderal paling terkenal dari Kerajaan Majapahit. \nIa dikenal melalui Sumpah Palapa yang diucapkannya, serta perannya yang besar dalam membantu Majapahit\nmenaklukkan dan menyatukan banyak wilayah di Nusantara.")
        time.sleep(1)
        sy.type_effect("\nAku: Ohh, jadi Patih Gajah Mada adalah orang yang sangat terkenal pada masanya ya?.")
        time.sleep(1)
        sy.type_effect("\nKak Fajar: Iya jadi dulu Patih Gajah Mada memang terkenal karena perannya dalam menyatukan wilayah nusantara.")
        bg.status = "Baik"
        time.sleep(1)
        sy.type_effect("\nKak Fajar: Baik anak-anak karena waktu kita sudah habis mari kita kembali kesekolah.")
        time.sleep(1)
        sy.type_effect("\nAku dan Teman-temanku: Baik kak!!.")
        time.sleep(1)
        sy.type_effect("\nAku dan teman-temanku pun kembali ke sekolah tanpa tahu apa yang terjadi saat aku tidur tadi.")
        time.sleep(1)
    
    def story_awal_iya(self):
        sy.type_effect("\nSaat aku membuka mataku tiba-tiba, aku sudah berada di hutan yang lebat dan gelap.")
        bg.status = "Panik"
        bg.mood = "Kaget"
        bg.jendela_status()
        time.sleep(1)
        sy.type_effect("\nDengan panik aku berjalan entah kemana dan menemui 2 persimpangan jalan.")
        time.sleep(1)
    
    def persimpangan_kanan(self):
        sy.type_effect("\nAkupun  berjalan melewati persimpangan kanan dan berharap menemukan sebuah pemukiman.")
        time.sleep(1)
        sy.type_effect("\nSetelah berjalan cukup lama akhirnya aku menemukan sebuah kerajaan yang besar nan megah.")
        bg.status = "Lega"
        bg.mood = "Senang"
        bg.jendela_status()
        time.sleep(1)
        sy.type_effect("\nTiba-tiba ada seorang pria tua menghampiriku, ia menatapku sambil keheranan.")
        time.sleep(1)
        sy.type_effect("\nPria Tua: Hei, siapa namamu? kenapa bajumu berbeda dengan kami?")
        time.sleep(1)
        sg.isi_nama()
        time.sleep(1)
        sy.type_effect(f"\nAku: Namaku {self.nama}")
        time.sleep(1)
        sy.type_effect(f"\n{self.nama}: Maaf kek, kalo boleh tahu ini dimana ya?")
        bg.status = "Penasaran"
        bg.jendela_status()
        time.sleep(1)
        sy.type_effect("\nPria Tua: Sepertinya kamu memang bukan orang sini, nama tempat ini adalah Kerajaan Majapahit.")
        time.sleep(1)
        sy.type_effect(f"\n{self.nama}: Bagaimana mungkin aku berada di Kerajaan Majapahit?, bukannya kerajaan itu ada masa lalu (berbicara di dalam hati). ")
        bg.mood = "kaget"
        bg.jendela_status()
        time.sleep(1)
        sy.type_effect(f"\n{self.nama}: Kerajaan Majapahit ada sekitar tahun berapa ya aku lupa!!, harusnya aku mendengarkan penjelasan Kak Fajar tadi.")
        time.sleep(1)
        jawab_tahun = input("\nKerajaan Majapahit ada sekitar tahun? (contoh jawaban: 1570 hingga 1789 masehi): ").strip()
        if jawab_tahun == "1293 hingga 1527 masehi":
            tn.nilai += 25
        else:
            tn.nilai += 0
        time.sleep(1)
        sy.type_effect(f"\n{self.nama}: Oh aku ingat, Kerajaan Majapahit ada sekitar {jawab_tahun}")
        time.sleep(1)
        sy.type_effect("\nPria Tua: Sekedar saran saja, jika kau ingin kembali ke tempat asalmu, carilah orang berbadan besar dan kuat serta senantiasa membawa keris")
        time.sleep(1)
        sy.type_effect("\nPria Tua: Mungkin dia bisa mengembalikanmu ke tempat asalmu.")
        time.sleep(1)
        sy.type_effect(f"\n{self.nama}: Kek, maksudnya apa kek?")
        time.sleep(1)
        sy.type_effect("\nSaat aku mengedipkan mata secara ajaib Pria Tua itu menghilang  entah kemana.")
        bg.status = "Penasaran"
        bg.mood = "Panik"
        bg.jendela_status()
        time.sleep(1)

    def ikuti_saran(self):
        sy.type_effect("\nDengan pikiran yang penuh pertanyaan dan keheranan, akupun mengikuti saran Pria Tua itu untuk mencari pria berbadan besar dan kuat serta senantiasa membawa keris.")
        bg.status = "Keheranan"
        bg.mood = "Panik"
        bg.jendela_status()
        time.sleep(1)
        sy.type_effect("\nSaat aku sedang menelusuri kota, terdapat seorang pria berbadan besar dan membawa keris sedang menyelenggarakan sayembara.")
        time.sleep(1)
        sy.type_effect("\nPria Berbadan Besar: Barang siapa yang mempunyai kebijakan/ide yang bagus dalam menangani perebutan wilayah oleh berbagai bangsawan kerajaan, ia akan diberikan hadiah oleh raja.")
        time.sleep(1)
        sy.type_effect("\nPedagang: Tuan, bagaimana kalau kita menaklukkan seluruh bangsawan itu?")
        time.sleep(1)
        sy.type_effect("\nPria Berbadan Besar: Kurang menarik!!, selanjutnya.")
        time.sleep(1)
        sy.type_effect("\nOrang Terpelajar: Untuk menangani masalah tersebut mungkin kita bisa menyatukan seluruh bangsawan-bangsawan itu.")
        time.sleep(1)
        sy.type_effect("\nPria Berbadan Besar: Kurang menarik!!, selanjutnya.")
        time.sleep(1)
        sy.type_effect(f"\n{self.nama}: Bagaimana kalau kita membagi kekuasaan ke bangsawan di beberapa wilayah namun kekuasaan tertinggi tetap dipegang oleh raja.")
        time.sleep(1)
        sy.type_effect("\nPria Berbadan Besar: Ide yang menarik, siapa namamu?")
        time.sleep(1)
        sy.type_effect(f"\n{self.nama}: Namaku {self.nama}")
        time.sleep(1)
        sy.type_effect(f"\n{self.nama}: Kalau anda sendiri siapa?.")
        time.sleep(1)
        sy.type_effect("\nPria Berbadan Besar: Anda serius tidak tahu siapa saya?")
        time.sleep(1)
        sy.type_effect(f"\n{self.nama}: Tidak.")
        time.sleep(1)
        sy.type_effect("\nPria Berbadan Besar: Saya adalah salah satu Patih yang terhormat dari Kerajaan Majapahit")
        time.sleep(1)
        sy.type_effect(f"\n{self.nama}: Dengan ciri ciri berbadan besar dan kuat serta senantiasa membawa keris, kira kira namanya siapa ya? (berbicara dalam hati)")
        bg.status = "Bertanya-tanya"
        bg.mood = "Senang"
        bg.jendela_status()
        sg.isi_nama_patih()
        if self.nama_patih == "patih gajah mada":
            tn.nilai += 25
        else:
            tn.nilai += 0
        bg.status = "Baik"
        bg.jendela_status()
        time.sleep(1)
        sy.type_effect(f"\n{self.nama_patih}: Karena kamu sudah memberikan ide yang menarik, mari ikuti aku ke istana raja.")
        time.sleep(1)
        sy.type_effect(f"\n{self.nama}: Sekarang?.")
        time.sleep(1)
        sy.type_effect(f"\n{self.nama_patih}: Iya sekarang.")
        time.sleep(1)
    
    def menemui_raja(self):
        sy.type_effect(f"\n{self.nama} dan {self.nama_patih} pun pergi ke istana raja untuk menemui sang raja.")
        time.sleep(1)
        sy.type_effect(f"\n{self.nama_patih}: Raja inilah orang yang kita cari selama ini, orang yang akan menyelesaikan masalah wilayah kita.")
        time.sleep(1)
        sy.type_effect("\nRaja: Siapa namanya?")
        time.sleep(1)
        sy.type_effect(f"\n{self.nama_patih}: Namanya adalah {self.nama}.")
        time.sleep(1)
        sy.type_effect(f"\nRaja: Hai {self.nama}, aku adalah raja dari kerajaan ini. Namaku adalah......")
        time.sleep(1)
        sg.isi_nama_raja()
        if self.nama_raja == "raja hayam wuruk":
            tn.nilai += 25
        else:
            tn.nilai += 0
        bg.jendela_status()
        time.sleep(1)
        sy.type_effect(f"\n{self.nama_raja}: Apa ide yang kamu usulkan agar bisa menangani permasalahan itu?.")
        time.sleep(1)
        sy.type_effect(f"\n{self.nama}: Kita bisa membagi kekuasaan ke bangsawan di beberapa wilayah namun kekuasaan tertinggi tetap dipegang oleh raja.")
        time.sleep(1)
        sy.type_effect(f"\n{self.nama_raja}: Memang ide yang menarik, apa permintaanmu?")
        time.sleep(1)
        sy.type_effect(f"\n{self.nama}: Permintaan saya adalah tolong kembalikan saya ke asal saya, lebih tepatnya tahun 2025.")
        bg.status = "Berharap"
        bg.jendela_status()
        time.sleep(1)
        sy.type_effect("\nTiba-tiba seorang Cendikiawan disebelah raja tiba-tiba ikut berkata.")
        time.sleep(1)
        sy.type_effect("\nCendikiwan: Ternyata kamu yang dibicarakan oleh pria tua itu.")
        time.sleep(1)
        sy.type_effect(f"\n{self.nama}: Pria tua? maksudmu pria tua yang kutemui di jalan itu?")
        bg.status = "Penasaran"
        bg.jendela_status()
        time.sleep(1)
        sy.type_effect("\nCendikiawan: Mungkin iya, Pria tua itu berkata bahwa akan ada seorang lelaki yang akan menangani permasalahan wilayah di Kerajaan Majapahit. Pria tua itu memberi buku ke raja dan berpesan; kalau dia sudah datang beri buku ini kepada dia.")
        time.sleep(1)
        sy.type_effect(f"\n{self.nama}: Apaaaa?")
        bg.status = "Penasaran"
        bg.mood = "kaget"
        bg.jendela_status()
        time.sleep(1)
        sy.type_effect(f"\n{self.nama}: Sebentar, harusnya informasi ini sangat penting bukan?. Kalau begitu kamu adalah salah satu orang kepercayaan raja, Siapa namamu?")
        time.sleep(1)
        sy.type_effect("\nCendikiawan: Aku adalah orang yang menerbitkan atau membuat Kitab Sutasomo. Dan mempunyai gelar Mpu")
        time.sleep(1)
        sg.isi_nama_mpu_()
        if self.nama_mpu == "mpu tantular":
            tn.nilai += 25
        else:
            tn.nilai += 0
        bg.jendela_status()
        time.sleep(1)
        sy.type_effect(f"\n{self.nama}: Kamu adalah {self.nama_mpu} bukan?")
        time.sleep(1)
        sy.type_effect(f"\n{self.nama_mpu}: Benar namaku {self.nama_mpu}")
        time.sleep(1)
        sy.type_effect(f"\n{self.nama_raja}: Sudah cukup perkenalannya, karena kamu sudah memberikan kontribusi ke negara ini. Kuanugrahi kamu dengan nama Raden {self.nama} dan ini buku yang dijanjikan Pria Tua itu.")
        time.sleep(1)
        sy.type_effect(f"\n{self.nama}: Terimakasih wahai {self.nama_raja}, saya dengan senang hati menerima hadiah ini.")
        time.sleep(1)
        sy.type_effect(f"\n{self.nama_raja}: Sama sama")
        time.sleep(1)
        sy.type_effect(f"\nSaat aku membuka buku itu, tiba-tiba sebuah lubang hitam muncul tepat di depanku.")
        time.sleep(1)
        sy.type_effect(f"\n{self.nama_mpu}: Masuklah segera ke lubang hitam itu, dia akan mengembalikanmu ke tempat asalmu")
        sy.type_effect(f"\nDengan wajah penuh kebingungan akupun segera masuk ke lubang hitam itu dan berharap bisa kembali ke tempat asalku.")
        bg.status = "Keheranan"
        bg.mood = "Panik"
        bg.jendela_status()
        time.sleep(1)

    def akhir_cerita(self):
        sy.type_effect(f"\n{self.nama}: Kek apa maksudnya itu, kekk!!!!, kakek!!!!!!.")
        bg.status = "Keheranan"
        bg.mood = "Kaget"
        bg.jendela_status()
        time.sleep(1)
        sy.type_effect("\nKak Fajar: Hei.....bangunlah....")
        time.sleep(1)
        sy.type_effect("\nSontak akupun terbangun dari tidurku!!, sambil mengusap air liurku.")
        bg.mood = "Kaget"
        bg.jendela_status()
        time.sleep(1)
        sy.type_effect(f"\n{self.nama}: Itu pasti hanya sebuah mimpi, hahahahah!!! (berbicara dalam hati)")
        bg.status = "Sedikit Gila"
        bg.mood = "Kaget"
        bg.jendela_status()
        time.sleep(1)
        sy.type_effect("\nKak Fajar: Anak-anak mari kita pergi ke Museum Trowulan.")
        time.sleep(1)
        sy.type_effect("\nAku dan Teman-temanku: Baik kak!!")
        time.sleep(1)
        sy.type_effect("\nAkupun pergi ke Museum Trowulan bersama Kak Fajar dan teman-teman sekelasku. .")
        time.sleep(1)
        sy.type_effect("\nSesampainya di Museum Trowulan, aku dan teman-temanku melihat-lihat bekas peninggalan Kerajaan Majapahit.")
        time.sleep(1)
        sy.type_effect(f"\nSaat sedang melihat-lihat, aku penasaran dengan lukisan wajah yang bernama {self.nama_patih}.\nSambil penasaran aku bertanya ke Kak Fajar.")
        bg.mood = "Senang"
        bg.status = "Penasaran"
        bg.jendela_status()
        time.sleep(1)
        sy.type_effect(f"\n{self.nama}: Kak Fajar!!, Kalo boleh tahu siapakah {self.nama_patih} itu?.")
        time.sleep(1)
        sy.type_effect(f"\nKak Fajar: {self.nama_patih} adalah salah satu jenderal dan penasihat paling terkenal dari Kerajaan Majapahit.\nIa dikenal melalui Sumpah Palapa yang diucapkannya, serta perannya yang besar dalam membantu Majapahit\nmenaklukkan dan menyatukan banyak wilayah di Nusantara.")
        time.sleep(1)
        sy.type_effect(f"\nAku: Ohh, jadi {self.nama_patih} adalah orang yang sangat terkenal pada masanya ya?.")
        time.sleep(1)
        sy.type_effect(f"\nKak Fajar: Iya jadi dulu {self.nama_patih} memang terkenal karena perannya dalam menyatukan wilayah nusantara.")
        bg.status = "Baik"
        time.sleep(1)
        sy.type_effect(f"\n{self.nama}: Sebentar bukankah nama tokoh ini agak familiar?")
        bg.status = "Bertanya tanya"
        bg.mood = "Kaget"
        bg.jendela_status()
        time.sleep(1)
        sy.type_effect(f"\nKak Fajar: Oh maksudmu tokoh bernama Raden {self.nama}? dia adalah kontributor dari Kerajaan Majapahit. Kontribusinya adalah dia menemukan kebijakan pembagian wilayah antar bangsawan kerajaan, yang menjadi pelopor sistem kebijakan provinsi saat ini.")
        time.sleep(1)
        sy.type_effect(f"\n{self.nama}: Bukankah itu ideku? dan namanya juga nama yang dihadiahkan oleh {self.nama_raja}? (bicara dalam hati).")
        time.sleep(1)
        sy.type_effect(f"\n{self.nama}: Ternyata pengalaman itu bukan mimpi, melainkan kenyataan!! (berbicara dalam hati).")
        bg.status = "Keheranan"
        bg.mood = "Kaget"
        bg.jendela_status()
        time.sleep(1)
        sy.type_effect("\nKak Fajar: Baik anak-anak karena waktu kita sudah habis mari kita kembali kesekolah.")
        time.sleep(1)
        sy.type_effect("\nAku dan Teman-temanku: Baik kak!!.")
        time.sleep(1)
        sy.type_effect("\nAkupun kembali kesekolah dengan wajah penuh kebingungan dan keheranan serta berharap kejadian itu tidak akan pernah terulang kembali dalam hidupku.") 
        time.sleep(1)

    def persimpangan_kiri(self):
        sy.type_effect("\nSetelah berjalan cukup lama tiba-tiba ada seorang pencuri yang menghampiriku")
        time.sleep(1)
        sy.type_effect("\nPencuri: Serahkan semua barangmu!!.")
        time.sleep(1)

    def kabur_pencuri(self):
        # time.sleep(1)
        sy.type_effect("\nSetelah kabur cukup jauh akhirnya aku menemukan sebuah kerajaan yang besar nan megah.")
        bg.status = "Lega"
        bg.mood = "Senang"
        bg.jendela_status()
        time.sleep(1)
        sy.type_effect("\nTiba-tiba ada seorang pria tua menghampiriku, ia menatapku sambil keheranan.")
        time.sleep(1)
        sy.type_effect("\nPria Tua: Hei, siapa namamu? kenapa bajumu berbeda dengan kami?")
        time.sleep(1)
        sg.isi_nama()
        time.sleep(1)
        sy.type_effect(f"\nAku: Namaku {self.nama}")
        time.sleep(1)
        sy.type_effect(f"\n{self.nama}: Maaf kek, kalo boleh tahu ini dimana ya?")
        bg.status = "Penasaran"
        bg.jendela_status()
        time.sleep(1)
        sy.type_effect("\nPria Tua: Sepertinya kamu memang bukan orang sini, nama tempat ini adalah Kerajaan Majapahit.")
        time.sleep(1)
        sy.type_effect(f"\n{self.nama}]: Bagaimana mungkin aku berada di Kerajaan Majapahit?, bukannya kerajaan itu ada masa lalu (berbicara di dalam hati). ")
        bg.mood = "kaget"
        bg.jendela_status()
        time.sleep(1)
        sy.type_effect(f"\n{self.nama}: Kerajaan Majapahit ada sekitar tahun berapa ya aku lupa!!, harusnya aku mendengarkan penjelasan Kak Fajar tadi.")
        time.sleep(1)
        jawab_tahun_2 = input("\nKerajaan Majapahit ada sekitar tahun? (contoh jawaban: 1570 hingga 1789 masehi): ").strip()
        if jawab_tahun_2 == "1293 hingga 1527 masehi":
            tn.nilai += 25
        else:
            tn.nilai += 0
        time.sleep(1)
        sy.type_effect(f"\n{self.nama}: Oh aku ingat, Kerajaan Majapahit ada sekitar {jawab_tahun_2}")
        time.sleep(1)
        sy.type_effect("\nPria Tua: Sekedar saran saja, jika kau ingin kembali ke tempat asalmu, carilah orang berbadan besar dan kuat serta senantiasa membawa keris")
        time.sleep(1)
        sy.type_effect("\nPria Tua: Mungkin dia bisa mengembalikanmu ke tempat asalmu.")
        time.sleep(1)
        sy.type_effect(f"\n{self.nama}: Kek, maksudnya apa kek?")
        time.sleep(1)
        sy.type_effect("\nSaat aku mengedipkan mata secara ajaib Pria Tua itu menghilang  entah kemana.")
        bg.status = "Penasaran"
        bg.mood = "Panik"
        bg.jendela_status()
        time.sleep(1)

    def lawan_pencuri(self):
        sy.type_effect("\nAku: Sini lawan aku pencuri, aku tidak sudi memberikan barangku kepadamu.")
        time.sleep(1)
        sy.type_effect("\nPencuri: Oh ya? baiklah sini lawan aku.")
        sy.type_effect("\nKarena perbedaan fisik yang cukup signifikan, akhirnya kamu terbunuh dan dikirim kembali ke tempat asalmu.")
        bg.status = "Meninggal"
        bg.mood = "-"
        bg.jendela_status()
        time.sleep(1)

    def pasrah_pencuri(self):
        sy.type_effect("\nAku: Menyerah, saya menyerah ini semua barang saya termasuk pakaian saya!!.")
        time.sleep(1)
        sy.type_effect("\nPencuri: Nah gitu dong, mana semua barangmu!!")
        time.sleep(1)
        sy.type_effect("\nDengan pasrah akupun memberikan semua barangku termasuk pakaianku kepada pencuri itu, kemudia pencuri itu meninggalkanku begitu saja.")
        bg.status = "Pasrah"
        bg.mood = "Kaget"
        bg.jendela_status()
        time.sleep(1)
        sy.type_effect("\nMalam sudah tiba, karena semua barang termasuk pakaianku sudah kuberikan pencuri itu. Aku mengalami Hipotermia, sebab suhu yang sangat dingin di hutan. Tiba-tiba aku kehilangan kesadaran dan mati di tempat.")
        bg.status = "Meninggal karena kedinginan"
        bg.mood = "-"
        bg.jendela_status()
        time.sleep(1)

    def tidak_ikuti_saran(self):
        sy.type_effect(f"\n{self.nama}: Apasih maksud dari kakek itu? lebih baik aku berkeliling saja")
        bg.status = "Keheranan"
        bg.mood = "Tidak Senang"
        bg.jendela_status()
        time.sleep(1)
        sy.type_effect("\n3 Hari berlalu aku masih tetap menelusuri kerajaan yang megah ini, tiba-tiba jendela nontifikasi yang sama datang menhampiriku, ia berkata; ")
        time.sleep(1)

    def belum_sempat(self):
        sy.type_effect("\nTiba-tiba muncullah sebuah lubang hitam yang menarik diriku masuk.")
        time.sleep(1)
        sy.type_effect("\nPria Tua: Karena kamu belum sempat menyelesaikannya aku akan mengirimmu ke asalmu dan menghapus ingatanmu tentang kejadian ini.")
        time.sleep(1)
        sy.type_effect(f"\nAku: Kek apa maksudnya itu, kekk!!!!, kakek!!!!!!.")
        bg.status = "Bertanya-tanya"
        bg.mood = "Kaget"
        bg.jendela_status()
        time.sleep(1)

    def petunjuk(self):
        sy.type_effect("\nTentang Game:\n\nJudul: Petualangan Di Era Majapahit\nTema Game: Story (Petualangan Di Era Majapahit)\nGenre: Fantasi, Misteri, Advanture, Fiksi, Role-Play\n\nCara Bermain:\n\n1.Pilih opsi yang sudah ditentukan\n2.Usahakan memilih opsi yang sudah ditentukan (jangan memilih yang tidak tertera)\n3.Setiap pilihan akan mempengaruhi hasil kedepannya\n4.Bijaklah dalam memilih opsi, karena akan berpengaruh ke akhir cerita\n5.Jawab pertanyaan dengan benar agar mendapatkan nilai yang bagus\n6.Terdapat 4 soal dengan masing masing memiliki nilai 25 poin\n7.Selamat bermain\n\n")

sg = story_game()


if __name__ == "__main__":
    sg = story_game()
    sg.story_awal()
    sg.story_awal_tidak()
    sg.persimpangan_kanan()
    sg.ikuti_saran()
    sg.tidak_ikuti_saran()
    sg.persimpangan_kiri()
    sg.lawan_pencuri()
    sg.belum_sempat()
    sg.pasrah_pencuri()
    sg.kabur_pencuri()
    sg.menemui_raja()
    sg.story_awal_iya()
    sg.petunjuk()