def insertSubstring(text, tag, substring):
    i_tag = text.index(tag)

    return text[:i_tag] + substring + text[i_tag + len(tag):]
