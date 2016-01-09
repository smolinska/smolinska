import re
import os.path as op

from django.template import TemplateDoesNotExist
from django.template.loader import get_template

groups = ('(?P<login>.*)', '(?P<host>.*)', '.*')
o_template = '<span class="js-hidden-eml" data-user="{}" data-website="{}">{}</span>'
e_template = '<a href="mailto:{}@{}">{}</a>'
e_regex = e_template.format(*groups)
o_regex = o_template.format(*groups)


def obfuscate_emails(content):
    def repl(a):
        return o_template.format(a.group('login')[::-1], a.group('host')[::-1], '')

    return re.sub(e_regex, repl, content)


def deobfuscate_emails(content):
    def repl(a):
        return e_template.format(a.group('login')[::-1], a.group('host')[::-1],
                                 a.group('login')[::-1] + '@' + a.group('host')[::-1])

    return re.sub(o_regex, repl, content)


def parse_SCSS_variables():
    scss_vars = dict()
    app_dir = op.dirname(__file__)
    with open(op.join(app_dir, 'static', 'css', 'variables.scss')) as vars_file:
        for line in vars_file.readlines():
            # TODO: handle units, floats, colors.
            match = re.search('^\s*\$(?P<name>\S+)\s*:\s*(?P<val>\d+)\D*;\s*$', line)
            if match is not None:
                scss_vars[match.group("name")] = int(match.group("val"))
    return scss_vars


def find_custom_template(tab):
    try:
        tab.template = get_template('tabs/{}.html'.format(tab.slug))
    except TemplateDoesNotExist:
        tab.template = get_template('tabs/baseTab.html')
    return tab
