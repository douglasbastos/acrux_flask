from news_app import create_app

app = create_app(config_filename='/home/douglas/workspace/acrux_flask/settings.py')
app.run(debug=True, use_reloader=True)
