from personaapi import app, engine
from personaapi.models import Base

import sys


if __name__ == '__main__':
    argument_list = sys.argv[1:] if len(sys.argv) > 1 else [None]

    if argument_list[0] == 'init':
        Base.metadata.create_all(engine)

    app.run(port=7070)
