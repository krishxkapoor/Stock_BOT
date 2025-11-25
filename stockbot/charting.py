import matplotlib.pyplot as plt
import io
import base64

def plot_candlestick(df, symbol):
    fig, ax = plt.subplots(figsize=(8,4))
    ax.plot(df['Date'], df['Close'], label="Close Price")
    ax.plot(df['Date'], df['ema'], label="EMA", linestyle="--")
    ax.fill_between(df['Date'], df['bb_lower'], df['bb_upper'], color='gray', alpha=0.3, label="Bollinger Bands")
    ax.set_title(f"{symbol} Candlestick Chart")
    ax.legend()
    buf = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_b64 = base64.b64encode(buf.read()).decode('utf-8')
    plt.close(fig)
    return image_b64
