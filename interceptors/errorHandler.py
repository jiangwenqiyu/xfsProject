from app import app
@app.errorhandler(404)
def error_404(e):
    return "找不到这个页面"