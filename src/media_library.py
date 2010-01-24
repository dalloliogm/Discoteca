#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       untitled.py
#       
#       Copyright 2010 Brandon Invergo <brandon@brandoninvergo.com>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

from library_model import *
import os
from mutagen import File as audio_file

def init_db():
    setup_all()
    if not os.access('music_library.sqlite',os.F_OK):
        create_all()
    
def scan_folder(path):
    contents = os.walk(path)
    for root, dirs, files in contents:
        for f in files:
            path = os.path.join(root,f)
            file = audio_file(path)
            if file:
                artist = file.get("TPE1")
                if artist:
                    artist_txt = unicode(artist.text[0])
                else:
                    artist_txt = u"Unknown Artist"
                album_artist = file.get("TPE2")
                if album_artist:
                    album_artist_txt = unicode(album_artist.text[0])
                else:
                    album_artist_txt = artist_txt
                disc = file.get("TPOS")
                if disc:
                    disc_txt = unicode(disc.text[0])
                else:
                    disc_txt = u""
                genre = file.get("TCON")
                if genre:
                    genre_txt = unicode(genre.text[0])
                else:
                    genre_txt = u""
                album = file.get("TALB")
                if album:
                    album_txt = unicode(album.text[0])
                else:
                    album_txt = u"Unknown Album"
                title = file.get("TIT2")
                if title:
                    title_txt = unicode(title.text[0])
                else:
                    title_txt = u"Unknown Song"
                track = file.get("TRCK")
                if track:
                    track_txt = unicode(track.text[0])
                else:
                    track_txt = u""
                year = file.get("TDRC")
                if year:
                    year_txt = unicode(year.text[0])
                else:
                    year_txt = u""
                
                db_artist = Artist.get_by(name=artist_txt)
                if not db_artist:
                    db_artist = Artist(name=artist_txt)

                db_album_artist = Artist.get_by(name=album_artist_txt)
                if not db_album_artist:
                    db_album_artist = Artist(name=album_artist_txt)

                db_album = Album.get_by(title=album_txt, \
                                    artist=db_album_artist)
                if not db_album:
                    db_album = Album(title=album_txt,\
                                    artist=db_album_artist,\
                                    year=year_txt)

                db_genre = Genre.get_by(name=genre_txt)
                if not db_genre:
                    db_genre = Genre(name=genre_txt)
                try:
                    Song(title=title_txt, location=unicode(path), \
                        track_no=track_txt, disc=disc_txt, \
                        artist=db_artist, album=db_album,\
                        genre=db_genre)
                except:
                    print "**************damn**************"
                session.commit()
    
def main():
    init_db()
    scan_folder('/media/5AE279806AA2F2DD/MP3s/')
    
if __name__ == '__main__':
	main()
    

