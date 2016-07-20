import re


def get_child(parent, selector, index=0):
    """Get a child element from parent matching the specified CSS selector at the specified zero-based index"""

    children = parent.cssselect(selector)
    if children is not None and ((index >= 0 and len(children) > index) or (index < 0 and len(children) >= abs(index))):
        return children[index]


def get_child_attribute(parent, selector, attribute, index=0):
    """Get an attribute value from the specified child element"""

    child = get_child(parent, selector, index)
    if child is not None:
        return child.get(attribute)


def parse_child_attribute(parent, selector, attribute, parser, index=0, default=None):
    """Parse an attribute value from the specified child element"""

    try:
        return parser(get_child_attribute(parent, selector, attribute, index))
    except (TypeError, ValueError):
        return default


def get_child_text(parent, selector, index=0):
    """Get the text content of the specified child element"""

    child = get_child(parent, selector, index)
    if child is not None:
        return child.text_content().strip()


def parse_child_text(parent, selector, parser, index=0):
    """Parse the text content of the specified child element"""

    try:
        return parser(get_child_text(parent, selector, index))
    except (TypeError, ValueError):
        return default


def get_child_text_match(parent, selector, pattern, index=0):
    """Get a regex match on the specified child element's text content"""

    text = get_child_text(parent, selector, index)
    if text is not None:
        return re.search(pattern, text)


def get_child_text_match_groups(parent, selector, pattern, index=0):
    """Get the regex match groups for the specified child element's text content"""

    match = get_child_text_match(parent, selector, pattern, index)
    if match is not None:
        return match.groups()


def get_child_text_match_group(parent, selector, pattern, index=0, group=0):
    """Get a regex match group for the specified child element's text content"""

    groups = get_child_text_match_groups(parent, selector, pattern, index)
    if groups is not None and ((group >= 0 and len(groups) > group) or (group < 0 and len(groups) >= abs(group))):
        return groups[group]


def parse_child_text_match_group(parent, selector, pattern, parser, index=0, group=0, default=None):
    """Parse a regex match group for the specified child element's text content"""

    try:
        return parser(get_child_text_match_group(parent, selector, pattern, index, group))
    except (TypeError, ValueError):
        return default
