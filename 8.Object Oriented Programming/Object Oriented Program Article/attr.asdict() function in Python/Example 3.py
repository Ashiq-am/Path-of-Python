import attr


@attr.s
class UserInfo(object):
	name = attr.ib()
	password = attr.ib()
	age = attr.ib()


# excluding attributes
print(attr.asdict(UserInfo("Marco", "abc@123", 22),
				filter=attr.filters.exclude(
					attr.fields(UserInfo).password, int)))


@attr.s
class Coordinates(object):
	x = attr.ib()
	y = attr.ib()
	z = attr.ib()


# inclusing attributes
print(attr.asdict(Coordinates(20, "5", 3),
				filter=attr.filters.include(int)))
