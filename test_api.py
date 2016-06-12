import click
from time import sleep
import webbrowser
from exactonline.api import ExactApi
from exactonline.storage import IniStorage
from urllib.parse import unquote

class MyIniStorage(IniStorage):
    def get_response_url(self):
        "Configure your custom response URL."
        return self.get_base_url()

@click.group()
def cli():
    pass

@click.command('setup')
@click.option('--base-url', prompt='Base url', help="Base url")
@click.option('--client-id', prompt='Client Id', help="Client id, found in the app center")
@click.option('--client-secret', prompt='Client secret', help="Client secret, found in the app center")
def setup(base_url, client_id, client_secret):
    """ One time setup of the ini storage. This onlu need to run once"""
    storage = get_storage();
    storage.set('application', 'base_url', base_url)
    storage.set('application', 'client_id', client_id)
    storage.set('application', 'client_secret', client_secret)
    api = ExactApi(storage)
    # Open a web browser to get the code query parameter
    print("A web browser is going to open in 5 seconds, authenticate and copy and paste the value of the code query parameter")
    sleep(5)
    webbrowser.open_new(api.create_auth_request_url())
    code = unquote(input('Enter value of the code query parameter: '))
    api.request_token(code)
    print("High five!! it worked")

@click.command('demo')
def demo():
    """Demo that connect to your API. and list the result of the division endpoint"""
    api = ExactApi(get_storage())
    api.refresh_token()
    divisions, current_divisions = api.get_divisions()
    print('Possible divisions {}'.format(divisions))
    print('Current division {}'.format(current_divisions))


def get_storage():
    return MyIniStorage('config.ini')


cli.add_command(demo)
cli.add_command(setup)

if __name__ == '__main__':
    cli()
