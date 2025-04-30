from google.adk import Agent
from .subagents import flight_agent
from .subagents import hotel_agent
from datetime import datetime, timedelta
import pytz


# class GetCurrentDateTimeTool(Tool):
#     name = "get_current_date_time"
#     description = "Retrieves the current date and time."
def GetCurrentDateTimeTool() -> datetime:
    """Retrieves the current date and time in IST."""
    india_timezone = pytz.timezone('Asia/Kolkata')
    current_time_india = datetime.now(india_timezone).strftime("%Y-%m-%d %H:%M:%S %Z%z")
    return current_time_india

# async def add_current_date(ctx: InvocationContext):
#     ctx.user_state['today'] = datetime.today().date().isoformat()
#     return ctx

# today = datetime.today().date()
coordinator_agent = Agent(
    name= "tarvel_coordinator",
    model="gemini-2.0-flash",
    description="Main coordinator that gathers travel preferences and queries the sub-agents",
    instruction="""
                You are a travel planning coordinator.
                Your taek is to gather travel preferences from the usr and cooredinate with sub-agents  to provide flight, hostel suggestions with day plans.
                You will recieve user input in natural lanuguage and need to extract the following details:

                Note that maximum budget should be used for both the flight and hotel suggestions, it should not be exceeded when combined.
                If the user doesnt specify the start_date, but something like "Next week", "Next month", or "Next year", convert it to a date format by taking

                Step 1: Extract the following details from the user's input:
                - Origin (departure location)
                - destination
                - start_date (format: YYYY-MM-DD)
                - end_date (format: YYYY-MM-DD)
                - budget_amount (number)
                - budget_currency (e.g. USD, LKR, $, INR)

                Step 2: If any of these details are missing or unclear:
                - For the start_date: If the user doesn't provide it, ask if they would like to use today's date or specify a preferred start date.
                - You can use the 'get_current_date_time' tool to know the current time.
                - For the end_date: If the user only providers the number of days , calculate the end_date based on today's date or the provided start date.
                    If no start_date is provided, ask the user to specify a preferred date or default to today's date ({today_static.isoformat()}).
                - If the user does not provide a budget currency, assume "INR" by default, unless stated otherwise.

                Step 3: Once all details are gathered:
                - Confirm the travel preferences with the user (Origin, destination, start_date, end_date, budget)
                - If there is any ambiguity, ask the user to confirm.

                Step 4: send the data to the respective agents:
                - `flight_agent` for flight suggestions
                - `hotel_agent` for hotel suggestions

                Step 5: Present a final results combining the results from both the agents and a day plan including:
                - trip summary with all details (origin, destination, start_date, end_date, budget)
                - Note that maximum budget should be used for both the flight and hotel suggestions, it should not be exceeded when combined.
                - Flight suggestions
                - Hostel suggestions
                - Total estimated cost
                - A suggested day plan for the trip, including activities and places to visit in the destination.

                Be concise, clear, and friendly in guiding the user. If you encounter any missing information, ask the user for clarification.
    """,
    sub_agents=[flight_agent.flight_agent, hotel_agent.hotel_agent],
    tools=[GetCurrentDateTimeTool]
)

root_agent = coordinator_agent