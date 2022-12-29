from django.db import models
from django.urls import reverse
from .ResourceCard import ResourceCard

html = str
Resource = ...


class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Имя меню", max_length=200)

    def render(self, request) -> html:
        parents = None
        result = []

        all_menu_resources = Resource.objects.filter(menu=self)
        first_level_resources = all_menu_resources.filter(parent=None)
        find_res = None

        for res in all_menu_resources:
            if res.absolute_url == request.path:
                find_res = res
                parents = find_res.parents
                break

        for resource in first_level_resources:
            result.append(resource.render(request, parents))

        return ''.join(result)

    def __str__(self) -> str:
        return self.name


class Resource(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.CharField(
        "Сссылка на ресурс(возможны пространства имен)",
        max_length=1000
    )
    parent = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='children',
        verbose_name='Родительский ресурс(пустой = верхний уровень меню)',
    )
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        related_name='resources',
        verbose_name="Является элементом меню",
    )
    url_is_namespace = models.BooleanField(
        "Пространство имен URL",
        default=False
    )

    def render(self, request, active_res_parents) -> html:
        card = ResourceCard(
            self,
            self.render_child(self.parent, request, active_res_parents),
            request,
            active_res_parents,
        )
        return card.render

    def render_child(self, parent, request, active_res_parents) -> bool:
        "Return true if it is desired resource or its parent."
        if self.absolute_url == request.path:
            return True

        if active_res_parents is None:
            return True

        if self in active_res_parents:
            return True

        return False

    @property
    def absolute_url(self) -> str:
        abs_url = self.url
        if self.url_is_namespace:
            abs_url = reverse(self.url)

        return abs_url

    @property
    def level(self) -> int:
        "Return resource level in tree."
        return len(self.parents)

    @property
    def parents(self) -> list[Resource]:
        "Return list of parents."
        p = self
        parents = []

        while p.parent:
            parents.append(p.parent)
            p = p.parent

        return parents

    def __str__(self):
        return (
            f"""
            Родитель: {self.parent.url if self.parent else 'Верхний уровень'}.
            Ссылка на ресурс: {self.url}
            """
        )
