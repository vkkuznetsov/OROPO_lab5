from neomodel import StructuredNode, StringProperty, RelationshipTo, UniqueIdProperty


class User(StructuredNode):
    user_id = StringProperty(unique_index=True, required=True)
    screen_name = StringProperty()
    full_name = StringProperty()
    sex = StringProperty()
    city = StringProperty()
    following = RelationshipTo('User', 'FOLLOW')
    subscribed = RelationshipTo('Group', 'SUBSCRIBE')


class Group(StructuredNode):
    group_id = StringProperty(unique_index=True, required=True)
    group_name = StringProperty()
    screen_name = StringProperty()
    members = RelationshipTo('User', 'SUBSCRIBE')
