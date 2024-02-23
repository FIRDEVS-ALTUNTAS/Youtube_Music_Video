from pytube import YouTube

link = input("Lütfen indirmek istediğiniz videonun linkini giriniz: ")
yt = YouTube(link)

print("İndirmek istediğiniz formatı seçiniz:")
print("1. Video")
print("2. Ses")

choice = input("Seçiminizi yapınız (1 veya 2): ")

if choice == '1':
    yr = yt.streams.get_highest_resolution()
    print("Video indiriliyor. Lütfen bekleyin.")
    yr.download()
    print("******************************************************")
    print("Video indirildi. İyi seyirler!")
    print("******************************************************")
elif choice == '2':
    audio_streams = yt.streams.filter(only_audio=True)
    if audio_streams:
        audio = audio_streams.get_audio_only()
        print("Ses dosyası indiriliyor. Lütfen bekleyin.")
        audio.download()
        print("******************************************************")
        print("Ses dosyası indirildi. İyi dinlemeler!")
        print("******************************************************")
    else:
        print("!!!  Bu video sadece ses içermiyor!!!")
else:
    print("!!! Geçersiz seçim. Lütfen 1 veya 2 giriniz!!!")
