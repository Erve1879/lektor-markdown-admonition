# -*- coding: utf-8 -*-
import re
from lektor.pluginsystem import Plugin


_prefix_re = re.compile(r'^\s*(!{1,4})\s+')

CLASSES = {
    1: 'success',
    2: 'notice',
    3: 'warning',
    4: 'danger',
}


class AdmonitionMixin(object):

    def paragraph(self, text):
        match = _prefix_re.match(text)
        if match is None:
            return super(AdmonitionMixin, self).paragraph(text)
        level = len(match.group(1))
        return '<aside class="%s">%s</aside>' % (
            CLASSES[level],
            text[match.end():]
        )


class MarkdownAdmonitionPlugin(Plugin):
    name = u'Markdown Admonition'
    description = u'Adds admonitions to markdown.'

    def on_markdown_config(self, config, **extra):
        config.renderer_mixins.append(AdmonitionMixin)
