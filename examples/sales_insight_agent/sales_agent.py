import pandas as pd
from bindu import Agent


def analyze_sales_data(csv_path: str):
    """
    Load sales data and compute basic business insights.
    """

    data = pd.read_csv(csv_path)

    # Calculate revenue per row
    data["revenue"] = data["quantity"] * data["price"]

    # Total revenue
    total_revenue = float(data["revenue"].sum())

    # Revenue grouped by product
    revenue_by_product = (
        data.groupby("product")["revenue"]
        .sum()
        .sort_values(ascending=False)
    )

    # Take top 3 products
    top_products = revenue_by_product.head(3).to_dict()

    # Total transactions
    transaction_count = len(data)

    return {
        "total_revenue": total_revenue,
        "top_products": top_products,
        "transaction_count": transaction_count,
    }


# Create a Bindu Agent
agent = Agent(
    name="Sales Insight Agent",
    description="Analyzes structured sales CSV data and returns useful business insights.",
    model="openai/gpt-4o-mini",
)

agent.instructions = [
    "When requested, analyze the provided sales CSV data.",
    "Return results in structured JSON format.",
]


@agent.tool
def analyze_sales():
    """
    Tool that runs the sales analysis.
    """
    return analyze_sales_data("examples/sales_insight_agent/sample_sales.csv")


if __name__ == "__main__":
    agent.serve(port=3781)
