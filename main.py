p = [" " for _ in range(10)]

p[1]=" "
p[2]=" "
p[3]=" "
p[4]=" "
p[5]=" "
p[6]=" "
p[7]=" "
p[8]=" "
p[9]=" "

n=0
w=0


def testanswer(Choix):
  if Choix >= 1 and Choix <= 9 :
    if p[Choix]==" " :
      return True
  print(" ")
  print("Saisie Incorrecte")
  print(" ")
  return False


print(" " "1"+ p[1] + "| " "2"+ p[2] + "| " "3"+ p[3] + " ")
print("---+---+---")
print(" " "4"+ p[4] + "| " "5"+ p[5] + "| " "6"+ p[6] + " ")
print("---+---+---")
print(" " "7"+ p[7] + "| " "8"+ p[8] + "| " "9"+ p[9] + " ")
print("   ")


print(" " + p[1] + " | " + p[2] + " | " + p[3] + " ")
print("---+---+---")
print(" " + p[4] + " | " + p[5] + " | " + p[6] + " ")
print("---+---+---")
print(" " + p[7] + " | " + p[8] + " | " + p[9] + " ")
print("   ")

Win=False

while Win==False :
 while True :
  Joueur1= int(input("Joueur 1, quelle case choisis-tu ?"))
  Test=testanswer(Joueur1)
  if Test :
      p[Joueur1]="X"
      n=n+1

  print(" " + p[1] + " | " + p[2] + " | " + p[3] + " ")
  print("---+---+---")
  print(" " + p[4] + " | " + p[5] + " | " + p[6] + " ")
  print("---+---+---")
  print(" " + p[7] + " | " + p[8] + " | " + p[9] + " ")
  print("   ")

  if p[1]==p[2]==p[3]=='X' or p[4]==p[5]==p[6]=='X' or p[7]==p[8]==p[9]=='X' or p[1]==p[5]==p[9]=='X' or  p[7]==p[3]==p[5]=='X' or p[8]==p[5]==p[2]=='X' or p[1]==p[4]==p[7]=='X' or p[3]==p[6]==p[9]=='X'or p[1]==p[2]==p[3]=='O' or p[4]==p[5]==p[6]=='O' or p[7]==p[8]==p[9]=='O' or p[1]==p[5]==p[9]=='O' or  p[7]==p[3]==p[5]=='O' or p[8]==p[5]==p[2]=='O' or p[1]==p[4]==p[7]=='O'or p[3]==p[6]==p[9]=='O' :
    Win=True
  if Test :
    break

 if n==9 :
     if p[1]==p[2]==p[3]=='X' or p[4]==p[5]==p[6]=='X' or p[7]==p[8]==p[9]=='X' or p[1]==p[5]==p[9]=='X' or  p[7]==p[3]==p[5]=='X' or p[8]==p[5]==p[2]=='X' or p[1]==p[4]==p[7]=='X' or p[3]==p[6]==p[9]=='X'or p[1]==p[2]==p[3]=='O' or p[4]==p[5]==p[6]=='O' or p[7]==p[8]==p[9]=='O' or p[1]==p[5]==p[9]=='O' or  p[7]==p[3]==p[5]=='O' or p[8]==p[5]==p[2]=='O' or p[1]==p[4]==p[7]=='O'or p[3]==p[6]==p[9]=='O' :
      Win=True
     if Win==True : 
       break
     else :  
       print ('Match nul !')
       w=9
       Win=True
 
 while True and not Win :
  Joueur2= int(input("Joueur 2, quelle case choisis-tu ?"))
  Test=testanswer(Joueur2)
  if Test :
      p[Joueur2]="O"
      n=n+1

  print(" " + p[1] + " | " + p[2] + " | " + p[3] + " ")
  print("---+---+---")
  print(" " + p[4] + " | " + p[5] + " | " + p[6] + " ")
  print("---+---+---")
  print(" " + p[7] + " | " + p[8] + " | " + p[9] + " ")
  print("   ")

  if p[1]==p[2]==p[3]=='O' or p[4]==p[5]==p[6]=='O' or p[7]==p[8]==p[9]=='O' or p[1]==p[5]==p[9]=='O' or  p[7]==p[3]==p[5]=='O' or p[8]==p[5]==p[2]=='O' or p[1]==p[4]==p[7]=='O'or p[3]==p[6]==p[9]=='O' or p[1]==p[2]==p[3]=='X' or p[4]==p[5]==p[6]=='X' or p[7]==p[8]==p[9]=='X' or p[1]==p[5]==p[9]=='X' or  p[7]==p[3]==p[5]=='X' or p[8]==p[5]==p[2]=='X' or p[1]==p[4]==p[7]=='X' or p[3]==p[6]==p[9]=='X' :
      Win=True
  if Test :
    break

if w==0 :
  print("Bravo !")