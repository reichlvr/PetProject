import click
from .process_text import process_text

@click.command()
@click.option('--interactive', '-i', is_flag=True, help='Интерактивный режим')
@click.argument('input_file', type=click.Path(exists=True), required=False)
@click.argument('output_file', type=click.Path(), required=False)
def main(interactive, input_file, output_file):
    """Обрабатывает текст из файла или в интерактивном режиме."""
    if interactive:
        text = click.prompt('Введите текст')
        res = process_text(text)
        click.echo("\n--- Оригинал с ошибками ---")
        click.echo(res['highlighted'])
        click.echo("\n--- Исправленный текст ---")
        click.echo(res['corrected'])
    elif input_file and output_file:
        text = open(input_file, 'r', encoding='utf-8').read()
        res = process_text(text)
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(res['corrected'])
        click.echo(f"✅ Результат сохранён в {output_file}")
    else:
        click.echo("Ошибка: используйте --interactive или укажите файлы")
