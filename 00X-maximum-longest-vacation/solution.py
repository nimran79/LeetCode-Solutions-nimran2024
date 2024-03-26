def max_vacation(calendar, pto):
    """
    Args:
        calendar: A list of characters ('H' for holiday, 'W' for workday).
        pto: The number of available PTO days.

    Returns:
        The maximum vacation length (integer).
    """

    longest_vacation = 0
    current_streak = 0 
    pto_used = 0

    for day in calendar:
        current_streak += 1  # Increment the current vacation streak

        if day == 'W':
            if pto_used < pto:
                pto_used += 1  # Use a PTO day (if available)
            else:
                current_streak = 0  # Reset the streak if we can't use PTO
                pto_used = 0  # Reset PTO used as the streak broke

        longest_vacation = max(longest_vacation, current_streak)

    return longest_vacation
