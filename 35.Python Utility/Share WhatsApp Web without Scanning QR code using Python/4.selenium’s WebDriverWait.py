def _wait_for_presence_of_an_element(browser, selector):
    element = None

    try:
        element = WebDriverWait(browser, DEFAULT_WAIT).until(
            EC.presence_of_element_located(selector)
        )
    except:
        pass
    finally:
        return element
