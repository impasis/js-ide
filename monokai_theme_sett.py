import ctypes


def rgbToHex(rgb):
    return "#%02x%02x%02x" % rgb


ctypes.windll.shcore.SetProcessDpiAwareness(True)

"""
github dark theme
======================================================================
"""

monokai_colors = {
    "keywords": rgbToHex((86, 216, 238)),
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
        r"\b(new|as|for|in|while|do|break|return|continue|switch|case|default|if|else|throw|try|catch|finally|yield"
        r"|await "
        r"|async|this|of|static|export|import|debugger|extends|super|var|let|const|with|function|class"
        r"|null|NaN|Infinity|undefined|of)\b",
        monokai_colors["keywords"]],
    [r"\b\d+(\.\d+)?\b", monokai_colors["numbers"]],
    [r"/\*.*?\*/", monokai_colors["comments"]],
    [r"\b(true|false)\b", monokai_colors["numbers"]],
    ['".*?"', monokai_colors["string"]],
    ['\'.*?\'', monokai_colors["string"]],
    ['//.*?$', monokai_colors["comments"]],
    [r"\(|\)", monokai_colors["brackets"]]
]