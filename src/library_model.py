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

from elixir import *

metadata.bind = "sqlite:///music_library.sqlite"
metadata.bind.echo = True

class Artist(Entity):
    name = Field(Unicode(60))
    albums = OneToMany('Album')
    songs = OneToMany('Song')
    
    def __repr__(self):
        return '<Artist "%s">' % (self.name)
        
class Album(Entity):
    title = Field(UnicodeText)
    year = Field(UnicodeText)
    artist = ManyToOne('Artist')
    songs = OneToMany('Song')
    
    def __repr__(self):
        return '<Album "%s"> (%s)'%(self.title, self.year)
        
class Song(Entity):
    title = Field(UnicodeText)
    location = Field(UnicodeText)
    track_no = Field(Unicode(3))
    disc = Field(Unicode(2))
    artist = ManyToOne('Artist')
    album = ManyToOne('Album')
    genre = ManyToOne('Genre')
    
    def __repr__(self):
        return '<Song "%s - %s">'%(self.track_no, self.title)

class Genre(Entity):
    name = Field(Unicode(30))
    song = OneToMany('Song')
    
    def __repr__(self):
        return '<Genre "%s">'%(self.name)
