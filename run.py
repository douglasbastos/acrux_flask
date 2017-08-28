import sys
from news_app import create_app


mode = sys.argv[1] if not len(sys.argv) else 'development'
app = create_app(mode)
app.run()
