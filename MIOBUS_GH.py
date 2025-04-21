import rhinoscriptsyntax as rs
import ghpythonlib.components as ghcomp
from math import pi

# origem
pc = ghcomp.ConstructPoint(0, 0, 0)
circulo = ghcomp.Circle(pc, raio)

# Formas
divisoes = ghcomp.PerpFrames(circulo, div, True).frames
modulos = ghcomp.Polygon(divisoes, raio_modulo, forma, 0).polygon

# Ângulo de rotação
angulo = [i * 360 / div for i in range(div)]
rad = [a * pi / 180 for a in angulo]

# Rotação individual
rotacionados = []
for m, r, plano in zip(modulos, rad, divisoes):
    rotacionados.append(ghcomp.Rotate(m, r, plano).geometry)

# Saídas
a = rotacionados        # módulos rotacionados
modulos = modulos       # módulos sem rotação (se quiser comparar)
circulo = circulo       # o círculo base
