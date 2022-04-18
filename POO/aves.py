#otra mane
class AnimalesAlados():
  def esta_feliz(self):
    return self.energia > 500

class Golondrina(AnimalesAlados):
  def __init__(self, energia):
    self.energia = energia

  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos

  def volar_en_circulos(self):
    self.volar(0)

  def volar(self, kms):
    self.energia -= 10 + kms
#Debil y feliz
  def esta_debil(self):
    return self.energia < 10


class Dragon(AnimalesAlados):     
  def __init__(self, cantidad_dientes, energia):
    self.energia = energia
    self.cantidad_dientes = cantidad_dientes

  def escupir_fuego(self):
    self.energia -= 2 * self.cantidad_dientes

  def comer_peces(self, unidades):
    self.energia += 100 * unidades

  def volar_en_circulos(self):
    self.energia -= 1

  def volar(self, kms):
    self.energia -= 10 + kms/10
# Debil y feliz
  def esta_debil(self):
    return self.energia < 50

pepita = Golondrina(100)
anastasia = Golondrina(200)
roberta = Dragon(10, 1000)
# Crear a maria y chimuelo.
maria = Golondrina(200)
chimuelo = Dragon(200, 1000)


class Entrenador: 
  "Un entrenador tiene un equipo y opuede admitir nuevos animales"
  def _init_(self, equipo):
    self.equipo = equipo

  def el_equipo(self):
    return self.equipo

  def agregar_animal(self, animal):
    self.equipo.append(animal)

  def entrenar_dragon(self, dragon):
    for i in range(20):
      dragon.volar_en_circulos()
    dragon.comer_peces(3)

  def entrenar_equipo(self):
    for dragon in self.equipo:
      self.entrenar_dragon

hipo = Entrenador([roberta])