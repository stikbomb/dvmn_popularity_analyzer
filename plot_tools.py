import plotly.graph_objects as go


def get_chart(stats_by_period):
    dates = []
    counts = []
    for item in stats_by_period:
        dates.append(item[0])
        counts.append(item[1])

    fig = go.Figure([go.Bar(x=dates, y=counts)])
    fig.show()


def get_group_chart(dates, results):

    fig = go.Figure(data=[
        go.Bar(name='Pepsi', x=dates, y=results[0]),
        go.Bar(name='7UP', x=dates, y=results[1]),
        go.Bar(name='Купаты', x=dates, y=results[2]),
    ])
    # Change the bar mode
    fig.update_layout(barmode='group')
    fig.show()
