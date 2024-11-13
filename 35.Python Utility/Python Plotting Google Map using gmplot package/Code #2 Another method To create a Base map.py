# import gmplot package
import gmplot

# from_geocode method return the
# latitude and longitude of given location .
gmap2 = gmplot.GoogleMapPlotter.from_geocode( "Dehradun, India" )

gmap2.draw( "C:\\Users\\user\\Desktop\\map12.html" )
