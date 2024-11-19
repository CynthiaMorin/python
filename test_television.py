import pytest
from television import Television

def test_initial_state():
    tv = Television()
    assert str(tv) == "Power: Off, Channel: 0, Volume: 0"

def test_power():
    tv = Television()
    tv.power()
    assert str(tv) == "Power: On, Channel: 0, Volume: 0"
    tv.power()
    assert str(tv) == "Power: Off, Channel: 0, Volume: 0"

def test_mute():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    assert str(tv) == "Power: On, Channel: 0, Volume: 0"
    tv.mute()
    assert str(tv) == "Power: On, Channel: 0, Volume: 1"

def test_channel_up():
    tv = Television()
    tv.power()
    tv.channel_up()
    assert str(tv) == "Power: On, Channel: 1, Volume: 0"
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    assert str(tv) == "Power: On, Channel: 0, Volume: 0"

def test_channel_down():
    tv = Television()
    tv.power()
    tv.channel_down()
    assert str(tv) == "Power: On, Channel: 3, Volume: 0"
    tv.channel_down()
    assert str(tv) == "Power: On, Channel: 2, Volume: 0"

def test_volume_up():
    tv = Television()
    tv.power()
    tv.volume_up()
    assert str(tv) == "Power: On, Channel: 0, Volume: 1"
    tv.volume_up()
    tv.volume_up()
    assert str(tv) == "Power: On, Channel: 0, Volume: 2"
    tv.volume_up()  # Exceeding max volume
    assert str(tv) == "Power: On, Channel: 0, Volume: 2"

def test_volume_down():
    tv = Television()
    tv.power()
    tv.volume_down()  # Already at minimum
    assert str(tv) == "Power: On, Channel: 0, Volume: 0"
    tv.volume_up()
    tv.volume_up()
    tv.volume_down()
    assert str(tv) == "Power: On, Channel: 0, Volume: 1"