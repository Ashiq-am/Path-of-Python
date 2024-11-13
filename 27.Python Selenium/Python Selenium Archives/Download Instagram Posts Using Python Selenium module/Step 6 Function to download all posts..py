def download_allposts():
    # open First Post
    first_post()

    user_name = url.split('/')[-1]

    # check if folder corresponding to user name exist or not
    if (os.path.isdir(user_name) == False):
        # Create folder
        os.mkdir(user_name)

    # Check if Posts contains multiple images or videos
    multiple_images = nested_check()

    if multiple_images:
        nescheck = multiple_images
        count_img = 0

        while nescheck:
            elem_img = chrome.find_element_by_class_name('rQDP3')

            # Function to save nested images
            save_multiple(user_name + '/' + 'content1.' + str(count_img), elem_img)
            count_img += 1
            nescheck.click()
            nescheck = nested_check()

        # pass last_img_flag True
        save_multiple(user_name + '/' + 'content1.' +
                      str(count_img), elem_img, last_img_flag=1)
    else:
        save_content('_97aPb', user_name + '/' + 'content1')
    c = 2

    while (True):
        next_el = next_post()

        if next_el != False:
            next_el.click()
            time.sleep(1.3)

            try:
                multiple_images = nested_check()

                if multiple_images:
                    nescheck = multiple_images
                    count_img = 0

                    while nescheck:
                        elem_img = chrome.find_element_by_class_name('rQDP3')
                        save_multiple(user_name + '/' + 'content' +
                                      str(c) + '.' + str(count_img), elem_img)
                        count_img += 1
                        nescheck.click()
                        nescheck = nested_check()
                    save_multiple(user_name + '/' + 'content' + str(c) +
                                  '.' + str(count_img), elem_img, 1)
                else:
                    save_content('_97aPb', user_name + '/' + 'content' + str(c))

            except selenium.common.exceptions.NoSuchElementException:
                print("finished")
                return

        else:
            break

        c += 1
