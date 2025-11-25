import pandas_ta as ta

def compute_indicators(df):
    df['rsi'] = ta.rsi(df['Close'])
    macd = ta.macd(df['Close'])
    df['macd'] = macd['MACD_12_26_9']
    df['ema'] = ta.ema(df['Close'])
    bb = ta.bbands(df['Close'])
    df['bb_upper'] = bb['BBU_20_2.0']
    df['bb_lower'] = bb['BBL_20_2.0']
    return df

def score_signal(df):
    latest = df.iloc[-1]
    score = 0
    if latest['rsi'] < 30:
        score += 2
    elif latest['rsi'] > 70:
        score -= 2
    if latest['macd'] > 0:
        score += 2
    else:
        score -= 2
    if latest['Close'] > latest['ema']:
        score += 1
    else:
        score -= 1
    buy_prob = int(50 + score * 10)
    buy_prob = max(0, min(100, buy_prob))
    sell_prob = 100 - buy_prob
    hold_prob = 100 - abs(buy_prob - 50)
    return {"buy_prob": buy_prob, "hold_prob": hold_prob, "sell_prob": sell_prob}