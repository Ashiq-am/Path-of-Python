import xml.dom.minidom as md


def main():
    file = md.parse("test.xml")

    height = file.createElement("height")

    # setting height value to 180cm
    height.setAttribute("val", "180 cm")

    # adding height tag to the "file"
    # object
    file.firstChild.appendChild(height)

    lan = ["English", "Spanish", "French"]

    # creating separate "lang" tags for
    # each language and adding it to
    # "file" object
    for l in lan:
        lang = file.createElement("lang")
        lang.setAttribute("lng", l)
        file.firstChild.appendChild(lang)

    delete = file.getElementsByTagName("hobby")

    # deleting all occurences of a particular
    # tag(here "hobby")
    for i in delete:
        x = i.parentNode
        x.removeChild(i)

    # modifying the value of a tag(here "age")
    file.getElementsByTagName("age")[0].childNodes[0].nodeValue = "29"

    # writing the changes in "file" object to
    # the "test.xml" file
    with open("test.xml", "w") as fs:

        fs.write(file.toxml())
        fs.close()


if __name__ == "__main__":
    main()
