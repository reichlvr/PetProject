import click
from .spell import correct_spelling
from .grammar import correct_grammar
from .utils import remove_repeats, highlight

@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.argument('output_file', type=click.Path())
def main(input_file, output_file):
    """CLI для обработки текстового файла"""
    text = open(input_file, 'r', encoding='utf-8').read()
    # Обработка
    from . import process_text  # чтобы все сразу
    res = process_text(text)
    # Запись результатов
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(res['corrected'])
    click.echo(f"Исправлено {res['errors_count']} ошибок. Результат в {output_file}")

if __name__ == '__main__':
    main()
