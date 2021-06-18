import random

print("""Tebak angka berdasarkan baris dari angka yang kamu mau!
Cobalah untuk menebak angka yang telah dibuat secara acak oleh program ini dalam 5 kali percobaan.
Perlu diingat untuk memasukkan angka dari yang terkecil hingga terbesar!
""")

try:
  def guess_game():
    print("==================================")
    print("Mau tebak angka dari berapa sampai berapa ?")
    first_input = int(input("Dari: "))
    second_input = int(input("Sampai: "))
    if second_input < first_input:
      print("Tolong Masukkan Angka yang Benar! Angka kedua tidak boleh lebih kecil dari Angka pertama")
      restart_game()
    number = random.randint(first_input, second_input)
    guess_chance = 0
    print("Waktunya Menebak!")
    print(f"Pilihan Angka Kamu: Dari {first_input} sampai {second_input}. Semoga Beruntung!")
    while guess_chance < 5:
      guess_chance += 1
      guess_number = int(input("Tebakan Angka: "))
      if guess_number < first_input:
        print(f"Kamu tidak boleh menebak angka yang lebih kecil dari pilihan kamu! Angka terkecil yang kamu pilih adalah {first_input}")
      elif guess_number > second_input:
        print(f"Kamu tidak boleh menebak angka yang diluar dan lebih besar dari pilihan kamu! Angka Terbesar yang kamu pilih adalah {second_input}")
      elif guess_number > number:
        print("Angka yang kamu masukkan sepertinya terlalu tinggi. Coba Lagi!")
      elif guess_number < number:
        print("Angka yang kamu masukkan sepertinya terlalu rendah. Coba Lagi!")
      elif guess_number == number:
        print(f"Selamat! Tebakanmu tepat, angkanya {number}")
        restart_game()
        break
    else:
      print(f"Kamu Sudah menebak lebih dari 5 kali! Sayang sekali tebakanmu kurang tepat, angka yang benar adalah {number}")
      restart_game()

  def restart_game():
    restart = str(input("Mau main Lagi ? [Y/N]: "))
    if restart == "Y" or restart == "y":
      guess_game()
    elif restart == "N" or restart == "n":
      print("Terima Kasih sudah Bermain!")
    else:
      print("Anda Tahu ? Anda baru saja mengetik sesuatu yang tidak dimengerti oleh Program ini!")
  guess_game()

except ValueError:
  print("Error! Hanya dapat menerima input Angka! Program dihentikan.")
  restart_game()
except SyntaxError:
  print("!!!!!!!!!!!!!!!!!!!!!!")

