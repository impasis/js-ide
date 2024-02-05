import ctypes


def rgbToHex(rgb):
    return "#%02x%02x%02x" % rgb


ctypes.windll.shcore.SetProcessDpiAwareness(True)

"""
monokai theme
======================================================================
"""

monokai_colors = {
    "keywords": rgbToHex((86, 216, 238)),
    "keywords_red": rgbToHex((249, 36, 114)),
    "keywords_orange": rgbToHex((250, 150, 34)),
    "comments": rgbToHex((117, 113, 94)),
    "string": rgbToHex((229, 216, 112)),
    "numbers": rgbToHex((174, 129, 255)),
    "background": rgbToHex((39, 40, 34)),
    "brackets": rgbToHex((232, 186, 54)),
    "txt_color": rgbToHex((218, 247, 241)),
    "sel_color": rgbToHex((87, 89, 89)),
}

js_syntax_monokai = [
    [
        r"\b(var|let|const|with|function|class)\b",
        monokai_colors["keywords"]
    ],
    [
        r"\b(this|super)\b", monokai_colors["keywords_orange"]
    ],
    [
        r"\b(new|as|for|in|while|do|break|return|continue|switch|case|default|if|else|throw|try|catch|finally|yield"
        r"|await|async|of|static|export|import|debugger|extends|with)\b",
        monokai_colors["keywords_red"]
    ],
    [r"\b\d+(\.\d+)?\b", monokai_colors["numbers"]],
    [r"/\*.*?\*/", monokai_colors["comments"]],
    [r"\b(true|false|null|NaN|Infinity|undefined)\b", monokai_colors["numbers"]],
    ['".*?"', monokai_colors["string"]],
    ['\'.*?\'', monokai_colors["string"]],
    ['//.*?$', monokai_colors["comments"]],
    [r"\(|\)", monokai_colors["brackets"]]
]