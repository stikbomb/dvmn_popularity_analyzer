import plotly.express as px


def get_chart(wide_df):
    tidy_df = wide_df.melt(id_vars='dates')
    fig = px.bar(tidy_df, x="dates", y="value", color="variable", barmode="group")
    fig.show()
