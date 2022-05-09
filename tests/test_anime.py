from application_anime.models.anime import Anime, Episode

import pytest

@pytest.fixture
def one_piece():
    episode_1 = Episode("001", "/home/maxime.bettinelli/PycharmProjects/application-anime/application_anime/files/test3.mp4")
    return Anime("One Piece", "Eiichiro Oda", "adventure", [episode_1])


class TestAnime:

    def test_repr_anime(self, one_piece):
        assert str(one_piece) == "One Piece by Eiichiro Oda"
        assert one_piece.name == "One Piece"

    def test_play_pilot(self, one_piece):
        one_piece.play_pilot()