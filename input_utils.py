class InputException(Exception):
    pass


def ask_for_input(sentence, is_mandatory: bool = False, max_failed_attempts: int = 5):
    for _ in range(max_failed_attempts):
        user_input = input(sentence)
        is_valid_input = validate_input(user_input)
        if is_valid_input:
            return user_input
        if not is_valid_input and not is_mandatory:
            return None
    raise InputException("Too many attempts")


def validate_input(user_input: str):
    return not user_input.strip() == ''


def validate_and_parse_tags(tags_as_str: str):
    # todo add validation
    return tags_as_str.split(",")
