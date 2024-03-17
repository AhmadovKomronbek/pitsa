print("""
███████ ██    ██ ██████  ███████ ██████      ██████  ██ ███████ ███████  █████  ███████ 
██      ██    ██ ██   ██ ██      ██   ██     ██   ██ ██    ███     ███  ██   ██ ██      
███████ ██    ██ ██████  █████   ██████      ██████  ██   ███     ███   ███████ ███████ 
     ██ ██    ██ ██      ██      ██   ██     ██      ██  ███     ███    ██   ██      ██ 
███████  ██████  ██      ███████ ██   ██     ██      ██ ███████ ███████ ██   ██ ███████ 
                                                                                        
                                                                                        
""")
print("Menyu")
print("           " + "Nomi" + "               " + "Puli"+"          "+"pitsa uchun pishloq narxi"+"          "+"pitsa uchun qalampir narxi")
print("1          " + "Big pizza" + "          " + "12$"+"           "+"3$"+"                                 "+"3$")
print("2          " + "Medium pizza" + "       " + "11$"+"           "+"2$"+"                                 "+"2$")
print("3          " + "Small pizza" + "        " + "10$"+"           "+"1$"+"                                 "+"1$")
print("Yetkazib berish 5$")
class Pitsamaker:
  def __init__(pitsaname, money, cheesemoney , peppermoney):
    pitsaname.money = money
    pitsaname.cheesemoney = cheesemoney
    pitsaname.peppermoney = peppermoney

Bigpitsa = Pitsamaker(12, 3 , 3)
Mediumpitsa = Pitsamaker(11, 2 , 2)
Smallpitsa = Pitsamaker(10, 1 , 1)
pizza_nomi = input("Qanaqa pizzani buyurtma qilasiz? ")
money=0
if pizza_nomi=="Big pizza" or pizza_nomi=="big pizza" or pizza_nomi=="Medium pizza" or pizza_nomi=="medium pizza" or pizza_nomi=="Small pizza" or pizza_nomi=="small pizza":
  if pizza_nomi == "Big pizza" or pizza_nomi == "big pizza":
    Changepitsa = Bigpitsa
  elif pizza_nomi == "Medium pizza" or pizza_nomi == "medium pizza":
    Changepitsa = Mediumpitsa
  else:
    Changepitsa = Smallpitsa
  print(f"Bu pizzaning puli {Changepitsa.money}$")
  print(Changepitsa)
  YesOrNo = input("Olasizmi ? (Ha yoki yo'q) :")
  if YesOrNo == "Ha":
    money += Changepitsa.money
    print(f"Pishloq puli {Changepitsa.cheesemoney}$")
    CheeseYesOrNo = input("Pishloq solaymi ? (Ha yoki Yo'q) :")
    if CheeseYesOrNo == "Ha":
      money += Changepitsa.cheesemoney
    print(f"Qalampir puli {Changepitsa.peppermoney}$")
    PepperYesOrNo = input("Qalampir solaymi ? (Ha yoki Yo'q) :")
    if PepperYesOrNo == "Ha":
      money += Changepitsa.peppermoney
    Dostavka = input("Yetkazib berylikmi ? (Ha yoki Yo'q)")
    if Dostavka == "Ha":
      money+=5
    print(f"Jammi hisob {money}$ bo'ldi")

  else:
    print("Orqaga qaytish")
else:
    print("Bunday pizza mavjud emas")