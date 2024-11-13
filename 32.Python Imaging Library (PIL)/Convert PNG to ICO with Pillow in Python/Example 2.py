from PIL import Image

logo = Image.open("C:\\Users\\sai mohan pula\
molu\\Desktop\\geeks_dir\\gfgLogo.png")

logo.save("C:\\Users\\sai mohan pulamolu\\Des\
ktop\\geeks_dir\\gfgLogoIco_40.ico", format='ICO',
		sizes=[(40, 40)])
