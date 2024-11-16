data = []
for i in range(0,len(authors)):


    rows = [authors[i].get_text(),titles[i].get_text(),
            genres[i].get_text(),prices[i].get_text(),
            pubdate[i].get_text(),des[i].get_text()]

    data.append(rows)
