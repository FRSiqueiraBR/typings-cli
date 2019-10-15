import click
import random
import pyfiglet

@click.command()
def start():
    generate_ascii()
    typing_test()


def typing_test():
    word_count = click.prompt('Words')
    text = generate_text(word_count)

    if click.confirm('Are yo READY?', abort=True):
        typing = click.prompt('Typing Test')

        compare_text_with_typing_test(text, typing)

        redo = click.confirm('REDO?')
        while redo: 
            typing_test()
            redo = click.confirm('REDO?')


def generate_ascii():
    click.secho(pyfiglet.figlet_format("Typings CLI"), fg='green')


def generate_text(word_count):
    words = ["the", "be", "of", "and", "a", "to", "in", "he", "have", "it",
             "that", "for", "they", "I", "with", "as", "not", "on", "she",
             "at", "by", "this", "we", "you", "do", "but", "from", "or",
             "which", "one", "would", "all", "will", "there", "say", "who",
             "make", "when", "can", "more", "if", "no", "man", "out", "other",
             "so", "what", "time", "up", "go", "about", "than", "into",
             "could", "state", "only", "new", "year", "some", "take", "come",
             "these", "know", "see", "use", "get", "like", "then", "first",
             "any", "work", "now", "may", "such", "give", "over", "think",
             "most", "even", "find", "day", "also", "after", "way", "many",
             "must", "look", "before", "great", "back", "through", "long",
             "where", "much", "should", "well", "people", "down", "own",
             "just", "because", "good", "each", "those", "feel", "seem",
             "how", "high", "too", "place", "little", "world", "very",
             "still", "nation", "hand", "old", "life", "tell", "write",
             "become", "here", "show", "house", "both", "between", "need",
             "mean", "call", "develop", "under", "last", "right", "move",
             "thing", "general", "school", "never", "same", "another",
             "begin", "while", "number", "part", "turn", "real", "leave",
             "might", "want", "point", "form", "off", "child", "few", "small",
             "since", "against", "ask", "late", "home", "interest", "large",
             "person", "end", "open", "public", "follow", "during", "present",
             "without", "again", "hold", "govern", "around", "possible",
             "head", "consider", "word", "program", "problem", "however",
             "lead", "system", "set", "order", "eye", "plan", "run", "keep",
             "face", "fact", "group", "play", "stand", "increase", "early",
             "course", "change", "help", "line"]
    separator = " "
    text = []

    for count in range(int(word_count)):
        text.append(random.choice(words))

    text = separator.join(text)

    click.echo(text)
    
    #click.echo(click.get_terminal_size())
    return text


def overlapping_percentage(text, typing_test):
    print(len(set(text) & set(typing_test)))
    return (100.0 * len(set(text) & set(typing_test))) / len(set(text) | set(typing_test))


def compare_text_with_typing_test(text, typing): 
    click.secho(text, fg='red')
    click.secho(typing, fg='green')


if __name__ == '__main__':
    start()
