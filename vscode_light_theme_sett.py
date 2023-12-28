import ctypes


def rgbToHex(rgb):
    return "#%02x%02x%02x" % rgb


ctypes.windll.shcore.SetProcessDpiAwareness(True)

"""
vscode light theme
======================================================================
"""

vscode_light_colors = {
    "keywords": rgbToHex((0, 0, 255)),
    "comments": rgbToHex((0, 128, 0)),
    "string": rgbToHex((163, 21, 21)),
    "numbers": rgbToHex((9, 134, 158)),
    "background": rgbToHex((255, 255, 255)),
    "brackets": rgbToHex((4, 49, 250)),
    "txt_color": rgbToHex((0, 0, 0)),
    "sel_color": rgbToHex((173, 214, 255)),
}

js_syntax_vscode_light = [
    [
        r"\b(new|as|for|in|while|do|break|return|continue|switch|case|default|if|else|throw|try|catch|finally|yield"
        r"|await|async|this|of|static|export|import|debugger|extends|super|var|let|const|with|function|class|true"
        r"|false|null|NaN|Infinity|undefined|of)\b",
        vscode_light_colors["keywords"]],
    [r"\b\d+(\.\d+)?\b", vscode_light_colors["numbers"]],
    [r"/\*.*?\*/", vscode_light_colors["comments"]],
    ['".*?"', vscode_light_colors["string"]],
    ['\'.*?\'', vscode_light_colors["string"]],
    ['//.*?$', vscode_light_colors["comments"]],
    [r"\(|\)", vscode_light_colors["brackets"]]
]