# app.py
import dash
from dash import html, Output, Input

# Create the Dash app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div([
    html.Button("Click Me", id="hello-button", n_clicks=0),
    html.Div(id="output-container")
])

# Callback to update output container
@app.callback(
    Output("output-container", "children"),
    Input("hello-button", "n_clicks")
)
def update_output(n_clicks):
    if n_clicks > 0:
        return "Hello World"
    return ""

# Run the app
if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8050)
