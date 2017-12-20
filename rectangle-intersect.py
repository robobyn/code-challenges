def get_rectangle_boundaries(rectangle_dimensions):
    """Given dimensions of a rectangle as a dict return as list.

    In: Dictionary containing rectangle's left x-axis coordinate as 'left_x',
    bottom y coordinate as 'bottom_y', 'width', and 'height'

    Returns: List containing left and right x-axis boundaries, top and bottom
    y-axis boundaries.

    >>> rectangle = {"left_x": 1, "bottom_y": 5, "width": 10, "height": 4}
    >>> get_rectangle_boundaries(rectangle)
    [1, 11, 5, 9]
    """

    left_point = rectangle_dimensions["left_x"]
    right_point = rectangle_dimensions["width"] + left_point
    bottom_point = rectangle_dimensions["bottom_y"]
    top_point = rectangle_dimensions["height"] + bottom_point

    return [left_point, right_point, bottom_point, top_point]


def get_intersection(rectangle_1, rectangle_2):
    """Given dimensions of 2 rectangles, return the dimensions of intersection.

    In: 2 dictionaries containing each rectangle's 'left_x', and 'bottom_y'
    coordinates, 'width', and 'height'.

    Returns: A single dictionary representing the dimensions of the rectangle
    where the two input values intersect.  If there is no intersection of the
    two rectangles return string 'No intersection'.

    >>> a_rectangle = {"left_x": 1, "bottom_y": 5, "width": 10, "height": 4}
    >>> next_rectangle = {"left_x": 2, "bottom_y": 4, "width": 13, "height": 8}
    >>> get_intersection(a_rectangle, next_rectangle)
    {'width': 9, 'left_x': 2, 'bottom_y': 5, 'height': 4}

    >>> no_intersect_1 = {"left_x": 1, "bottom_y": 5, "width": 4, "height": 4}
    >>> no_intersect_2 = {"left_x": 6, "bottom_y": 5, "width": 10, "height": 4}
    >>> get_intersection(no_intersect_1, no_intersect_2)
    'No intersection'
    """

    rect_1_left, rect_1_right, rect_1_bottom, rect_1_top = \
        get_rectangle_boundaries(rectangle_1)

    rect_2_left, rect_2_right, rect_2_bottom, rect_2_top = \
        get_rectangle_boundaries(rectangle_2)

    intersection = {}

    if rect_1_left >= rect_2_right or rect_2_left >= rect_1_right:
        return "No intersection"

    if rect_1_bottom >= rect_2_top or rect_2_bottom >= rect_1_top:
        return "No intersection"

    intersection["left_x"] = max(rect_1_left, rect_2_left)
    intersection["bottom_y"] = max(rect_1_bottom, rect_2_bottom)
    intersect_right = min(rect_1_right, rect_2_right)
    intersect_top = min(rect_1_top, rect_2_top)

    intersection["width"] = intersect_right - intersection["left_x"]
    intersection["height"] = intersect_top - intersection["bottom_y"]

    return intersection


if __name__ == "__main__":

    import doctest
    doctest.testmod()
