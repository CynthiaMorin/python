import pytest
from television import Television

"""As shown in the lab 12 instructions I am using the str method to check the tv values"""

def test_initial_state(): """Tests the initial state of the televison"""
    tv = Television()
    assert str(tv) == "Power: Off, Channel: 0, Volume: 0"

def test_power(): """Tests that the power on the television has the ability to turn on and off"""
    tv = Television()
    tv.power()
    assert str(tv) == "Power: On, Channel: 0, Volume: 0"
    tv.power()
    assert str(tv) == "Power: Off, Channel: 0, Volume: 0"

def test_mute(): """Tests that the tv details when the tv is on, volume increased once,
and then tv muted. Tests when tv is on and unmuted, off and muted, or off and unmuted."""
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    assert str(tv) == "Power: On, Channel: 0, Volume: 0"
    tv.mute()
    assert str(tv) == "Power: On, Channel: 0, Volume: 1"

def test_channel_up(): """Tests that the tv deetails when the tv is off and channel is increased,
when tv is on and channel is increased, and when tv is on and one has increased the channel past the max value."""
    tv = Television()
    tv.power()
    tv.channel_up()
    assert str(tv) == "Power: On, Channel: 1, Volume: 0"
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    assert str(tv) == "Power: On, Channel: 0, Volume: 0"

def test_channel_down(): """Tests that the tv details when tv is off and channel is decreased,
and when tv is on and one has decreased channel past the minimum value"""
    tv = Television()
    tv.power()
    tv.channel_down()
    assert str(tv) == "Power: On, Channel: 3, Volume: 0"
    tv.channel_down()
    assert str(tv) == "Power: On, Channel: 2, Volume: 0"

def test_volume_up(): """Tests that the tv details when the tv is off and volume is increased,
when tv is on and volume is increased, tv is on and muted when volume is increased,
and when tv is on and one increases volume past the max value"""
    tv = Television()
    tv.power()
    tv.volume_up()
    assert str(tv) == "Power: On, Channel: 0, Volume: 1"
    tv.volume_up()
    tv.volume_up()
    assert str(tv) == "Power: On, Channel: 0, Volume: 2"
    tv.volume_up()  # Exceeding max volume
    assert str(tv) == "Power: On, Channel: 0, Volume: 2"

def test_volume_down(): """Tests that the tv details when the tv is off and volume is decreased,
when the tv is on and volume is decreased, and when tv is on and muted and volume is decreased, and finally
that the tv is on and one has decreased the volume past the minimum value"""
    tv = Television()
    tv.power()
    tv.volume_down()  # Already at minimum
    assert str(tv) == "Power: On, Channel: 0, Volume: 0"
    tv.volume_up()
    tv.volume_up()
    tv.volume_down()
    assert str(tv) == "Power: On, Channel: 0, Volume: 1"