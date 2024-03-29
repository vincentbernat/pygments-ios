# -*- coding: utf-8 -*-
# Copyright (c) 2017 Vincent Bernat <bernat@luffy.cx>
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

from pygments.lexer import RegexLexer, bygroups
from pygments.token import Text, Comment, Keyword
from pygments.token import String, Number, Name


class IOSLexer(RegexLexer):
    name = "IOS"
    aliases = ["ios", "cisco", "quagga"]
    tokens = {
        'root': [
            (r'^[ \t]*!.*?\n', Comment.Singleline),
            (r'"(\\\\|\\"|[^"])*"', String.Double),
            (r'[a-f0-9]*:[a-f0-9]*:[a-f0-9:]*(:\d+\.\d+\.\d+\.\d+)?(/\d+)?',
             Number),  # IPv6
            (r'\d+\.\d+\.\d+\.\d+(/\d+)?', Number),  # IPv4
            (r'^([ \t]*)(no[ \t]+)?([a-z][-\w]*)',
             bygroups(Text, Keyword, Name.Function)),
            (r'[ \t]+', Text),
            (r'\n', Text),
            (r'\d+', Number),
            (r'\S+', Text),
        ],
    }
