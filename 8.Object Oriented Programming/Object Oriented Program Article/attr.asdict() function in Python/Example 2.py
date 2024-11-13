import attr


@attr.s
class UserInfo(object):
	users = attr.ib()


@attr.s
class User(object):
	email = attr.ib()
	name = attr.ib()


# including only name and not email
attr.asdict(UserInfo([User("lee@har.invalid", "Lee"),
					User("rachel@har.invalid", "Rachel")]),
			filter=lambda attr, value: attr.name != "email")
