import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("job_data.csv")

skills = df["Skills"].str.split(", ")
skills_count = skills.explode().value_counts()

skills_count.plot(kind="bar", title="Top Skills Demand")
plt.xlabel("Skills")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("skills_demand.png")
plt.show()
