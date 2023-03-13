import csv 
import datetime


#Pizzalarin menudeki numaralari, isimleri, fiyatlari ve aciklamalari bu class ile tanimlanmistir.
class Pizza:

  def __init__(self, no, pname, cost, description):
    self.no = no
    self.pname = pname
    self.cost = cost
    self.description = description
  
  #fiyat ve aciklamalarin dondurulmesi icin get_cost ve get_description methodlari kullanilmistir.
  def get_cost(self):
    return self.cost

  def get_description(self):
    return self.cost

#Inheritance mantigi ile Pizza sinifinin methodlari aktarilmistir.
class Klasik(Pizza):
  pass
Klasik_Pizza = Klasik(1, "Klasik Pizza", 20, "Classic for Classic Lovers")

class Margherita(Pizza):
  pass
Margherita_Pizza = Margherita(2, "Margherita Pizza", 22, "Margherita for Margherita Lovers")

class Sade(Pizza):
  pass
Sade_Pizza = Sade(3, "Sade Pizza", 24, "Sade for Sade Lovers")

class Turk(Pizza):
  pass
Turk_Pizza = Turk(4, "Turk Pizza", 26, "Turk Pizza for Turk Pizza Lovers")

#Sos sinifina da Pizza sinifinin methodlari inheritance mantigi ile aktarilmistir.
class Sauce(Pizza):
  pass
olive = Sauce(11, "Zeytin", 3, "Zeytin ilavesi")
mushroom = Sauce(12, "Mantar", 4, "Mantar ilavesi")
goat_cheese = Sauce(13, "Keci Peyniri", 5, "Keci Peyniri Ilavesi")
meat = Sauce(14, "Et", 7, "Et Ilavesi")
onion = Sauce(15, "Sogan", 6, "Sogan Ilavesi")
corn = Sauce(16, "Misir", 8, "Misir Ilavesi")

#Menu.txt dosyasini acmak icin kullanilmistir.
with open('Menu.txt') as Menu:
  PizzaMenu = Menu.read()

#Main fonksiyonu ile Menu gosterilmistir. 
def main():
  print("Aydogan Pizza'ya hoşgeldiniz !!! Menüyü inceleyerek pizzanıza karar verebilirsiniz. \n" )
  print(PizzaMenu)

#Pizza secimi bu fonksiyon icerisinde yapilmistir.
def pizza_sel():
  
  price = 0
  user_info = []
  Pizzanum = int(input("Lutfen Pizzanizi Seciniz: "))

  if Pizzanum == 1:
    print(f"Secilen Pizza: {Klasik_Pizza.pname}")
    user_info.append(Klasik_Pizza.pname)
    price += Klasik_Pizza.cost
  if Pizzanum == 2:
    print(f"Secilen Pizza: {Margherita_Pizza.pname}")
    user_info.append(Margherita_Pizza.pname)
    price += Margherita_Pizza.cost
  if Pizzanum == 3:
    print(f"Secilen Pizza: {Sade_Pizza.pname}")
    user_info.append(Sade_Pizza.pname)
    price += Sade_Pizza.cost
  if Pizzanum == 4:
    print(f"Secilen Pizza: {Turk_Pizza.pname}")
    user_info.append(Turk_Pizza.pname)
    price += Turk_Pizza.cost

main()
pizza_sel()

