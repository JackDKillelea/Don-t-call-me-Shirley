from helpers.DataHelper import GetScoreData

# Highlight max and min values
def Highlight_Max_Min(s):
    is_max = s == s.max()
    is_min = s == s.min()
    return ['background-color: #007d23' if v else 'background-color: #7d0000' if m else '' 
            for v, m in zip(is_max, is_min)]

def Highlight_Max_Min_Inverted(s):
    is_max = s == s.max()
    is_min = s == s.min()
    return ['background-color: #7d0000' if v else 'background-color: #007d23' if m else '' 
            for v, m in zip(is_max, is_min)]

def ScoreColours(s):
    styles = []
    scoreData = GetScoreData()
    thresholds = {entry['score']: entry['rgbHex'] for entry in scoreData}

    for value in s:
        try:
            numeric_value = float(value)
        except ValueError:
            numeric_value = 0

        colour = ""
        for threshold, color in thresholds.items():
            if numeric_value > threshold:
                colour = color
                break
        
        styles.append(f'color: {colour}')
    return styles