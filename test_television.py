import pytest
from television import Television

def test_initial_state(): """Tests the initial state of the televison"""
    tv = Television()
    assert str(tv) == "Power: Off, Channel: 0, Volume: 0"

def test_power(): """Tests that the power on the television has the ability to turn on and off"""
    tv = Television()
    tv.power()
    assert str(tv) == "Power: On, Channel: 0, Volume: 0"
    tv.power()
    assert str(tv) == "Power: Off, Channel: 0, Volume: 0"

def test_mute(): """Tests the status of the mute feature at the beginning of the program"""
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    assert str(tv) == "Power: On, Channel: 0, Volume: 0"
    tv.mute()
    assert str(tv) == "Power: On, Channel: 0, Volume: 1"

def test_channel_up(): """Tests the ability of the tv channels to be increased by 1"""
    tv = Television()
    tv.power()
    tv.channel_up()
    assert str(tv) == "Power: On, Channel: 1, Volume: 0"
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    assert str(tv) == "Power: On, Channel: 0, Volume: 0"

def test_channel_down(): """Tests the ability of the tv channels to be decreased by 1"""
    tv = Television()
    tv.power()
    tv.channel_down()
    assert str(tv) == "Power: On, Channel: 3, Volume: 0"
    tv.channel_down()
    assert str(tv) == "Power: On, Channel: 2, Volume: 0"

def test_volume_up(): """Tests the ability of the volume feature to increase by 1"""
    tv = Television()
    tv.power()
    tv.volume_up()
    assert str(tv) == "Power: On, Channel: 0, Volume: 1"
    tv.volume_up()
    tv.volume_up()
    assert str(tv) == "Power: On, Channel: 0, Volume: 2"
    tv.volume_up()  # Exceeding max volume
    assert str(tv) == "Power: On, Channel: 0, Volume: 2"

def test_volume_down(): """Tests that the volume down feature can decrease the volume by 1"""
    tv = Television()
    tv.power()
    tv.volume_down()  # Already at minimum
    assert str(tv) == "Power: On, Channel: 0, Volume: 0"
    tv.volume_up()
    tv.volume_up()
    tv.volume_down()
    assert str(tv) == "Power: On, Channel: 0, Volume: 1"