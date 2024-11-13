import cherrypy


class Root(object):

    @cherrypy.expose
    def index(self):
        return """<html> 
<head> 

</head> 
<body> 

<div class="container"> 
	<h2><u><i>Multiplication</i></u></h2> 
	<form action="store" id="form" method="GET"> 
	<input type="number" name="num1" /><br /> 
	<input type="number" name="num2" /><br /> 


	<input style="margin-left: 250px;" id=" submit" type="submit"/></div> 
</div> 
	</form> 
</div> 

</body> 
</html>"""

    @cherrypy.expose
    def store(self, num1, num2):
        mul1 = int(num1)
        mul2 = int(num2)

        result = mul1 * mul2

        out = """<html> 
		<body> 



<p> Sum: %s</p> 




		<a style="color:red; font-size:35px;" id="shutdown"; href="./shutdown"><i>Shutdown Server</i></a> 
		</body> 
		</html> 

		"""

        return out % (result)

    @cherrypy.expose
    def shutdown(self):
        cherrypy.engine.exit()


if __name__ == "__main__":
    cherrypy.config.update({'server.socket_port': 8087})

    cherrypy.quickstart(Root())
