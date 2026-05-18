import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import io
import base64

plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

def heat_map_portfolio(two_days_candle_data):
    
    returns_df = pd.DataFrame(two_days_candle_data)
    
    returns_df = returns_df.dropna()
    
    corr = returns_df.corr()
    corr = corr.iloc[::-1]
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(
        corr,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        vmin=-1,
        vmax=1,
        center=0,
        linewidths=0.5,
        square=True,
        ax = ax
    )

    plt.title("일별 수익률 상관관계 히트맵")
    plt.tight_layout()
    
    # PNG파일로 변환 후 저장
    buffer = io.BytesIO()
    fig.savefig(buffer, format="png", bbox_inches="tight")
    buffer.seek(0)

    image_base64 = base64.b64encode(buffer.read()).decode("utf-8")
    
    plt.close(fig)
    #plt.show()
    
    return f"""
    <img src="data:image/png;base64,{image_base64}">
    """