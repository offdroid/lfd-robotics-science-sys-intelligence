import matplotlib.pyplot as plt
from pathlib import Path
import pandas as pd
import seaborn as sns

df = None
for path in Path("path/to/results").glob("*/*"):
    if path.name == ("eval.csv"):
        print("Importing", path)
        _df = pd.read_csv(path)
        _df["eps"] = "16 demonstration eps."
        if df is None:
            df = _df
        else:
            df = pd.concat([df, _df], axis=0)

ax0 = plt.subplot(1, 1, 1)
ax = sns.lineplot(df, x="step", y="average_test_return", hue="eps", palette="tab10", ax=ax0)

ax2 = plt.axes([0.26, 0.2, .24, .6], facecolor='white')
_g = sns.lineplot(df, x="step", y="average_test_return", hue="eps", palette="tab10", ax=ax2)
ax2.set_xlim([0.0, 60_000.0])
ax2.legend([],[], frameon=False)

ax.set(xlabel='Timesteps', ylabel='Average return')
ax2.set(xlabel='', ylabel='')
ax.grid()
ax2.grid()
ax0.ticklabel_format(style='sci', scilimits=(0, 0), axis='x')
ax2.ticklabel_format(style='sci', scilimits=(0, 1), axis='x')
ax2.xaxis.major.formatter._useMathText = True
plt.show()
