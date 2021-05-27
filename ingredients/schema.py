import graphene
from graphene_django import DjangoObjectType
from graphene_django import DjangoListField

from ingredients.models import Category, Ingredient


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name")

class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = ("id", "name", "notes", "category")

class CategoryMutation(graphene.Mutation):
    
    class Arguments:
        id = graphene.ID()
        name = graphene.String(required=True)
        
    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(self, root, info, name):
        category = Category(name=name)
        category.save()
        return CategoryMutation(category=category)

class Mutation(graphene.ObjectType):
    update_ingredients = CategoryMutation.Field()

class Query(graphene.ObjectType):
    all_ingredients = graphene.List(IngredientType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    def resolve_all_ingredients(root, info):
        # We can easily optimize query count in the resolve method
        return Ingredient.objects.select_related("category").all()

    def resolve_category_by_name(root, info, name):
        return Category.objects.get(name=name)

schema = graphene.Schema(query=Query, mutation=Mutation)