"""Global options for the Interactive Tables"""

"""Show the index? Possible values: True, False and 'auto'. In mode 'auto', the index is not shown
if it has no name and its content is range(N)"""
showIndex = "auto"

"""Default styling options. See https://datatables.net/manual/styling/classes"""
classes = ["display"]

"""Tag options example caption.  See: https://datatables.net/blog/2014-11-07"""
tags = {}

"""Default table style"""
style = "max-width:100%"

"""Maximum bytes for displaying a table"""
maxBytes = 2**16

"""Maximum number of rows or columns"""
# maxRows = 10000
# maxColumns = 1000
