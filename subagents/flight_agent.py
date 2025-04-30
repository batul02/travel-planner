from google.adk import Agent

flight_agent = Agent(
    name="flight_agent",
    model="gemini-2.0-flash",
    description="Suggest flights based on origin, destination, travel dates and the budget",
    instruction="""
                You are a flight booking agent. The coordinator will give you:
                - origin
                - destination
                - start_date
                - end_date
                - budget_amount
                - budget_currancy

                Return 1-2 mock flight options including:
                - Airline name
                - Departure and return date/time
                - Price in the specified currency
                - Class (Economy/Business)

                Make sure the total price is within the budget.
    """
)