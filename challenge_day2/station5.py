#sample input, sample output, input, output
#Greta, 5, David C
#Marie, 2, Alissa
#Isar, 3, Juan
#Karolina, 1, Younes
#Yifan, 6, Juan
#Greta, 5, Yinan
#Yvan, 2, Leopaldo
#Pija, 4, Julia
#Anna D, 4, Ivan
#Anna, 1, Uli
#Elianna, 4, Jelle
#Nicolas, 3, David G
#YangYang, 4, Anita
#Nicolas, 3, Nadee
#Maliah, 1, Ivan
#Maria Paz, 2, Nikola
#Maliah, 1, Juan
#Oleysa, 6, Nadee
#Greta, 5, Alissa 

def solution_station_5(n):
    learning_teams = {
        "1": ["Daeho, David, Kaisa, Oliver, Sara, Dan, Ivar, Lotte, Riya, Vassil, Twan, Ester, Karolina, Lena, Margarita, Anna, Kien, Klaudia, Maliah, Todd"],
        "2": ["Oumaima, Mathilde, Marie, Anita, Ziyan, Bernardo, Eleanor, Lorijn, Maria, Younes, Yvan, Henning, Liangyu, Maciej, Toprak, Chris, GengXin, Mingze, Phoebe"],
        "3": ["Betija, Haider, Kacper, Sophie, Amir, Baltasar, Isar, Jelle, Nicolas, David, Ipek, Juan, Marfa, Maria, Alissa, Leopoldo, Mies, Jiaying, Kaixin, Mai, Sem, Tibbe"],
        "4": ["Justus, Julia, Philip, Uli, Vanessa, Anna, Ekaterina, Thessa, Tongfei, Yang, Benedikt, Jan, Nadee, Osjah, Tim, Eliana, Joana, Peilin, Pija, Wenhao"],
        "5": ["Afua, Cristina, Greta, Jace, Laura, Anna, Bassant, Ivan, Juriaan, Kiavash"],
        "6": ["Keitaro, Nohemi, Norina, Yifan, Yinan, Luo, Nikola, Olesya, Sophie, Tom"]

    }

    name_to_teams = {}
    for team, names_list in learning_teams.items():
        for names_str in names_list:
            for name in [n.strip() for n in names_str.split(",")]:
                name_to_teams[name] = int(team)
            
    return name_to_teams.get(n, -1)

