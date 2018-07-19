The problem is your __str__ is supposed to return string representation of self, and you print() instead, returning nothing. (`return None` is implied to be the last line of any method that does not return or yield.) Try this:


def __str__(self):
	tmp = self.head
	while tmp:
		s += str(tmp.value)
		if s.next:
			s += ','
	return '[' + s + ']'

