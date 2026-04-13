"""
1 Raspa el siguiente sitio y guarda los datos como un archivo JSON (url = 'http://www.bu.edu/president/boston-university-facts-stats/').
2 Extrae las tablas de esta URL (https://archive.ics.uci.edu/ml/datasets.php) y conviértelas a un archivo JSON.
3 Raspa la tabla de presidentes y guarda los datos como JSON (https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). Esta tabla no está muy bien estructurada,por lo que la extracción puede llevar tiempo.
"""
# Ejercicio 1: teniendo en cuenta que en  http://www.bu.edu/president/boston-university-facts-stats/  tenemos ul > li > span x2   y queremos extraer el texto de span (1er span es la clave y el 2do es el valor)
