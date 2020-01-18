from subprocess import Popen


def load_jupyter_server_extension(nbapp):
    """serve the bokeh-app directory with bokeh server"""
    Popen(["streamlit", "st_runner.py", "apps", "--server.enableCORS=False", "--browser.gatherUsageStats=False"])
