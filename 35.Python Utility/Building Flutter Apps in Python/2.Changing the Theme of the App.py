import flet as flt

def myapp(page: flt.Page):
	page.theme_mode = flt.ThemeMode.DARK # change DARK to LIGHT to convert it to light mode
	page.window_height = 400
	page.window_width = 500

	page.title = 'GeeksApp using Flet'

	page.update()


flt.app(target=myapp)
