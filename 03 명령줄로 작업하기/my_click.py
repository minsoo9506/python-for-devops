import click

# 이렇게 데코레이터를 통해
# 각 함수가 실행될 때 명령줄을 넣을 수 있다.
@click.command()
@click.option('--greeting', default='Hi')
@click.option('--name', default='Someone')
def use_click(greeting, name):
    print(greeting)
    print(name)

if __name__ == '__main__':
    use_click()