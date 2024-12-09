import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.set_title("Weights Diagram")

ax.spines["bottom"].set_position("zero")
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.set_xlim([-2, 2])
ax.set_ylim([-3, 2])

ax.set_xticks([-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2])
ax.set_xticklabels(["", r"$-\frac{3}{2}$", "-1", r"$-\frac{1}{2}$", "0", r"$\frac{1}{2}$", "1", r"$\frac{3}{2}$", ""])

ax.set_xlabel(r"$t_3$", horizontalalignment="right", verticalalignment="bottom", x=1.05)
ax.set_ylabel(r"$Y$", loc="top", rotation=0)

xvals = [1.5, 0.5, -0.5, -1.5, 1, 0.5, 0]
yvals = [1, 1, 1, 1, 0, -1, -2]

ax.plot(xvals, yvals, ".k", markersize=12)

fig.savefig("hw/epp_hw7/weights_diagram1.png", bbox_inches="tight")

###

fig, ax = plt.subplots()

ax.set_title("Weights Diagram")

ax.spines["bottom"].set_position("zero")
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.set_xlim([-2, 2])
ax.set_ylim([-3, 2])

ax.set_xticks([-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2])
ax.set_xticklabels(["", r"$-\frac{3}{2}$", "-1", r"$-\frac{1}{2}$", "0", r"$\frac{1}{2}$", "1", r"$\frac{3}{2}$", ""])

ax.set_xlabel(r"$t_3$", horizontalalignment="right", verticalalignment="bottom", x=1.05)
ax.set_ylabel(r"$Y$", loc="top", rotation=0)

xvals = [1.5, 0.5, -0.5, -1.5, 1, 0.5, 0, -1, -0.5, 0]
yvals = [1, 1, 1, 1, 0, -1, -2, 0, -1, 0]

ax.plot(xvals, yvals, ".k", markersize=12)

###

fig.savefig("hw/epp_hw7/weights_diagram2.png", bbox_inches="tight")

fig, ax = plt.subplots()

ax.set_title("Weights Diagram")

ax.spines["bottom"].set_position("zero")
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.set_xlim([-2, 2])
ax.set_ylim([-3, 2])

ax.set_xticks([-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2])
ax.set_xticklabels(["", r"$-\frac{3}{2}$", "-1", r"$-\frac{1}{2}$", "0", r"$\frac{1}{2}$", "1", r"$\frac{3}{2}$", ""])

ax.set_xlabel(r"$t_3$", horizontalalignment="right", verticalalignment="bottom", x=1.05)
ax.set_ylabel(r"$Y$", loc="top", rotation=0)

xvals = [1.5, 0.5, -0.5, -1.5, 1, 0.5, 0, -1, -0.5, 0]
yvals = [1, 1, 1, 1, 0, -1, -2, 0, -1, 0]


ax.plot([-1.5, 0], [1,-2],"--", color="gray")
ax.plot([-0.5, 0.5], [1,-1],"--", color="gray")
ax.plot([0.5, 1], [1,0],"--", color="gray")

ax.plot(xvals, yvals, ".k", markersize=12)

ax.text(0.1, -2.1, r"$Q=-1$")
ax.text(0.6, -1.1, r"$Q=0$")
ax.text(1.0, 0.2, r"$Q=1$")
ax.text(1.6, 0.9, r"$Q=2$")


fig.savefig("hw/epp_hw7/weights_diagram3.png", bbox_inches="tight")