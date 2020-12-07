import utils

app = utils.create_app()


@app.route('/')
def index():
    return 'Hello 2 world'


if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=5000)
