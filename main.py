import menu
import utils

TOTAL_POPULATION = int(7.794*(10**9))
BIRTH_PER_DAY = 4000
DEATH_BY_COVID = 5000 #faux au moment où j'écris (29/10/20)

print("---- Quelques infos ----")
print(f"Population totale : {utils.format_int(TOTAL_POPULATION)} habitants", f"Naissances par jour : {BIRTH_PER_DAY}", f"Morts du covid par jour : {DEATH_BY_COVID}", sep='\n')

def population_remain(k):
    result = TOTAL_POPULATION+(BIRTH_PER_DAY-DEATH_BY_COVID)*k
    print(f"{utils.format_int(result)} personnes survivront après {k} jours (soit {utils.format_int(TOTAL_POPULATION-result)} morts)")

def days_remain(k):
    result = (k-TOTAL_POPULATION)/(BIRTH_PER_DAY-DEATH_BY_COVID)
    print(f"{result} jours (soit {result//365} ans et {result%365} jours) passeront avant que la population soit de {utils.format_int(k)} habitants")

options = [population_remain, days_remain]

while True:
    index, _ = menu.open_menu("Menu", ['Population restante en fonction de k jours', 'Jours restants avant que la population soit inférieure à k', 'quitter'])
    print("")
    if index >= len(options):
        print("A bientôt !")
        exit()
    k = eval(input("k : "))
    print("")
    options[index](k)
    print("")