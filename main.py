import click
import requests

@click.group()
def cli():
    pass

@click.command(help='gets weather information of a particular place')
@click.option('--location','-l', help='The name of the location you want to get weather information for')
@click.option('--slackid', envvar='SLACKID')
def getweather(location, slackid):
    if location:
        loc = location
    else:
        loc = click.prompt('Please enter a location')
    if loc:
        if slackid:
            payload = {'command': 'getweather', 'slack_id': str(slackid), 'location': str(loc)}
            r = requests.post('http://f141be9.ngrok.com/incoming', data=payload)
            if r.status_code == 200:
                click.echo('>>>  ' + r.content)
            else:
                click.echo('>>>  Error encountered when trying to get weather information')
        else:
            click.echo('>>>  Error: Slack Id not found. Set your slack Id i.e export SLACKID="slackid" ')


@click.command(help='gets the list of all your notes')
@click.option('--slackid', envvar='SLACKID')
def listnotes(slackid):
    if slackid:
        payload = {'command': 'listnotes', 'slack_id': str(slackid)}
        r = requests.post('http://f141be9.ngrok.com/incoming', data=payload)
        if r.status_code == 200:
            click.echo('>>>  ' + r.content)
        else:
            click.echo('>>>  Error encountered when trying to get list of notes')
    else:
        click.echo('>>>  Error: Slack Id not found. Set your slack Id i.e export SLACKID="slackid"')


@click.command(help='write a note')
@click.option('--slackid', envvar='SLACKID')
def writenote(slackid):
    if slackid:
        note = click.prompt('Write your note here >>>  ')
        payload = {'command': 'writenote', 'slack_id': str(slackid), 'note': str(note)}
        r = requests.post('http://f141be9.ngrok.com/incoming', data=payload)
        if r.status_code == 200:
            click.echo('>>>  ' + r.content)
        else:
            click.echo('>>>  Error encountered when trying to make a note')
    else:
        click.echo('>>>  Error: Slack Id not found. Set your slack Id i.e export SLACKID="slackid" ')


@click.command(help='delete a note')
@click.option('--slackid', envvar='SLACKID')
@click.option('--index','-i', help='The number of note you want to delete from the list')
def deletenote(slackid, index):
    if index:
        idx = index
    else:
        idx = click.prompt('Enter the note number')
    if idx:
        if slackid:
            payload = {'command': 'deletenote', 'slack_id': str(slackid), 'index': str(idx)}
            r = requests.post('http://f141be9.ngrok.com/incoming', data=payload)
            if r.status_code == 200:
                click.echo('>>>  ' + r.content)
            else:
                click.echo('>>>  Error encountered when trying to delete a note')
        else:
            click.echo('>>>  Error: Slack Id not found. Set your slack Id i.e export SLACKID="slackid" ')


@click.command(help='Ask mentors for help')
@click.option('--slackid', envvar='SLACKID')
@click.option('--tech','-t', help='The technology you have problem with')
def needhelp(slackid, tech):
    if tech:
        t = tech
        desc = click.prompt('Please describe the challenge you are trying to solve in not more than 200 words \n')
    else:
        t = click.prompt('Technology please')
        desc = click.prompt('Please describe the challenge you are trying to solve in not more than 200 words \n')
    if desc and t:
        if slackid:
            payload = {'command': 'needhelp', 'slack_id': str(slackid), 'tech': str(t), 'desc': str(desc)}
            r = requests.post('http://f141be9.ngrok.com/incoming', data=payload)
            if r.status_code == 200:
                click.echo('>>>  ' + r.content)
            else:
                click.echo('>>>  Error encountered when trying to reach out to mentors')
        else:
            click.echo('>>>  Error: Slack Id not found. Set your slack Id i.e export SLACKID="slackid" ')


@click.command(help='Register as mentor on genio platform')
@click.option('--slackid', envvar='SLACKID')
@click.option('--tech','-t', help='The technology you want to mentor on')
def mentor(slackid, tech):
    if tech:
        t = tech
    else:
        t = click.prompt('Which technology will you like to mentor on ')
    if t:
        if slackid:
            payload = {'command': 'mentor', 'slack_id': str(slackid), 'tech': str(t)}
            r = requests.post('http://f141be9.ngrok.com/incoming', data=payload)
            if r.status_code == 200:
                click.echo('>>>  ' + r.content)
            else:
                click.echo('>>>  Error encountered when trying to register as a mentor')
        else:
            click.echo('>>>  Error: Slack Id not found. Set your slack Id i.e export SLACKID="slackid" ')


@click.command(help='Calculate mathematical expressions and conversions')
@click.option('--slackid', envvar='SLACKID')
@click.option('--expression','-e', help='The technology you have problem with')
def calculate(slackid, expression):
    if expression:
        e = expression
    else:
        e = click.prompt('>>>>>>> ')
    if e:
        if slackid:
            payload = {'command': 'calculate', 'slack_id': str(slackid), 'expression': str(e)}
            r = requests.post('http://f141be9.ngrok.com/incoming', data=payload)
            if r.status_code == 200:
                click.echo('>>>  ' + r.content)
            else:
                click.echo('>>>  Error encountered when trying to fetch answer')
        else:
            click.echo('>>>  Error: Slack Id not found. Set your slack Id i.e export SLACKID="slackid" ')


@click.command(help='lists mentors for different technology')
@click.option('--slackid', envvar='SLACKID')
def listmentors(slackid):
    if slackid:
        payload = {'command': 'listmentors', 'slack_id': str(slackid)}
        r = requests.post('http://f141be9.ngrok.com/incoming', data=payload)
        if r.status_code == 200:
            click.echo('>>>  \n' + r.content)
        else:
            click.echo('>>>  Error encountered when trying to get a list of mentors')
    else:
        click.echo('>>>  Error: Slack Id not found. Set your slack Id i.e export SLACKID="slackid" ')


cli.add_command(getweather)
cli.add_command(listnotes)
cli.add_command(writenote)
cli.add_command(deletenote)
cli.add_command(needhelp)
cli.add_command(mentor)
cli.add_command(calculate)
cli.add_command(listmentors)
