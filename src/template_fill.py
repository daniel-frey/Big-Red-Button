import re


def print_intro():
    """"""
    print('')


def get_template_text(template_filename):
    """"""
    with open(template_filename, 'r') as infile:
        return(infile.read())


def parse_template_text(template):
    """Parse the template text. Return a list of user prompts and the template text with the prompts stripped out."""
    pattern = '<.*?>'
    prompts = re.findall(pattern, template)
    template = re.sub(pattern, '<>', template)
    return template, prompts


def get_user_responses(questions):
    """"""
    responses = []
    for prompt in questions:
        responses.append(input(f'Enter a {prompt.lower()}: '))
    return responses


def format_template_text(template_text, responses):
    """"""
    return template_text.format(*responses)


def print_formatted_text(template_text):
    """Print out the final text."""
    print(template_text)


def write_to_file(filename, template_text):
    """Open a file for writing and write the template_text into it."""
    with open(filename, 'w') as out_file:
        out_file.write(template_text)


def run():
    """Enter script execution."""
    print_intro()
    filename = 'ec2instance_template.json'
    template_text = get_template_text(filename)
    template_text, prompts = parse_template_text(template_text)
    responses = get_user_responses(prompts)
    template_text = format_template_text(template_text, responses)
    print_formatted_text(template_text)
    out_filename = 'completed_instance.json'
    write_to_file(out_filename, template_text)


if __name__ == '__main__':
    run()
