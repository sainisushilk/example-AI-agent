from langchain_core.tools import tool

@tool
def get_leave_info(leave_type: str) -> str:
    """Get company leave policy information.
    Supported leave types: casual, sick, maternity, paternity
    """
    policy = {
        "casual": "Casual leave is 12 days per year. Maximum 3 consecutive days allowed.",
        "sick": "Sick leave is 10 days per year. Medical certificate is required if leave exceeds 2 days.",
        "maternity": "Maternity leave is 26 weeks as per government rules.",
        "paternity": "Paternity leave is 7 days within 3 months of child birth.",
    }
    return policy.get(leave_type.lower().strip(), "Leave type not found in company policy.")


@tool
def weeks_to_days(weeks: int) -> int:
    """Convert weeks into days."""
    return weeks * 7


@tool
def calculate_remaining_leaves(total: int, used: int) -> int:
    """Calculate remaining leaves given total allotted and already used leaves."""
    return total - used


def get_tools():
    return [get_leave_info, weeks_to_days, calculate_remaining_leaves]