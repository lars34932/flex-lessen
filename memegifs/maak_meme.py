from PIL import Image, ImageFont, ImageDraw

achtergrond = Image.open("download.jfif")
lettertype = ImageFont.truetype("impact.ttf", 40)
tekengebied = ImageDraw.Draw(achtergrond)

tekst=""

tekst_breedte, tekst_hoogte = tekengebied.textsize(tekst, font=lettertype) 
print("tekstbreedte=" + str(tekst_breedte) + ", tekst_hoogte=" + str(tekst_hoogte))

breedte = achtergrond.width
hoogte = achtergrond.height

nieuwe_breedte = breedte * 2
nieuwe_hoogte = hoogte * 2

nieuwe_afmeting = (nieuwe_breedte, nieuwe_hoogte)

tekst_x = (breedte - tekst_breedte) / 2
tekst_y = (hoogte - tekst_hoogte) / 2

tekst = "yeet"
tekengebied.multiline_text((tekst_x-25, tekst_y+45), tekst, font=lettertype, fill=(255,255,255))

grote_achtergrond = achtergrond.resize(nieuwe_afmeting)

grote_achtergrond.show()

