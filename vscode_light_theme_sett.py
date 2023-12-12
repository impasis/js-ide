import ctypes


def rgbToHex(rgb):
    return "#%02x%02x%02x" % rgb


ctypes.windll.shcore.SetProcessDpiAwareness(True)

"""
vscode light theme
======================================================================
"""

vscode_colors = {
	"keywords": rgbToHex((0, 0, 255)),
	"comments": rgbToHex((0, 128, 0)),
	"string": rgbToHex((163, 21, 21)),
	"numbers": rgbToHex((9, 134, 158)),
    "background": rgbToHex((255, 255, 255)),
    "brackets": rgbToHex((4, 49, 250)),
    "txt_color": rgbToHex((0, 0, 0)),
    "sel_color": rgbToHex((173, 214, 255)),
}

js_syntax_vscode = [
    [r"\b(do|as|for|in|while|do|break|return|continue|switch|case|default|if|else|throw|try|catch|finally|yield|await|async|this|of|static|export|import|debugger|extends|super|var|let|const|with|function|class|true|false|null|NaN|Infinity|undefined)\b", vscode_colors["keywords"]],
    [r"\b\d+(\.\d+)?\b", vscode_colors["numbers"]],
    [r"/\*.*?\*/", vscode_colors["comments"]],
    ['".*?"',  vscode_colors["string"]],
    ['\'.*?\'', vscode_colors["string"]],
    ['//.*?$', vscode_colors["comments"]],
    [r"\(|\)", vscode_colors["brackets"]]
]