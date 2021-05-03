def my_print(txt):
    print(txt)

msg_template='''Hello {name}, Thank you for joining {website}. We are very happy to have you with us.'''

def format_msg(name,website):
    my_print(msg_template.format(name=name,website=website))

format_msg("Robert","yield_url")
format_msg("Ramachari","yashu.url")
