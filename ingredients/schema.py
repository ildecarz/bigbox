import graphene
from graphene_django import DjangoObjectType

from ingredients.models import Category, Ingredient


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "ingredients")

class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = ("id", "name", "notes", "category")

class CreateIngredients(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        id = graphene.ID()

    ok = graphene.Boolean()
    ingredients = graphene.Field(IngredientType)

    @classmethod
    def mutate(cls, root, info, name, id):
        ingredients = Ingredient.objects.get(pk=id)
        ingredients.name = name
        Ingredient.save()
        return CreateIngredients(ingredients=ingredients)

class MyMutations(graphene.ObjectType):
    create_ingredients = CreateIngredients.Field()

class Query(graphene.ObjectType):
    all_ingredients = graphene.List(IngredientType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    def resolve_all_ingredients(root, info):
        # We can easily optimize query count in the resolve method
        return Ingredient.objects.select_related("category").all()

    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None

schema = graphene.Schema(query=Query, mutation=MyMutations)