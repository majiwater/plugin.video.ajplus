from xbmcswift2 import Plugin, xbmcgui
from resources.lib import buzzfeedscraper

PLUGIN_URL = 'plugin://plugin.video.youtube/?action=play_video&videoid'

plugin = Plugin()


@plugin.route('/')
def main_menu():

    items = [
        {
            # AJ+ EN
            'label': plugin.get_string(30000),
            'path': plugin.url_for('get_content', url='https://www.youtube.com/channel/UCV3Nm3T-XAgVhKH9jT0ViRg/videos'),
            'thumbnail': 'https://yt3.ggpht.com/-ZdkPN_aFeYY/AAAAAAAAAAI/AAAAAAAAAAA/Gf2XBEqFddI/s100-c-k-no-rj-c0xffffff/photo.jpg',
        },
        {
            # AJ+ ES
            'label': plugin.get_string(30001),
            'path': plugin.url_for('get_content', url='https://www.youtube.com/channel/UCS0lmlVIYVz2qeWlZ_ynIWg/videos'),
            'thumbnail': 'https://yt3.ggpht.com/-dIY2yXt4g6E/AAAAAAAAAAI/AAAAAAAAAAA/HfkzxVUID2c/s100-c-k-no-rj-c0xffffff/photo.jpg',
        },
        {
            # AJ+ AR
            'label': plugin.get_string(30002),
            'path': plugin.url_for('get_content', url='https://www.youtube.com/channel/UC-4KnPMmZzwAzW7SbVATUZQ/videos'),
            'thumbnail': 'https://yt3.ggpht.com/-Gp4qJ1iZHH4/AAAAAAAAAAI/AAAAAAAAAAA/EO7AVgoVh4Y/s100-c-k-no-rj-c0xffffff/photo.jpg',
        }
    ]
    
    return items


@plugin.route('/content/<url>')
def get_content(url):
    
    content = buzzfeedscraper.get_latest(url)
    items = []

    for i in content:
        items.append({
            'label': i['label'],
            'path': PLUGIN_URL + i['path'],
            'thumbnail': i['thumbnail'],
            'is_playable': True,
        })

    return items


if __name__ == '__main__':
    plugin.run()
