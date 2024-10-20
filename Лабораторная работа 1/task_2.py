# TODO Найдите количество книг, которое можно разместить на дискете

razmer = 1.44 #mb
stranic = 100
strok = 50
simvolov = 25
razmer_simvola = 4 #байта

razmer_knigi = simvolov * strok * stranic * razmer_simvola
razmer1 = razmer * 1024 **2
count = round(razmer1 // razmer_knigi)

print("Количество книг, помещающихся на дискету:", count)