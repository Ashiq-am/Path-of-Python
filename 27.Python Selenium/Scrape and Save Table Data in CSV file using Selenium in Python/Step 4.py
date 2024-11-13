while (1):

    try:
        method = driver.find_element_by_xpath('//*[@id="post-427949"]\
		/div[3]/table[2]/tbody/tr[' + str(r) + ']/td[1]').text
        Desc = driver.find_element_by_xpath('//*[@id="post-427949"]\
		/div[3]/table[2]/tbody/tr[' + str(r) + ']/td[2]').text
        Table_dict = {
            'Method': method,
            'Description': Desc
        }
        templist.append(Table_dict)
        df = pd.DataFrame(templist)
        r += 1

    except NoSuchElementException:
        break
