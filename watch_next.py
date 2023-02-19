import spacy

nlp = spacy.load('en_core_web_md')

Planet_Hulk_desc = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, " \
                   "the illuminati trick Hulk " \
                   "into a shuttle and lauch him into space to a planet Sakaar where he is sold into slavery and " \
                   "trained as a gladiator."

Planet_Hulk_desc = nlp(Planet_Hulk_desc)

MovieA = "When Hiccup discovers Toothless isn't the only Night Fury, he must seek \"The Hidden World\", a secret " \
         "Dragon Utopia before a hired tyrant named Grimmel finds it first."
MovieB = "After the death of Superman, several new people present themselves as possible successors."
MovieC = "A darkness swirls at the center of a world-renowned dance company, one that will engulf the artistic " \
         "director, an ambitious young dancer, and a grieving psychotherapist. Some will succumb to the nightmare. " \
         "Others will finally wake up."
MovieD = "A humorous take on Sir Arthur Conan Doyle's classic mysteries featuring Sherlock Holmes and Doctor Watson."
MovieE = "A 16-year-old girl and her extended family are left reeling after her calculating grandmother unveils an " \
         "array of secrets on her deathbed."
MovieF = "In the last moments of World War II, a young German soldier fighting for survival finds a Nazi captain's " \
         "uniform. Impersonating an officer, the man quickly takes on the monstrous identity of the perpetrators " \
         "he is trying to escape from."
MovieG = "The world at an end, a dying mother sends her young son on a quest to find the place that grants wishes."
MovieH = "A musician helps a young singer and actress find fame, even as age and " \
         "alcoholism send his own career into a downward spiral."
MovieI = "Corporate analyst and single mom, Jen, tackles Christmas with a business-like approach until her uncle " \
         "arrives with a handsome stranger in tow."
MovieJ = "Adapted from the bestselling novel by Madeleine St John, Ladies in Black is an alluring and " \
         "tender-hearted comedy drama about the lives of a group of department store employees in 1959 Sydney."

movie_list = [MovieA, MovieB, MovieC, MovieD, MovieE, MovieF, MovieG, MovieH, MovieI, MovieJ]

a = [nlp(MovieA).similarity(Planet_Hulk_desc),
     nlp(MovieB).similarity(Planet_Hulk_desc),
     nlp(MovieC).similarity(Planet_Hulk_desc),
     nlp(MovieD).similarity(Planet_Hulk_desc),
     nlp(MovieE).similarity(Planet_Hulk_desc),
     nlp(MovieF).similarity(Planet_Hulk_desc),
     nlp(MovieG).similarity(Planet_Hulk_desc),
     nlp(MovieH).similarity(Planet_Hulk_desc),
     nlp(MovieI).similarity(Planet_Hulk_desc),
     nlp(MovieJ).similarity(Planet_Hulk_desc)]

while True:
    movie = input("Have you watched Planet Hulk? Yes or No?").lower()
    if movie == "yes":
        print(f"you should watch this movie, here's the description of it: \n {movie_list[a.index(max(a))]}")
        quit()
    elif movie == "no":
        print("You may want to watch Planet Hulk.")
        quit()
    else:
        print("enter an appropriate answer")
        continue
