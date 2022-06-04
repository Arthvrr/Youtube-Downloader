from flask import Flask, redirect, request, render_template, send_file, session, url_for
from pytube import YouTube
from io import BytesIO
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = "7472DQDHU2ID90AE82UDOA8DDJNA20UE1DN183UDU1"

@app.route('/', methods= ['GET','POST']) 
def home():
    if request.method == "POST":
        session['link'] = request.form.get("url")
        patternURL = re.compile("(?<=v=)\w{0,11}|(?<=youtu\.be\/)\w{0,11}",re.IGNORECASE)
        videoID = re.match(patternURL,session['link']) #Bout de code permettant d'obtenir l'url de la miniature (module re)
        reg_result = re.findall(patternURL, session["link"])
        video_id = video_url = reg_result[0] if reg_result else None
        if video_id:
            thumbnail_url = f"https://i3.ytimg.com/vi/{video_id}/maxresdefault.jpg"
        try: #regarder si l'url est valable ou non
            url = YouTube(session['link'])
            url.check_availability() #Fonction pytube vérifiant que l'url est valide 
        except:
            return render_template('error.html') #Si erreur on arrive à error.html
        return render_template("download.html",thumbnail=thumbnail_url, url=url)
    return render_template('home.html') #Si pas POST comme requête on reste dans le menu


@app.route("/download", methods=["GET","POST"])
def download_video():
    if request.method == "POST":
        url = YouTube(session['link'])
        str_url = str(url) #on convertir la variable url en string
        true_url = "https://www.youtube.com/" + str_url[41:52] #true_url nous donne l'url de base sur YouTube
        yt = YouTube(true_url)
        video_title = yt.title #Permet d'obtenir le titre de la vidéo YouTube (module pytube)
        format = request.form.get('format')
        buffer = BytesIO()
        url = YouTube(session['link'])
        itag = request.form.get("itag")
        video = url.streams.get_by_itag(itag)
        video.stream_to_buffer(buffer)
        buffer.seek(0)
        if format == "MP3": #Si le format sélectionné est MP3
            return send_file(buffer, as_attachment=True, download_name=video_title+".mp3")
        else: #Si le format choisi est MP4
            return send_file(buffer, as_attachment=True, download_name=video_title+".mp4", mimetype="video/mp4")
    return redirect(url_for('home')) #Si pas POST comme requête on retourne à home.html


@app.route("/faq", methods=["GET","POST"])
def faq():
    if request.method == "GET":
        try:
            return render_template('faq.html')
        except :
            return render_template('error.html')
    return redirect(url_for('home')) #Si pas POST comme requête on retourne à home.html

    
if __name__ == '__main__':
    app.run(debug=True)
