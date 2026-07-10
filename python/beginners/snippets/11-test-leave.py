def test_leave_dungeon_changes_state():
    me = Actor()
    me.enter_dungeon()
    me.leave_dungeon()
    assert "vor dem Verlies" in str(me)
