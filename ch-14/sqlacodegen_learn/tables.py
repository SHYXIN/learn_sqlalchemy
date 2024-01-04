# sqlacodegen sqlite:///Chinook_Sqlite.sqlite --tables Artist,Track > tables.py
# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, NVARCHAR, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Artist(Base):
    __tablename__ = 'Artist'

    ArtistId = Column(Integer, primary_key=True, unique=True)
    Name = Column(NVARCHAR(120))


class Genre(Base):
    __tablename__ = 'Genre'

    GenreId = Column(Integer, primary_key=True, unique=True)
    Name = Column(NVARCHAR(120))


class MediaType(Base):
    __tablename__ = 'MediaType'

    MediaTypeId = Column(Integer, primary_key=True, unique=True)
    Name = Column(NVARCHAR(120))


class Album(Base):
    __tablename__ = 'Album'

    AlbumId = Column(Integer, primary_key=True, unique=True)
    Title = Column(NVARCHAR(160), nullable=False)
    ArtistId = Column(ForeignKey('Artist.ArtistId'), nullable=False, index=True)

    Artist = relationship('Artist')


class Track(Base):
    __tablename__ = 'Track'

    TrackId = Column(Integer, primary_key=True, unique=True)
    Name = Column(NVARCHAR(200), nullable=False)
    AlbumId = Column(ForeignKey('Album.AlbumId'), index=True)
    MediaTypeId = Column(ForeignKey('MediaType.MediaTypeId'), nullable=False, index=True)
    GenreId = Column(ForeignKey('Genre.GenreId'), index=True)
    Composer = Column(NVARCHAR(220))
    Milliseconds = Column(Integer, nullable=False)
    Bytes = Column(Integer)
    UnitPrice = Column(Numeric(10, 2), nullable=False)

    Album = relationship('Album')
    Genre = relationship('Genre')
    MediaType = relationship('MediaType')
