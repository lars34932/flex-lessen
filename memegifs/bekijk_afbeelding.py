from PIL import Image

afbeelding = Image.open("2f0.png")

afbeelding.show()

breedte = afbeelding.width
hoogte = afbeelding.height

print("De afbeelding is " + str(breedte) + " pixels breed en " + str(hoogte) + " pixels hoog")

print(afbeelding.format, afbeelding.size, afbeelding.mode)

helft_breedte = breedte // 2
helft_hoogte = hoogte // 2

nieuwe_afmeting = (helft_breedte, helft_hoogte)

kleinere_afbeelding = afbeelding.resize(nieuwe_afmeting)

kleinere_afbeelding.save('stonks.jpg')

