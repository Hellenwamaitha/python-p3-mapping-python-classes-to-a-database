#!/usr/bin/env python3

#!/usr/bin/env python3

from config import CONN, CURSOR
from song import Song
def reset_database():
    Song.drop_table()
    Song.create_table()
    Song.create("Hello", "25")
    Song.create("99 Problems", "The Black Album")


reset_database()
import pytest; pytest.set_trace()

if __name__ == '__main__':
    import ipdb; ipdb.set_trace()