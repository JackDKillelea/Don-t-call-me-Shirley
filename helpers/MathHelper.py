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