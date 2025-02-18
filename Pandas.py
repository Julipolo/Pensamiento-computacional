# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 10:02:02 2025

@author: Julip
"""
import pandas as pd
peliculas = {'nombre': ['Titanic', 'Kil Bill', 'Matrix', 'El padrino', 'Avatar',
                        'Casablanca', 'El exorcista',  'Soy leyenda',
                        'El club de la pelea', 'Mujercitas'],
            'director': ['James Cameron', 'Quentin Tarantino', 'Hermanas Wachowski',
                        'Francis Ford Coppola', 'James Cameron', 'Michael Curtiz',
                        'William Friedkin', 'Francis Lawrence','David Fincher',
                        'Greta Gerwig'],
            'año': [1997, 2003, 1999, 1972, 2009, 1942, 1973, 2007, 1999, 2019],
            'género': ['romance', 'acción', 'ciencia ficción', 'drama', 'ciencia ficción', 'drama', 'terror',
                        'ciencia ficción', 'drama', 'drama'],
            'puntaje': [8.6, None, 6.9, 7.5, 9.1, 6.0, None, None, 9.4, 8.0]}

df = pd.DataFrame(peliculas)
df
#  Mostrar la información del DataFrame con el método info(), ¿Cómo se llaman y qué tipo de dato tiene
# cada columna? ¿Cuántos elementos nulos hay en cada columna? Interpretar qué información se guarda
# en esta tabla y para qué puede serv
def uno():
    df.info()
# 2. Mostrar sólo los nombres de las primeras 3 películas del DataFrame.
def dos():
    print(df["nombre"].head(3))
