#!/usr/bin/python3
""" Module for lockboxes problem """


def canUnlockAll(boxes):
    """
    Check if boxes can be unlocked
    Args:
        boxes(list): list of lists
    """
    for key in range(1, len(boxes)):
        found_key = False
        for idx in range(len(boxes)):
            if key in boxes[idx] and key != idx:
                found_key = True
                break
        if not found_key:
            return False
    return True
