import ctypes


def rgbToHex(rgb):
    return "#%02x%02x%02x" % rgb


ctypes.windll.shcore.SetProcessDpiAwareness(True)

"""
monokai theme
======================================================================
"""

html_monokai_colors = {
    "tags": rgbToHex((249, 36, 114)),
    "attributes": rgbToHex((166, 206, 40)),
    "values": rgbToHex((229, 216, 112)),
}

html_syntax_monokai = [
    [r'<(/?[\w\d-]+ )>', html_monokai_colors["tags"]],
    [r'([\w\d-]+)(?=\s*=\s*["\'])', html_monokai_colors["attributes"]],
    [r'["\'](.*?)["\']', html_monokai_colors["values"]]
]

# TEST
