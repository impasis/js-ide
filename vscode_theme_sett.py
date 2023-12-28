import ctypes


def rgbToHex(rgb):
    return "#%02x%02x%02x" % rgb


ctypes.windll.shcore.SetProcessDpiAwareness(True)

"""
vscode theme
======================================================================
"""

vscode_colors = {
    "keywords": rgbToHex((62, 156, 214)),
    "comments": rgbToHex((106, 153, 85)),
    "string": rgbToHex((206, 145, 120)),
    "numbers": rgbToHex((167, 206, 168)),
    "background": rgbToHex((30, 30, 30)),
    "brackets": rgbToHex((255, 215, 14)),
    "txt_color": rgbToHex((234, 234, 234)),
    "sel_color": rgbToHex((38, 79, 120)),
}

js_syntax_vscode = [
    [
        r"\b(new|as|for|in|while|do|break|return|continue|switch|case|default|if|else|throw|try|catch|finally|yield"
        r"|await "
        r"|async|this|of|static|export|import|debugger|extends|super|var|let|const|with|function|class|true|false"
        r"|null|NaN|Infinity|undefined|of)\b",
        vscode_colors["keywords"]],
    [r"\b\d+(\.\d+)?\b", vscode_colors["numbers"]],
    [r"/\*.*?\*/", vscode_colors["comments"]],
    ['".*?"', vscode_colors["string"]],
    ['\'.*?\'', vscode_colors["string"]],
    ['//.*?$', vscode_colors["comments"]],
    [r"\(|\)", vscode_colors["brackets"]]
]
