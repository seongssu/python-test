import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

def heat_map_portfolio(profit_days):
    
    returns_df = pd.DataFrame(profit_days)
    
    returns_df = returns_df.dropna()
    
    corr = returns_df.corr()
    corr = corr.iloc[::-1]
    plt.figure(figsize=(8, 6))
    sns.heatmap(
        corr,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        vmin=-1,
        vmax=1,
        center=0,
        linewidths=0.5,
        square=True
    )

    plt.title("일별 수익률 상관관계 히트맵")
    plt.tight_layout()
    plt.show()