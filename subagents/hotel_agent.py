from google.adk import Agent

hotel_agent = Agent(
    name="hostel_agent",
    model="gemini-2.0-flash",
    description="Fing hotels within the destination and budget for the given dates",
    instruction="""
                You are a hotel booking agent. The coordinator will give you:
                - origin
                - destination
                - start_date
                - end_date
                - budget_amount
                - budget_currancy

                Return 1-2 mock hostel options including:
                - Hotel name
                - Nightly rate and total cost in the give currency
                - Main features

                Ensure total price fits the budget.
    """
)