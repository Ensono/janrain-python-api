from termcolor import colored


def output(should_print, output_text):
    output_color = 'grey'
    if should_print:
        print(colored(output_text, output_color))
