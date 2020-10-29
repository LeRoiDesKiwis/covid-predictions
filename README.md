# Présentation
Ce programme vous permettra de calculer quelques statistiques sur le Covid-19.
Les données comme le nombre total d'habitants, le nombre de morts du covid peuvent changer entre temps.

# Comment ça marche ?
Rien de plus simple :
Démarrez tout d'abord le programme en tapant ``py main.py`` sur votre invite de commande préférée, puis choisissez ce que vous voulez faire en tapant le numéro de l'option choisie.

## Population restante en fonction de k jours
Comme son nom l'indique, cette "option" vous permettra de voir le nombre d'habitants dans le monde après k jours. Les naissances sont prises en compte dans le calcul. Seul les décès qui ont pour cause le covid-19 sont prises en compte.

## Jours restants avant que la population soit inférieure à k
Vous pouvez ici voir le nombre de jour avant que le nombre d'habitants ne soit en dessous d'un certain seuil.

# Les chiffres

# À savoir
- Le nombre de décès du covid est ici faux (à l'instant où j'écris), mais comme pour l'instant, ne nombre de décès est de à peu près 500 morts/jour et le nombre de naissances de 3000/jours, il n'y a pas de décès. J'ai donc augmenté un peu la valeur.
- Si vous trouvez des sources plus fiables, n'hésitez pas à faire une pull request.

# Sources
Vous trouverez ci-dessous les sources des chiffres utilisés (nombre total d'habitants etc) :
- [Google](https://www.google.com/search?rlz=1C1CHBF_frFR891FR891&sxsrf=ALeKk02aglzHIuzTpdWO4ZCxraXzOL0K2g%3A1603973589828&ei=1bGaX-TyMcTbgwfgwIqIDA&q=d%C3%A9c%C3%A8s+covid&oq=d%C3%A9c%C3%A8s+covid&gs_lcp=CgZwc3ktYWIQAzIECCMQJzIICAAQsQMQgwEyDQgAELEDEIMBEBQQhwIyBQgAELEDMggIABCxAxCDATIICAAQsQMQgwEyCAgAELEDEIMBMgIIADICCAAyCAgAELEDEIMBOgoIABCxAxCDARBDUIYDWJUFYNwGaABwAHgAgAH1AogB8QiSAQcwLjEuMS4ymAEAoAEBqgEHZ3dzLXdpesABAQ&sclient=psy-ab&ved=0ahUKEwiksbOg49nsAhXE7eAKHWCgAsEQ4dUDCA0&uact=5) pour le nombre de décès du covid/jour.
- [Insee](https://www.insee.fr/fr/statistiques/4277635?sommaire=4318291) pour le nombre de naissances par an (j'ai divisé par 365 pour obtenir le nombre de naissances par jour).
- [Worldometers](https://www.worldometers.info/fr/) pour un peu tous les chiffres.
- [Wikipédia](https://fr.wikipedia.org/wiki/Population_mondiale) pour le nombre d'habitants total sur Terre.