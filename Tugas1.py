while True:
  try:
    num = float(input("Masukkan Bilangan: "))
    if num >= 0 or num < 0:
        if num >= 0:
            if num == 0:
                print("Bilangan ini bernilai Nol")
            else:
                print("Bilangan ini adalah bilangan positif")
        else:
            print("Bilangan ini adalah bilangan Negatif")
        break
     
    print("Bilangan yang diinput Invalid, Harus Angka")
  except Exception as e:
    print("Bilangan yang diinput Invalid, Harus Angka")
