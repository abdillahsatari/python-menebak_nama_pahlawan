""" Program python sederhana - Menebak nama pahlawan
contributors
Abdillah Satari Rahim
Peperangan Asimetris co.09
----------------------------------------
"""
heroLists = []
newParse = []

def guessTheHero (limit, i):
    while (i < int(limit)+1):        
        try:
            playerGuess = input(f"\nMasukkan Nama Pahlawan ke-{i}: ").upper()
            """ 
                Melakukan validasi terhadap inputan apakah inputan sudah pernah diinput atau belum dan 
                apakah elemen huruf pertamanya adalah elemen huruf terakhir dari input sebelumnya
                ----------------------------------------
            """
            if heroLists and playerGuess in heroLists:
                raise ValueError("{} sudah disebutkan".format(playerGuess))
            elif heroLists and playerGuess[0] != (heroLists[-1])[-1]:
                raise ValueError("element huruf pertamanya bukan element huruf terakhir dari tebakan sebelumnya".format(playerGuess))

            heroLists.append(playerGuess)

            # calling the user inputs recursive function
            guessTheHero(limit, i + 1)
            return

        except ValueError as e:
            print("Oh tidak!, {}. Silahkan tebak pahlawan yang lain".format(e))

def recursiveSort(list, newParse = None):
    if newParse is None:
        newParse = []
    if len(list) == 0:
        return newParse
    else:
        x = max(list)
        print(x)
        list.remove(x)
        newParse.append(x)
        # calling the data resslut recursive function
        recursiveSort(heroLists, newParse)
        return 

def main():
    print("""Nama Mahasiswa: Lailatu Qomariah\nNIM: 120200402005""")
    print("\r")
    print("""Halo petualang! Selamat datang pada permainan tebak nama pahlawan!\nMari lihat seberapa jauh kamu mengenal para pahlawan Bangsa!""")
    
    playerName = input("Siapa nama Anda? ")
    wannaPlay = input("\nHi, {}, apakah Anda ingin bermain tebak nama pahlawan? (Tulis Ya/Tidak) ".format(playerName))

    while wannaPlay.lower() == "ya":
        try:
            print("""Sebelum kita mulai menurut anda berapa banyak nama pahlawan yang dapat anda tebak?""")
            totalRound = input("Masukkan jumlah tebakan yang anda inginkan ")
            print("\nHebat! Mari Kita Mulai {}, semoga anda beruntung!".format(playerName))

            # initiate recursive function for user inputs
            guessTheHero(totalRound, i=1)
            print('Selamat anda telah berhasil menebak nama pahlawan dengan baik dan benar')
            print('Berikut adalah jawaban anda yang sudah di sorting:')
            
            # initiate recursive function for list of data result 
            afterSort = recursiveSort(heroLists)
  
            play_again = input("Apakah Anda ingin coba lagi? (Tulis Ya/Tidak) ")
            if play_again.lower() == "tidak" or play_again.lower() != "ya":
                    print("Terima kasih, sampai jumpa kembali!")
                    break

        except ValueError as err:
            print("Oh tidak!, pahlawan ini sudah disebutkan. Silahkan mencoba lagi...")
            print("({})".format(err))

    else:
        print("Sepertinya anda belum siap, Sampai jumpa kembali!")

if __name__ == '__main__':
    main()