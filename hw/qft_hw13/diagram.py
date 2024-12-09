import matplotlib.pyplot as plt
from feynman import Diagram

diagram = Diagram()

# Create four vertices.
v1 = diagram.vertex(xy=(0.3,0.5))
v2 = diagram.vertex(v1.xy, dx=-0.2, dy=0.2, marker='')
v3 = diagram.vertex(v1.xy, dx=-0.2, dy=-0.2, marker='')

v2.text(r"$e^-$")
v3.text(r"$e^+$")

v1.text(r"$\mu$", x=0.03, y=0.05)
v1.text("a", x=-0.03, y=0.06)
v1.text("b", x=-0.03, y=-0.06)

v4 = diagram.vertex(xy=(0.6,0.5))
v5 = diagram.vertex(v4.xy, dx=0.2, dy=0.2, marker='')
v6 = diagram.vertex(v4.xy, dx=0.2, dy=-0.2, marker='')
v4.text(r"$\nu$", x=-0.02, y=0.05)
v4.text("c", x=0.03, y=0.06)
v4.text("d", x=0.03, y=-0.06)

v6.text(r"$\overline{\nu}_\mu$", x=0.01, y=0.03)
v5.text(r"$\nu_\mu$")

w = diagram.line(v1, v4, style="wiggly")

# Create four lines.
# By default, 'simple' lines have arrows
# and others flavours such as 'wiggly' or 'loopy' don't.
l21 = diagram.line(v2, v1)
l31 = diagram.line(v1, v3)

l45 = diagram.line(v4, v5)
l46 = diagram.line(v6, v4)

# Add labels.
l21.text(r"$p_1$")
l31.text(r"$p_2$")
l45.text(r"$k_1$")
l46.text(r"$k_2$")


diagram.plot()

plt.savefig("hw/qft_hw13/13_6_feynman_diagram.png",bbox_inches="tight")