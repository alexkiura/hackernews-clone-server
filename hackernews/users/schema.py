from django.contrib.auth import get_user_model

import graphene
from graphene_django import DjangoObjectType

USER_MODEL = get_user_model()


class UserType(DjangoObjectType):
    class Meta:
        model = USER_MODEL


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email):
        user = USER_MODEL(
            username=username,
            email=email
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
