import flet as flt

def myapp(page: flt.Page):
	page.theme_mode = flt.ThemeMode.LIGHT
	page.window_height = 400
	page.window_width = 500

	page.add(
		flt.Text("Hello Geeks",
		size = 40,
		color = flt.colors.GREEN,
		bgcolor = flt.colors.YELLOW_300,
		weight=flt.FontWeight.BOLD,
	))

	page.title = 'GeeksApp using Flet'

	page.update()


flt.app(target=myapp)
