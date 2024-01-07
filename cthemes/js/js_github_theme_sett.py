import ctypes


def rgbToHex(rgb):
    return "#%02x%02x%02x" % rgb


ctypes.windll.shcore.SetProcessDpiAwareness(True)

"""
github theme
======================================================================
"""

github_colors = {
    "keywords": rgbToHex((215, 58, 73)),
    "comments": rgbToHex((106, 115, 125)),
    "string": rgbToHex((3, 47, 98)),
    "numbers": rgbToHex((2, 91, 196)),
    "background": rgbToHex((255, 255, 255)),
    "brackets": rgbToHex((215, 58, 73)),
    "txt_color": rgbToHex((36, 41, 46)),
    "sel_color": rgbToHex((204, 229, 255)),
}

js_syntax_github = [
    [
        r"\b(new|as|for|in|while|do|break|return|continue|switch|case|default|if|else|throw|try|catch|finally|yield"
        r"|await "
        r"|async|this|of|static|export|import|debugger|extends|super|var|let|const|with|function|class"
        r"|null|NaN|Infinity|undefined|of)\b",
        github_colors["keywords"]],
    [r"\b\d+(\.\d+)?\b", github_colors["numbers"]],
    [r"/\*.*?\*/", github_colors["comments"]],
    [r"\b(true|false)\b", github_colors["numbers"]],
    ['".*?"', github_colors["string"]],
    ['\'.*?\'', github_colors["string"]],
    ['//.*?$', github_colors["comments"]],
    [r"\(|\)", github_colors["brackets"]]
]