# -*- coding: utf-8 -*-

import urllib

from aqt.utils import openLink
from anki.hooks import addHook

JISHO_TEMPLATE = "https://jisho.org/search/{}"


def lookup_online(text):
    text = urllib.parse.quote(text, encoding="utf8")
    openLink(JISHO_TEMPLATE.format(text))


def add_lookup_action(view, menu):
    """Add action to context menu"""
    selected = view.page().selectedText().strip()
    if not selected:
        return

    suffix = (selected[:20] + "..") if len(selected) > 20 else selected

    label = "Search for {} on Jisho".format(suffix)
    a = menu.addAction(label)
    a.triggered.connect(lambda _, t=selected: lookup_online(t))


addHook("AnkiWebView.contextMenuEvent", add_lookup_action)
addHook("EditorWebView.contextMenuEvent", add_lookup_action)
