#! /usr/bin/env python3

import datetime
from string import Template

cal = dict()

def prompt_for_time():
        print("Enter date as YYYY-MM-DD:HH")
        time_str = input("> ")
        format_str = "%Y-%m-%d:%H"
        return datetime.datetime.strptime(time_str, format_str)

def create_event(time, desc):
        if time.date() not in cal:
                cal[time.date()] = dict()
        date_dict = cal[time.date()]
        if time.hour not in date_dict:
                date_dict[time.hour] = desc
        else:
                print("Event already exists.")

def add():
        print("Adding a new event.")
        time = prompt_for_time()
        add_time(time)

def add_time(time):
        found = False
        if time.date() in cal:
                date_dict = cal[time.date()]
                if time.hour in date_dict:
                        found = True
                        print("There already exists an event at that time.")
                        print("Do you want to edit the existing event?")
                        selection = input("> ").lower()
                        if selection == 'y':
                                edit_time(time)
                        else:
                                print("Event not edited.")
        if found == False:
                print("Enter event description.")
                desc = input("> ")
                create_event(time, desc)
                cal[time] = desc
                print("Event added.")

def delete():
        print("Deleting an event.")
        time = prompt_for_time()
        found = False
        if time.date() in cal:
                date_dict = cal[time.date()]
                if time.hour in date_dict:
                        found = True
                        print(date_dict[time.hour])
                        print("Are you sure you want to delete this event?")
                        selection = input("> ").lower()
                        if selection == 'y':
                                delete_event(time)
                                print("Event deleted.")
                        else:
                                print("Event not deleted.")
        if found == False:
                print("Event not found.")

def edit():
        print("Editing an event.")
        time = prompt_for_time()
        edit_time(time)

def edit_time(time):
        found = False
        if time.date() in cal:
                date_dict = cal[time.date()]
                if time.hour in date_dict:
                        found = True
                        print(date_dict[time.hour])
                        print("What is the new event description?")
                        date_dict[time.hour] = input("> ")
        if found == False:
                print("Event not found.")
                print("Do you want to add an event for this time?")
                selection = input("> ").lower()
                if selection == 'y':
                        add_time(time)
                else:
                        print("Event not added.")

def show():
        print("Showing events.")
        print("Enter date as YYYY-MM-DD")
        time_str = input("> ")
        format_str = "%Y-%m-%d"
        day = datetime.datetime.strptime(time_str, format_str)
        print(day.date())
        if day.date() in cal:
                day_dict = cal[day.date()]
                for hour in range(24):
                        desc = day_dict.get(hour, "")
                        template = Template("${h}: ${d}")
                        event = template.substitute(h=hour, d=desc)
                        print(event)
        else:
                print("No events found on that day.")

def display_menu_options():
        print("Options:")
        print("(A) Add an event.")
        print("(D) Delete an event.")
        print("(E) Edit an event.")
        print("(S) Show events.")
        print("(Q) Quit.")

def try_again():
        print("Uh. Try again.")
        print()

def menu():
        while(True):
                display_menu_options()
                selection = input("> ").lower()
                if selection == 'q':
                        print("See you later!")
                        return
                else:
                        fns = {'a': add, 'd': delete, 'e': edit, 's': show}
                        fns.get(selection, try_again)()
                print()

if __name__ == '__main__':
        menu()
