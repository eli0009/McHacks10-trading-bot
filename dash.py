from mainML import get_stock_prediction
import dash
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash()

app.layout = html.Div([
    html.H1("Hi! Welcome to the Stock Predictor"),
    html.P("Please enter a ticker symbol:"),
    dcc.Input(id="ticker", type="text"),
    html.Button(id="submit", children="Submit"),
    html.Div(id="output")
])

@app.callback(
    dash.dependencies.Output("output", "children"),
    [dash.dependencies.Input("submit", "noclick")],
    [dash.dependencies.State("ticker", "value")]
)
def predict_stock(noclick, ticker):
    if noclick is None:
        return ""

    decision = get_stock_prediction(ticker)

    if decision == 1:
        return "Buy"
    elif decision == -1:
        return "Sell"
    else:
        return "Hold"

if __name__ == "__main__":
    app.run_server(debug=True)
