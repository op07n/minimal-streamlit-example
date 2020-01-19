from subprocess import Popen


def load_jupyter_server_extension(nbapp):
    """serve the bokeh-app directory with bokeh server"""
    Popen(["streamlit", "run", "st_runner.py", "apps", "--browser.serverAddress=0.0.0.0", "--server.enableCORS=False", "--browser.gatherUsageStats=False"])
