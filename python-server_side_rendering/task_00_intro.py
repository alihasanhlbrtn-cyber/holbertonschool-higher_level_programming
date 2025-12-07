#!/usr/bin/python3
"""
Simple templating program to generate invitation files
from a template string and a list of attendee dictionaries.
"""

import os


def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template and a list of attendees.

    - template: string with placeholders {name}, {event_title}, {event_date}, {event_location}
    - attendees: list of dictionaries, each representing one attendee
    """
    
    if not isinstance(template, str):
        print("Invalid template, expected a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Invalid attendees, expected a list of dictionaries.")
        return

    
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    
    for index, attendee in enumerate(attendees, start=1):
    
        name = attendee.get("name") or "N/A"
        event_title = attendee.get("event_title") or "N/A"
        event_date = attendee.get("event_date") or "N/A"
        event_location = attendee.get("event_location") or "N/A"

    
        processed = template
        processed = processed.replace("{name}", str(name))
        processed = processed.replace("{event_title}", str(event_title))
        processed = processed.replace("{event_date}", str(event_date))
        processed = processed.replace("{event_location}", str(event_location))

        
        filename = f"output_{index}.txt"

        
        try:
            
            with open(filename, "w", encoding="utf-8") as f:
                f.write(processed)
        except OSError as e:
            print(f"Error writing file {filename}: {e}")
