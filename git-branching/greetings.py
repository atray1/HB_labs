"""A file with different ways to greet people."""


def get_friendly_greeting(name):
	"""Provide a greeting that is friendly, given a name."""

	return "Hi {}, glad to see you!".format(name)


def get_grumpy_greeting(name):
	"""Provide a greeting that is grumpy, given a name."""

	return "Ugh, hey {}".format(name)


def get_neutral_greeting(name):
	"""Provide a greeting that is neutral, given a name."""

	return "Hi {}".format(name)