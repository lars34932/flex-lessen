import io
bestand = io.open("hallo.txt", "w")
bestand.write("Test 123!")
bestand.close()