import ctypes


def rgbToHex(rgb):
    return "#%02x%02x%02x" % rgb


ctypes.windll.shcore.SetProcessDpiAwareness(True)

"""
github dark theme
======================================================================
"""

github_dark_colors = {
    "keywords": rgbToHex((255, 123, 114)),
    "comments": rgbToHex((111, 146, 158)),
    "string": rgbToHex((165, 214, 255)),
    "numbers": rgbToHex((123, 190, 250)),
    "background": rgbToHex((13, 17, 23)),
    "brackets": rgbToHex((248, 170, 111)),
    "txt_color": rgbToHex((230, 237, 243)),
    "sel_color": rgbToHex((34, 55, 75)),
}

js_syntax_github_dark = [
    [
        r"\b(new|as|for|in|while|do|break|return|continue|switch|case|default|if|else|throw|try|catch|finally|yield"
        r"|await "
        r"|async|this|of|static|export|import|debugger|extends|super|var|let|const|with|function|class"
        r"|null|NaN|Infinity|undefined|of)\b",
        github_dark_colors["keywords"]],
    [r"\b\d+(\.\d+)?\b", github_dark_colors["numbers"]],
    [r"/\*.*?\*/", github_dark_colors["comments"]],
    [r"\b(true|false)\b", github_dark_colors["numbers"]],
    ['".*?"', github_dark_colors["string"]],
    ['\'.*?\'', github_dark_colors["string"]],
    ['//.*?$', github_dark_colors["comments"]],
    [r"\(|\)", github_dark_colors["brackets"]]
]
