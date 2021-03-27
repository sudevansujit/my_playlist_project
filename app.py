from flask import Flask, render_template
from pymongo import MongoClient
from flask import Flask, render_template, request, redirect, url_for 


client = MongoClient()
db = client.Playlister
playlists = db.playlists

def video_url_creator(id_lst):
    videos = []
    for vid_id in id_lst:
        # We know that embedded YouTube videos always have this format
        video = 'https://youtube.com/embed/' + vid_id
        videos.append(video)
    return videos

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    # change the original return statement you wrote to the one below
    return render_template('home.html', msg='Flask is Cool!!')


# OUR MOCK ARRAY OF PROJECTS
playlists = [
{ 'title': 'Cat Videos', 'description': 'Cats acting weird' },
    { 'title': '80\'s Music', 'description': 'Don\'t stop believing!' }
]

@app.route('/playlists')
def playlists_index():
    """Show all playlists."""
    return render_template('playlists_index.html', playlists=playlists)

@app.route('/playlists/new')
def playlists_new():
    """Create a new playlist."""
    return render_template('playlists_new.html')

# @app.route('/playlists', methods=['POST'])
# def playlists_submit():
#     """Submit a new playlist."""
#     print(request.form.to_dict())
#     return redirect(url_for('playlists_index'))

# @app.route('/playlists', methods=['POST'])
# def playlists_submit():
#     """Submit a new playlist."""
#     playlist = {
#         'title': request.form.get('title'),
#         'description': request.form.get('description')
#     }
#     playlists.insert_one(playlist)
#     return redirect(url_for('playlists_index'))

# Note the methods parameter that explicitly tells the route that this is a POST
@app.route('/playlists', methods=['POST'])
def playlists_submit():
    """Submit a new playlist."""
    # Grab the video IDs and make a list out of them
    video_ids = request.form.get('video_ids').split()
    # call our helper function to create the list of links
    videos = video_url_creator(video_ids)
    playlist = {
        'title': request.form.get('title'),
        'description': request.form.get('description'),
        'videos': videos,
        'video_ids': video_ids
    }
    playlists.insert_one(playlist)
    return redirect(url_for('playlists_index'))


















