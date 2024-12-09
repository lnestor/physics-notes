import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig, ax = plt.subplots()

ax.add_patch(Rectangle((0.8, 0.0), 0.2, 0.2, fill=True, edgecolor="black", facecolor="gray"))
ax.add_patch(Rectangle((0.7, 0.2), 0.1, 0.1, fill=True, edgecolor="black", facecolor="gray"))
ax.add_patch(Rectangle((0.5, 0.3), 0.2, 0.2, fill=True, edgecolor="black", facecolor="gray"))
ax.add_patch(Rectangle((0.3, 0.5), 0.2, 0.2, fill=True, edgecolor="black", facecolor="gray"))
ax.add_patch(Rectangle((0.0, 0.7), 0.3, 0.3, fill=True, edgecolor="black", facecolor="gray"))

ax.text(0.9, 0.1, r"$m_5,j_5$", horizontalalignment="center", verticalalignment="center")
ax.text(0.75, 0.25, r"$m_4,j_4$", horizontalalignment="center", verticalalignment="center")
ax.text(0.6, 0.4, r"$m_3,j_3$", horizontalalignment="center", verticalalignment="center")
ax.text(0.4, 0.6, r"$m_2,j_2$", horizontalalignment="center", verticalalignment="center")
ax.text(0.15, 0.85, r"$m_1,j_1$", horizontalalignment="center", verticalalignment="center")

ax.set_aspect(1)
ax.set_title("Representations of the Poincare Group")
ax.tick_params(bottom=False, labelbottom=False, left=False, labelleft=False)

fig.savefig("notes/poincare/irrep_visual.png", bbox_inches="tight")