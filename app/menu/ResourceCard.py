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
        horizontal_margin = res.level * PX_MARGIN_LEFT

        result = '<div>'
        result += (
            '<a class="btn btn-primary"'
            + f'style="margin: {PX_VERTICAL_MARGIN}px {horizontal_margin}px" '
            + f'href="{url}"'
            + f'role="button">{url}</a> '
        )

        if self.render_child:
            for child in res.children.all():
                result += child.render(self.request, self.active_res_parents)

        return result + '</div>'
