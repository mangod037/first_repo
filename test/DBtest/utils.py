from django.utils.text import slugify

def uniqueSlugGenerator(modelInstance, name, slug_field):
    slug = slugify(name)
    modelClass = modelInstance.__class__
    while modelClass._default_manager.filter(slug=slug).exists():
        objectPk = modelClass._default_manager.latest('pk')
        objectPk = objectPk.pk + 1
        slug = f"{slug}-{objectPk}"
    return slug

