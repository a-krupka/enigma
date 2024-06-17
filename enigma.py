from rotory import rotor1,rotor2,rotor3,rotor4,rotor5,pis_cis,cis_pis,ref_B,inv_rotor1,inv_rotor2,inv_rotor3,inv_rotor4,inv_rotor5,inv_rotor1_keys,inv_rotor2_keys,inv_rotor3_keys,inv_rotor4_keys,inv_rotor5_keys
import string

#for cislo,haf in zip(range(1,6),["EKMFLGDQVZNTOWYHXUSPAIBRCJ","AJDKSIRUXBLHWTMCQGZNPYFVOE","BDFHJLCPRTXVZNYEIWGAKMUSQO","ESOVPZJAYQUIRHXLNFTGKDCMWB","VZBRGITYUPSDNHLXAWMJQOFECK"]):
#       print(f"inv_rotor{cislo} = ","[")
#       for i,j in zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",haf):
#           print('[{'+f'"{j}":"{i}"'+'},'+'""],')
#       print("]")


#print(rotor1[0])
#rotor1.sort(key=rotor1[0].__eq__) # přesune instanci nakonec
#print(rotor1[0])
#a= rotor1[1][0].values()
#print(a)

#for j,i in zip(range(26),string.ascii_uppercase):
#       print(f'"{i}":{j},')
plug_dict = {}
while True:
       a = input("Enter letters to plugboard in format 'xx' to exit press X: ").capitalize()
       if a == "x".upper():
              break
       if len(a) == 2:
              a = list(a.upper())
              b,c = a
              if (b and c) in string.ascii_letters and b!=c:
                     plug_dict[b] = c

print(plug_dict)
inv_plug_dict = {}
for keys,values in plug_dict.items():
       inv_plug_dict[values] = keys
print(inv_plug_dict)


rotor1 = rotor1
rotor2 = rotor2
rotor3 = rotor3
inv_rotor1 = inv_rotor1
inv_rotor2 = inv_rotor2
inv_rotor3 = inv_rotor3
inv_rotor1_keys = inv_rotor1_keys
inv_rotor2_keys = inv_rotor2_keys
inv_rotor3_keys = inv_rotor3_keys

while True:
       pozice_P = int(input("Stanovte počáteční číslo (1-26) na rotoru 1: ")) - 1
       if not 0 <= pozice_P <= 25:
              continue
       pozice_M = int(input("Stanovte počáteční číslo (1-26) na rotoru 2: ")) - 1
       if not 0 <= pozice_M <= 25:
              continue
       pozice_L = int(input("Stanovte počáteční číslo (1-26) na rotoru 3: ")) - 1
       if not 0 <= pozice_L <= 25:
              continue
       break



def position(letter,pos):
       sum = pis_cis[letter] + pos
       if sum > 25:
              sum -= 26 #opravit
       return cis_pis[sum]
def inverted_position(letter,pos):
       sum = pis_cis[letter] - pos
       if sum < 0:
              sum += 26 #opravit
       return cis_pis[sum]
def plusone(number):
       number += 1
       if number > 25:
              number -= 26 #opravit
       return number

#print(position("R",pozice))

decyphered = ""
text = "ybkak mfmeu c" #Tohle je zkouska"
for i in text.upper().replace(" ",""):
       if i in plug_dict:
              i = plug_dict[i]
       elif i in inv_plug_dict:           # Plugboard goes both ways
              i = inv_plug_dict[i]
       pozice_P = plusone(pozice_P)
       if rotor1[pozice_P][1] != "":
              pozice_M = plusone(pozice_M)
       if rotor2[pozice_M][1] != "":
              pozice_L = plusone(pozice_L)
       rot1 = rotor1[pis_cis[position(i,pozice_P)]][0][position(i,pozice_P)]
       rot1 = inverted_position(rot1,pozice_P) #pozice pravá
       rot1 = position(rot1,pozice_M) #pozice levá
       rot2 = rotor2[pis_cis[rot1]][0][rot1]#rotor2[pis_cis[position(rot1,pozice_M)]][0][position(rot1,pozice_M)]
       rot2 = inverted_position(rot2, pozice_M)
       rot2 = position(rot2,pozice_L)
       rot3 = rotor3[pis_cis[rot2]][0][rot2]
       rot3 = inverted_position(rot3,pozice_L)

       reflector = ref_B[rot3]
       reflector = position(reflector,pozice_L)

       rot4 = inv_rotor3[inv_rotor3_keys.index(reflector)][0][reflector]
       rot4 = inverted_position(rot4,pozice_L)
       rot4 = position(rot4, pozice_M)
       rot5 = inv_rotor2[inv_rotor2_keys.index(rot4)][0][rot4]
       rot5 = inverted_position(rot5,pozice_M)
       rot5 = position(rot5,pozice_P)
       rot6 = inv_rotor1[inv_rotor1_keys.index(rot5)][0][rot5]
       rot6 = inverted_position(rot6,pozice_P)
       if rot6 in plug_dict:
              rot6 = plug_dict[rot6]
       elif rot6 in inv_plug_dict:
              rot6 = inv_plug_dict[rot6]
       decyphered += rot6
       #print(rot6)
       #print(rot1,rot2,rot3,reflector,rot4,rot5,rot6,sep="\n")

print(decyphered)

