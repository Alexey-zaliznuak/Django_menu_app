from django.template import loader

html = str

PX_MARGIN_LEFT = 40
PX_VERTICAL_MARGIN = 5


class ResourceCard():
    def __init__(self, res, render_child, request, active_res_parents) -> None:
        self.res = res
        self.render_child = render_child
        self.request = request
        self.active_res_parents = active_res_parents

    @property
    def render(self) -> html:
        res = self.res
        url = res.absolute_url
        child_html = ''
        horizontal_margin = res.level * PX_MARGIN_LEFT

        if self.render_child:
            for child in res.children.all():
                child_html += child.render(
                    self.request,
                    self.active_res_parents
                )

        context = {
            'vertical_margin': PX_VERTICAL_MARGIN,
            'horizontal_margin': horizontal_margin,
            'url': url,
            'child_html': child_html,
            'is_active': url == self.request.path
        }
        render = loader.render_to_string(
            'resource_card.html',
            context
        )

        return render
